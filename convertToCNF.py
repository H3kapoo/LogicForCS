# CONVERTS FROM NNF TO CNF
from convertToNNF import toNNF,GetDict,Assemble,ToString

def CanPushFormula(Dict_):
    ctr = False

    for keys in range(len(Dict_) - 1, -1, -1):
        if len(Dict_[keys]) == 5:
            if Dict_[keys][2] == '|':
                beenFiled = False
                left = Dict_[keys][1]
                if len(Dict_[left]) == 5:
                    if Dict_[left][2] == '^':
                        beenFiled == True
                        ctr = True
                        p = Dict_[keys][3]
                        q = Dict_[left][1]
                        r = Dict_[left][3]
                        if True:
                            Dict_[keys].clear()
                            Dict_[keys].append('(')
                            Dict_[keys].append('(')
                            Dict_[keys].append(p)
                            Dict_[keys].append('|')
                            Dict_[keys].append(r)
                            Dict_[keys].append(')')
                            Dict_[keys].append('^')
                            Dict_[keys].append('(')
                            Dict_[keys].append(p)
                            Dict_[keys].append('|')
                            Dict_[keys].append(q)
                            Dict_[keys].append(')')
                            Dict_[keys].append(')')

            if Dict_[keys][2] == '|':
                right = Dict_[keys][3]

                if len(Dict_[right]) == 5:
                    if Dict_[right][2] == '^':
                        ctr = True
                        p = Dict_[keys][1]
                        q = Dict_[right][1]
                        r = Dict_[right][3]
                        if True:
                            Dict_[keys].clear()
                            Dict_[keys].append('(')
                            Dict_[keys].append('(')
                            Dict_[keys].append(p)
                            Dict_[keys].append('|')
                            Dict_[keys].append(q)
                            Dict_[keys].append(')')
                            Dict_[keys].append('^')
                            Dict_[keys].append('(')
                            Dict_[keys].append(p)
                            Dict_[keys].append('|')
                            Dict_[keys].append(r)
                            Dict_[keys].append(')')
                            Dict_[keys].append(')')

    return ctr

inp = input('Input proposition to convert to CNF: ')
CNF = toNNF(inp)

Dict = GetDict(CNF)

while CanPushFormula(Dict[0]):
    Final = Assemble(Dict[0], Dict[1], Dict[2], 'none')
    CNF = ToString(Final)
    Dict = GetDict(CNF)

print('Proposition in CNF:', CNF)
