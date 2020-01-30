# CHECK IF A FORMULA IT'S A WFF
# DEPENDS ON: lcs_helper.py

# neg !
# and ^
# or |
# imp >
# equ -
# valid expressions
#A - atom
# (!Q) neg
# (A^B) and
# (A|B) or
# (A>B) imp
# (A-B) equ

from random import randint as rand
from lcs_helper import AnalyzeNonBool
con = ['!', '^', '|', '-', '>']

# Start
prop = input("Input a proposition: ")
AnalyzeNonBool(prop)
