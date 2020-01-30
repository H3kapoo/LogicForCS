# CONVERTS A RELAXED FORMULA INTO A STRONG FORM FORMULA
# DEPENDS ON: rel_helper.py

from rel_helper import GetListForm, GetAtomsFromList, GetSubPropNumberID, ReplaceAtoms
from rel_helper import StillHasTwoParanthesis, GetParanthesisLoc, MakeSubPropFrom, SubstractSubProp
from rel_helper import PropIsFinished, CheckForNegation, CheckForAndOr, CheckForImplication, CheckForEquivalence
from rel_helper import BreakListResolveChain, ContainsAtoms, PrintChain, FinalReplace


def Transform(Prop):
    PropListForm = GetListForm(Prop)

    SubProps = GetAtomsFromList(PropListForm)

    NumberOfAtoms = len(SubProps)

    BreakListIDs = []

    SubPropNumberID = GetSubPropNumberID(SubProps)

    PropListForm = ReplaceAtoms(PropListForm, SubProps)

    while StillHasTwoParanthesis(PropListForm) == 'Pass':
        ParanthesisLoc = GetParanthesisLoc(PropListForm)

        SubProps.append(MakeSubPropFrom(
            PropListForm, ParanthesisLoc[0], ParanthesisLoc[1]))

        PropListForm = SubstractSubProp(
            PropListForm, ParanthesisLoc[0], ParanthesisLoc[1])

        PropListForm.insert(ParanthesisLoc[0], SubPropNumberID)

        if ContainsAtoms(SubProps[SubPropNumberID], NumberOfAtoms) == 'ContainsAtoms':
            BreakListIDs.append(SubPropNumberID)

        SubPropNumberID += 1

    while PropIsFinished(PropListForm) == 'NotFinished':
        # returns a flag and a list of indexes as response as list
        while CheckForNegation(PropListForm)[0] == 'Found':
            SubProps.append(CheckForNegation(PropListForm)[1])
            SubLoc = CheckForNegation(PropListForm)[2]
            PropListForm = SubstractSubProp(PropListForm, SubLoc[0], SubLoc[1])
            PropListForm.insert(SubLoc[0], SubPropNumberID)

            if ContainsAtoms(SubProps[SubPropNumberID], NumberOfAtoms) == 'ContainsAtoms':
                BreakListIDs.append(SubPropNumberID)

            SubPropNumberID += 1
            # print(PropListForm)

        while CheckForAndOr(PropListForm)[0] == 'Found':
            SubProps.append(CheckForAndOr(PropListForm)[1])
            SubLoc = CheckForAndOr(PropListForm)[2]
            PropListForm = SubstractSubProp(PropListForm, SubLoc[0], SubLoc[1])
            PropListForm.insert(SubLoc[0], SubPropNumberID)

            if ContainsAtoms(SubProps[SubPropNumberID], NumberOfAtoms) == 'ContainsAtoms':
                BreakListIDs.append(SubPropNumberID)

            SubPropNumberID += 1
            # print(PropListForm)

        while CheckForImplication(PropListForm)[0] == 'Found':
            SubProps.append(CheckForImplication(PropListForm)[1])
            SubLoc = CheckForImplication(PropListForm)[2]
            PropListForm = SubstractSubProp(PropListForm, SubLoc[0], SubLoc[1])
            PropListForm.insert(SubLoc[0], SubPropNumberID)

            if ContainsAtoms(SubProps[SubPropNumberID], NumberOfAtoms) == 'ContainsAtoms':
                BreakListIDs.append(SubPropNumberID)

            SubPropNumberID += 1
            # print(PropListForm)

        while CheckForEquivalence(PropListForm)[0] == 'Found':
            SubProps.append(CheckForEquivalence(PropListForm)[1])
            SubLoc = CheckForEquivalence(PropListForm)[2]
            PropListForm = SubstractSubProp(PropListForm, SubLoc[0], SubLoc[1])
            PropListForm.insert(SubLoc[0], SubPropNumberID)

            if ContainsAtoms(SubProps[SubPropNumberID], NumberOfAtoms) == 'ContainsAtoms':
                BreakListIDs.append(SubPropNumberID)

            SubPropNumberID += 1
            # print(PropListForm)

    SubProps.append(SubPropNumberID)
    SubPropNumberID += 1

    BreakListResolveChain(BreakListIDs, SubProps,
                          NumberOfAtoms, SubPropNumberID)

    Result = FinalReplace(SubProps[SubPropNumberID-2], SubProps)

    return PrintChain(Result)


if __name__ == "__main__":
    inp = input('Enter a WFF in relaxed form: ')
    Transform(inp)
