# WFF under a specific interpretation

from lcsHelperFunc import neg, and_, or_, imp, equ, booleanReplace, booleanFunction, AnalyzeBoolSingleShot

# Start
prop = input("Input a proposition: ")
prop = booleanReplace(prop)
AnalyzeBoolSingleShot(prop)
