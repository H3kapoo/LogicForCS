# WFF all interpretations and validity check

import lcsHelperFunc as lcs

con = ['!', '^', '|', '-', '>']

def neg(ipt):
    if ipt == 'T':
        return 'F'
    else:
        return 'T'

def and_(ipt1, ipt2):
    if ipt1 == 'T' and ipt2 == 'T':
        return 'T'
    else:
        return 'F'

def or_(ipt1, ipt2):
    if ipt1 == 'F' and ipt2 == 'F':
        return 'F'
    else:
        return 'T'

def imp(ipt1, ipt2):
    if ipt1 == 'T' and ipt2 == 'F':
        return 'F'
    else:
        return 'T'

def equ(ipt1, ipt2):
    if (ipt1 == 'T' and ipt2 == 'T') or (ipt1 == 'F' and ipt2 == 'F'):
        return 'T'
    else:
        return 'F'

def boolean(prop, type_):
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

def booleanReplace(p, index, nr):
    print()
    atoms = set()
    i = 0

    for l in p:
        if (l).isalpha() and (l not in atoms):
            repWith = possible_bool[index+(2**nr)*i]
            p = p.replace(l, repWith)
            atoms.add(l)
            i += 1

    print()
    print('--->Proposition in boolean form: ', p)
    print()
    return p

def analyze(prop):
    op = 0
    cp = 0
    found_cp = False
    valid_flag = False

    if len(prop) == 1 and (prop).isalpha():  # check for atoms
        print('---> Result of boolean operation: ', prop)
        if prop == 'T':
            answer_pool.append('T')
            return
        else:
            answer_pool.append('F')
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
        bool_value = boolean(sprop, 1)
        prop = prop.replace(sprop, bool_value, 1)
        valid_flag = True

    # type II
    elif cp - op == 4 and (prop[op + 1]).isalpha() and (prop[op + 2] in con) and (prop[op + 3]).isalpha():
        sprop = '(' + prop[op + 1] + prop[op + 2] + prop[op + 3] + ')'
        bool_value = boolean(sprop, 2)
        prop = prop.replace(sprop, bool_value, 1)
        valid_flag = True

    if valid_flag:
        analyze(prop)

def GenerateBool(nr):
    l = []
    spots = 2**nr
    put_true = True
    halfing = spots/2
    ctr = 0

    for i in range(0, nr):
        for x in range(0, spots):
            if ctr < halfing and put_true == True:
                l.append('T')
                ctr += 1
            elif ctr < halfing and put_true == False:
                l.append('F')
                ctr += 1
            else:
                put_true = not put_true
                if put_true:
                    l.append('T')
                if not put_true:
                    l.append('F')
                ctr = 1

        halfing //= 2

    return l

# Start
prop = input("Input a proposition: ")
nr = int(input("Number of unique atoms: "))
possible_bool = GenerateBool(nr)
answer_pool = []

for i in range(0, 2 ** nr):
    prop_replaced = booleanReplace(prop, i, nr)
    analyze(prop_replaced)

if len(answer_pool) > 0:
    print(answer_pool)

    true = 0
    false = 0

    for x in answer_pool:
        if x == 'T':
            true += 1
        else:
            false += 1

    if true > 0 and false == 0:
        print('valid ')
    if true > 0 and false > 0:
        print('satisfiable,invalid ')
    if true == 0 and false > 0:
        print('unsatisfiable ')
else:
    print("Error flag checked.Proposition fails the test.Not a WFF.")
