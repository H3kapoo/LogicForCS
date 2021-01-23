# CONVERTS A RELAXED/STRONG FORM PROPOSITION TO NNF
from relaxedToStrong import Transform

def Extract(source, st, en):
    lis = []
    for i in range(st, en + 1):
        lis.append(source[i])
    return lis

def ReplaceWith(source, st, en, wit):
    for i in range(en, st - 1, -1):
        source.pop(i)
    source.insert(st, wit)

def Push(prop, ind, sub_prop):
    prop.pop(ind)
    for i in range(0, len(sub_prop)):
        prop.insert(ind + i, sub_prop[i])

def ResolveDictNeg(dict_):

    for keys in range(len(dict_)-1, -1, -1):
        # for keys in dict_:
        if len(dict_[keys]) > 1:
            if dict_[keys][1] == '!':
                d = int(dict_[keys][2])
                Push(dict_[keys], 2, dict_[d])

    for keys in dict_:  # [:-1] ?
        if len(dict_[keys]) > 4:
            if dict_[keys][2] == '(':
                if dict_[keys][3] == '!':
                    dummy = dict_[keys][4]
                    dict_[keys].clear()
                    dict_[keys].append(dummy)
                    # (!(!Q)) -> Q
                elif str(dict_[keys][3]).isnumeric() and str(dict_[keys][5]).isnumeric():
                    if dict_[keys][4] == '^':
                        p = dict_[keys][3]
                        q = dict_[keys][5]
                        dict_[keys].clear()
                        dict_[keys].append('(')
                        dict_[keys].append('(')
                        dict_[keys].append('!')
                        dict_[keys].append(p)
                        dict_[keys].append(')')
                        dict_[keys].append('|')
                        dict_[keys].append('(')
                        dict_[keys].append('!')
                        dict_[keys].append(q)
                        dict_[keys].append(')')
                        dict_[keys].append(')')
                    if dict_[keys][4] == '|':
                        p = dict_[keys][3]
                        q = dict_[keys][5]
                        dict_[keys].clear()
                        dict_[keys].append('(')
                        dict_[keys].append('(')
                        dict_[keys].append('!')
                        dict_[keys].append(p)
                        dict_[keys].append(')')
                        dict_[keys].append('^')
                        dict_[keys].append('(')
                        dict_[keys].append('!')
                        dict_[keys].append(q)
                        dict_[keys].append(')')
                        dict_[keys].append(')')

def ResolveDictEqu(dict_):
    for keys in range(len(dict_)-1, -1, -1):
        if len(dict_[keys]) == 5:
            if dict_[keys][2] == '-':
                p = int(dict_[keys][1])
                q = int(dict_[keys][3])
                dict_[keys].clear()
                dict_[keys].append('(')
                dict_[keys].append('(')
                dict_[keys].append(p)
                dict_[keys].append('>')
                dict_[keys].append(q)
                dict_[keys].append(')')
                dict_[keys].append('^')
                dict_[keys].append('(')
                dict_[keys].append(q)
                dict_[keys].append('>')
                dict_[keys].append(p)
                dict_[keys].append(')')
                dict_[keys].append(')')

def ResolveDictImp(dict_):
    for keys in range(len(dict_)-1, -1, -1):
        if len(dict_[keys]) == 5:
            if dict_[keys][2] == '>':
                p = int(dict_[keys][1])
                q = int(dict_[keys][3])
                dict_[keys].clear()
                dict_[keys].append('(')
                dict_[keys].append('(')
                dict_[keys].append('!')
                dict_[keys].append(p)
                dict_[keys].append(')')
                dict_[keys].append('|')
                dict_[keys].append(q)
                dict_[keys].append(')')

def GetDict(prop):
    prop_list = []
    Dict = {}
    for el in prop:
        prop_list.append(el)

    atoms_set = set()

    for el in prop_list:
        if (el).isalpha():
            atoms_set.add(el)
    atoms_no = len(atoms_set)

    atoms_set = list(atoms_set)

    for i in range(0, atoms_no):
        Dict[i] = atoms_set[i]

    for i in range(0, atoms_no):
        for j in range(0, len(prop_list)):
            if atoms_set[i] == prop_list[j]:
                prop_list[j] = i

    atoms_no_copy = atoms_no
    atoms_no_copy += 0  # was 1
    op = 0
    cp = 0
    while len(prop_list) != 1:
        for i in range(0, len(prop_list)):
            if prop_list[i] == '(':
                op = i
        for i in range(0, len(prop_list)):
            if prop_list[i] == ')' and i > op:
                cp = i
                break
        extracted = Extract(prop_list, op, cp)
        ReplaceWith(prop_list, op, cp, atoms_no_copy)
        Dict[atoms_no_copy] = extracted
        atoms_no_copy += 1

    return (Dict, atoms_no_copy-1, atoms_no)

def Assemble(dict_, elem_no, atoms_no, type_):
    if type_ == 'neg':
        ResolveDictNeg(dict_)
    if type_ == 'equ':
        ResolveDictEqu(dict_)
    if type_ == 'imp':
        ResolveDictImp(dict_)

    final = dict_[elem_no]
    elem_no -= 1
    while elem_no != -1:  # -1
        for i in range(0, len(final)):
            if str(final[i]) == str(elem_no):
                final[i] = dict_[elem_no]
                Push(final, i, dict_[elem_no])
                break

        found = False
        for i in range(0, len(final)):
            if final[i] == elem_no:
                found = True
                break
        if not found:
            elem_no -= 1

    return final

def hasToPushNeg(final):
    for i in range(0, len(final) - 1):
        if final[i] == '!' and final[i + 1] == '(':
            return True
    return False

def hasToPushImp(final):
    for i in range(0, len(final) - 1):
        if final[i] == '>':
            return True
    return False

def hasToPushEqu(final):
    for i in range(0, len(final) - 1):
        if final[i] == '-':
            return True
    return False

def ToString(final):
    string = ''
    for el in final:
        string += str(el)
    return string

# STRAT HERE
def toNNF(Final):
    Final = Transform(Final)

    while hasToPushEqu(Final):
        Dict = GetDict(Final)
        Final = Assemble(Dict[0], Dict[1], Dict[2], 'equ')
        Final = ToString(Final)

    while hasToPushImp(Final):
        Dict = GetDict(Final)
        Final = Assemble(Dict[0], Dict[1], Dict[2], 'imp')
        Final = ToString(Final)

    while hasToPushNeg(Final):
        Dict = GetDict(Final)
        Final = Assemble(Dict[0], Dict[1], Dict[2], 'neg')
        Final = ToString(Final)

    print('Proposition in NNF:', Final)
    return Final

if __name__ == "__main__":
     prop = input('Input a proposition to convert to NNF: ')
     toNNF(prop)
