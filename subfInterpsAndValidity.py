# WFF interp of all subformulas

from lcsHelperFunc import Analyze, GenerateBool, Validity, GetAnswerPool, ResetAnswerPool

print('Does not check for WFF.Ensure that yourself.')
prop = input('Input a proposition: ')

l = []
aquired = set()
atoms = []
D = {}
char_spaging = []
values = []

# extract block
# extract indexes of all start '(' and end ')' in list l
op = -2
cp = -2
index = 0
while op != 0 and cp != len(prop) - 1:

    for i in range(0, len(prop)):

        if (prop[i]).upper() >= 'A' and (prop[i]).upper() <= 'Z' and (prop[i] not in aquired):
            atoms.append([i])
            aquired.add(prop[i])

        if prop[i] == '(' and (i not in aquired):
            op = i
            index = i
    aquired.add(index)

    for i in range(0, len(prop)):
        if prop[i] == ')' and i > index and (i not in aquired):
            cp = i
            index = i
            break
    aquired.add(index)

    l.append([op, cp])

# values block table
# Generate all possible combinations of N atoms
# Generate a 2 dimensional list values[nr_props][2*nr_atoms] = T/F
nr = len(atoms)
possible_bool = GenerateBool(nr)

for i in range(0, nr):
    x = []
    for j in range(0, 2**nr):
        x.append(possible_bool[j + (2 ** nr) * i])
    values.append(x)

# Construct the sub-formulas from the indexes in list l,put them in props_list,also print them in a row
props_list = []

i = 0
for a in atoms:
    l.insert(i, a)
    i += 1

for x in l:
    p = ''
    if len(x) == 1:
        print(prop[int(x[0])], end='    ')
        pass
    else:
        for i in range(x[0], x[1]+1):
            print(prop[i], end='')
            p += prop[i]
        print(end='    ')
    props_list.append(p)
print()
print()

# Assign each atom an ID thru dictionary going from 0 to (No of atoms)-1
s = 0
for a in atoms:
    D[prop[a[0]]] = s
    s += 1

# Foreach sub-formula 'props' in 'props_list,calculate it's value under 2**(No atoms) interpretations
# by replacing each atom in the 'the prop' with it's value from values,row 'ID value',column 'i-th' interpretation
# Analyze the prop,retrive 'answer_pool' and append it as new row in 'values',reset 'answer_pool'
for props in props_list:
    the_prop = props
    if len(props) > 1:
        for i in range(0, 2**nr):
            for c in the_prop:
                if c >= 'A' and c <= 'Z':
                    the_prop = the_prop.replace(c, values[D[c]][i], 1)
            Analyze(the_prop)
            the_prop = props
        answer_pool = GetAnswerPool()
        values.append(answer_pool.copy())
        ResetAnswerPool()

# Print all values in 'values' as a table
for x in range(0, 2 ** nr):
    for y in range(0, len(props_list)):
        print(values[y][x], end='    ')
        print(' ' * len(props_list[y]), end='')
    print(x+1, end='  ')
    print()

# Check for validity using the last column
Validity(values[-1], 'default')
