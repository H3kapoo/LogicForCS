# Utility functions for LCS programs

from math import log2
from random import randint as rand

# Connectives and vars
con = ['!', '^', '|', '-', '>']
atms = []
possible_bool = []
answer_pool = []

# Info Prompt
def Prompt():
    print('# neg !')
    print('# and ^')
    print('# or |')
    print('# imp >')
    print('# equ -')
    print()

# Truth Function !
def neg(ipt):
    if ipt == 'T':
        return 'F'
    else:
        return 'T'

# Truth Function ^
def and_(ipt1, ipt2):
    if ipt1 == 'T' and ipt2 == 'T':
        return 'T'
    else:
        return 'F'

# Truth Function |
def or_(ipt1, ipt2):
    if ipt1 == 'F' and ipt2 == 'F':
        return 'F'
    else:
        return 'T'

# Truth Function >
def imp(ipt1, ipt2):
    if ipt1 == 'T' and ipt2 == 'F':
        return 'F'
    else:
        return 'T'

# Truth Function -
def equ(ipt1, ipt2):
    if (ipt1 == 'T' and ipt2 == 'T') or (ipt1 == 'F' and ipt2 == 'F'):
        return 'T'
    else:
        return 'F'

# Truth result of sub-proposition of type 1 or 2
def BooleanType(prop, type_):
    if type_ == 1:
        return neg(prop[2])

    if type_ == 2:
        if prop[2] == '^':
            return and_(prop[1], prop[3])
        if prop[2] == '|':
            return or_(prop[1], prop[3])
        if prop[2] == '-':
            return equ(prop[1], prop[3])
        if prop[2] == '>':
            return imp(prop[1], prop[3])
    return '---'

# Returns the truth value for the prop of type type_
def booleanFunction(prop, type_):
    if type_ == 1:
        return neg(prop[2])

    if type_ == 2:
        if prop[2] == '^':
            return and_(prop[1], prop[3])
        if prop[2] == '|':
            return or_(prop[1], prop[3])
        if prop[2] == '-':
            return equ(prop[1], prop[3])
        if prop[2] == '>':
            return imp(prop[1], prop[3])
    return '---'


# Generates all possible combinations of 'nr' unique atoms
def GenerateBool(nr):
    nr_atoms = nr
    spots = 2**nr
    put_true = True
    halfing = spots/2
    ctr = 0

    for i in range(0, nr):
        for x in range(0, spots):
            if ctr < halfing and put_true == True:
                possible_bool.append('T')
                ctr += 1
            elif ctr < halfing and put_true == False:
                possible_bool.append('F')
                ctr += 1
            else:
                put_true = not put_true
                if put_true:
                    possible_bool.append('T')
                if not put_true:
                    possible_bool.append('F')
                ctr = 1

        halfing //= 2

    return possible_bool

#Replaces atoms with truth values given at the time of calling
def booleanReplace(p):
    print()
    atoms = set()

    for l in p:
        if (l).isalpha() and (l not in atoms):
            print('Truth value for ', l, ' is (T/F): ', end='')
            repWith = input()
            p = p.replace(l, repWith)
            atoms.add(l)

    print()
    print('--->Proposition in boolean form: ', p)
    print()
    return p

# Replaces atoms with the truth values at 'index' (needs GenerateBool)
def BooleanReplace(p, index, nr, possible_bool):
    #print()
    atoms = set()
    i = 0

    for l in p:
        if (l).isalpha() and (l not in atoms):
            repWith = possible_bool[index+(2**nr)*i]
            p = p.replace(l, repWith)
            atoms.add(l)
            if l not in atms:
                atms.append(l)
            i += 1
    return p


# Analyzes the proposition 'p' (is in BooleanForm), appends an (T/F) answer for the pool
def Analyze(prop):
    op = 0
    cp = 0
    found_cp = False
    valid_flag = False

    if len(prop) == 1 and (prop).isalpha():  # check for atoms
        #print('---> Result of boolean operation: ', prop)
        if prop == 'T':
            answer_pool.append('T')
            return 'T'
        else:
            answer_pool.append('F')
            return 'F'

    for i in range(0, len(prop)):  # find last open par
        if prop[i] == '(':
            op = i
    for i in range(op, len(prop)):  # find first close par
        if prop[i] == ')':
            cp = i
            break

    # verify for type I
    if cp - op == 3 and prop[op + 1] == '!' and (prop[op + 2]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + ')'
        bool_value = BooleanType(sprop, 1)
        prop = prop.replace(sprop, bool_value, 1)
        valid_flag = True

    # type II
    elif cp - op == 4 and (prop[op + 1]).isalpha() and (prop[op + 2] in con) and (prop[op + 3]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + prop[op + 3] + ')'
        bool_value = BooleanType(sprop, 2)
        prop = prop.replace(sprop, bool_value, 1)
        valid_flag = True

    if valid_flag:
        Analyze(prop)

# Analyzes the proposition 'p' (is in BooleanForm),just returns (T/F) no answer_pool appends
def AnalyzeBoolSingleShot(prop):
    op = 0
    cp = 0
    found_cp = False
    valid_flag = False

    if len(prop) == 1 and (prop).isalpha():  # check for atoms
        print('---> Result of boolean operation: ', prop)
        return

    for i in range(0, len(prop)):  # find last open par
        if prop[i] == '(':
            op = i
    for i in range(op, len(prop)):  # find first close par
        if prop[i] == ')':
            cp = i
            break

    # verify for type I
    if cp - op == 3 and prop[op + 1] == '!' and (prop[op + 2]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + ')'
        bool_value = booleanFunction(sprop, 1)
        print('Step---> ', sprop, ' gets replaced with: ', bool_value)
        print()
        prop = prop.replace(sprop, bool_value, 1)
        print('--->Proposition to analyze: ', prop)
        print()
        valid_flag = True

    # type II
    elif cp - op == 4 and (prop[op + 1]).isalpha() and (prop[op + 2] in con) and (prop[op + 3]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + prop[op + 3] + ')'
        bool_value = booleanFunction(sprop, 2)
        print('Step---> ', sprop, ' gets replaced with: ', bool_value)
        print()
        prop = prop.replace(sprop, bool_value, 1)
        print('--->Proposition to analyze: ', prop)
        print()
        valid_flag = True

    if valid_flag:
        AnalyzeBoolSingleShot(prop)
    else:
        print("Error flag checked.Proposition fails the test.Not a WFF.")

# Get the answer pool
def GetAnswerPool():
    return answer_pool

#Reset AnswerPool
def ResetAnswerPool():
    answer_pool.clear()
    return []

# Validity Check
def Validity(answer_pool, mode):
    if len(answer_pool) > 0:
        if(mode == 'default'):
            pass
        if (mode == 'pretty'):
            PrettyPrint()

        true = 0
        false = 0

        for x in answer_pool:
            if x == 'T':
                true += 1
            else:
                false += 1

        if true > 0 and false == 0:
            print('Proposition: Valid ')
        if true > 0 and false > 0:
            print('Proposition: Satisfiable,Invalid ')
        if true == 0 and false > 0:
            print('Proposition: Unsatisfiable ')
    else:
        print("Error flag checked.Proposition fails the test.Not a WFF.")

# Nice Add-ons
def PrettyPrint():
    print()

    nr_atoms = int(log2(len(answer_pool)))

    print('  ', end='')

    for a in atms:
        print(a, ' |  ', end='')

    print('Answer')
    print('--------'*nr_atoms)

    to_print = '  '
    for i in range(0, 2 ** nr_atoms):
        for j in range(0, nr_atoms):
            to_print += possible_bool[i + (2 ** nr_atoms) * j] + '  |  '
        to_print += answer_pool[i]
        print(to_print)
        print('--------'*nr_atoms)
        to_print = '  '

#Analyze non boolean form proposition
def AnalyzeNonBool(prop):
    op = 0
    cp = 0
    found_cp = False
    valid_flag = False

    if len(prop) == 1 and (prop).isalpha():  # check for atoms
        print('In the end,this is a correct proposition.')
        return

    for i in range(0, len(prop)):  # find last open par
        if prop[i] == '(':
            op = i
    for i in range(op, len(prop)):  # find first close par
        if prop[i] == ')':
            cp = i
            break

    # verify for type I
    if cp - op == 3 and prop[op + 1] == '!' and (prop[op + 2]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + ')'
        atom = chr(rand(65, 90))
        print(sprop, ' gets replaced with ', atom)
        print()
        prop = prop.replace(sprop, atom, 1)
        print('Proposition to analyze ', prop)
        valid_flag = True

    # type II
    elif cp - op == 4 and (prop[op + 1]).isalpha() and (prop[op + 2] in con) and (prop[op + 3]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + prop[op + 3] + ')'
        atom = chr(rand(65, 90))
        print(sprop, ' gets replaced with ', atom)
        print()
        prop = prop.replace(sprop, atom, 1)
        print('Proposition to analyze ', prop)
        valid_flag = True

    else:
        print('Invalid expression: ', prop, ' ,matches no type.')

    if valid_flag:
        AnalyzeNonBool(prop)

