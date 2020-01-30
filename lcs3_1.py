
# WFF all interp. table view

from lcs_helper import neg, and_, or_, imp, equ, Prompt
from lcs_helper import BooleanType, GenerateBool, Analyze, BooleanReplace, Validity, GetAnswerPool

# Start
Prompt()
prop = input('Input a proposition: ')
atoms = int(input('Number of unique atoms: '))

possible_bool = GenerateBool(atoms)

for i in range(0, 2 ** atoms):
    prop_replaced = BooleanReplace(prop, i, atoms, possible_bool)
    Analyze(prop_replaced)

answer_pool = GetAnswerPool()
Validity(answer_pool, 'pretty')
