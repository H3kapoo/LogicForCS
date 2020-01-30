
# WFF under a specific interpretation

from lcs_helper import Prompt, neg, and_, or_, imp, equ, booleanReplace, booleanFunction, AnalyzeBoolSingleShot

# Start
Prompt()
prop = input("Input a proposition: ")
prop = booleanReplace(prop)
AnalyzeBoolSingleShot(prop)
