#HELPER CLASS FOR RELAXED -> STRONG FORM

def GetListForm(Prop):
    ListOfElements = []
    for Element in Prop:
        ListOfElements.append(Element)
    return ListOfElements


def GetAtomsFromList(Prop):
    UniqueAtoms = set()
    for Atom in Prop:
        if (Atom).isalpha():
            UniqueAtoms.add(Atom)
    return list(UniqueAtoms)


def GetSubPropNumberID(SubProps):
    return len(SubProps)


def ReplaceAtoms(Prop, Atoms):
    IDs = {}
    AtomsLength = len(Atoms)
    PropLength = len(Prop)
    for i in range(0, AtomsLength):
        IDs[Atoms[i]] = i
    for i in range(0, PropLength):
        if (Prop[i]).isalpha():
            Prop[i] = IDs[Prop[i]]
    return Prop


def StillHasTwoParanthesis(Prop):
    NoOfParanthesisL = 0
    NoOfParanthesisR = 0
    for Element in Prop:
        if Element == ')':
            NoOfParanthesisR += 1
        if Element == '(':
            NoOfParanthesisL += 1
    if NoOfParanthesisL == 0 and NoOfParanthesisR == 0:
        return 'NextPhase'
    if NoOfParanthesisL != NoOfParanthesisR:
        print("Proposition can't be relaxed,paranthesis missing maybe.")
        exit(0)  # Should Quit App
    if NoOfParanthesisL == NoOfParanthesisR:
        return 'Pass'


def GetParanthesisLoc(Prop):
    OpenParanthesis = -1
    ClosParanthesis = -1
    PropLength = len(Prop)
    for i in range(0, PropLength):
        if Prop[i] == '(':
            OpenParanthesis = i
    for i in range(0, PropLength):
        if Prop[i] == ')' and i > OpenParanthesis:
            ClosParanthesis = i
            break
    return [OpenParanthesis, ClosParanthesis]


def MakeSubPropFrom(Prop, From, To):
    SubProp = []
    Range = To - From
    for i in range(From, To+1):
        SubProp.append(Prop[i])
    return SubProp


def SubstractSubProp(Prop, From, To):
    PropCopy = Prop.copy()
    for i in range(To, From-1, -1):
        PropCopy.pop(i)
    return PropCopy


def PropIsFinished(Prop):
    if (str(Prop[0])).isnumeric() and len(Prop) == 1:
        return 'Finished'
    if Prop[0] == '(' and (str(Prop[1])).isnumeric() and Prop[2] == ')':
        return 'Finished'
    return 'NotFinished'


def CheckForNegation(Prop):
    Found = 'NotFound'
    IndexStart = 0
    SubProp = []
    PropLength = len(Prop)

    for i in range(PropLength - 1, -1, -1):  # Make it in reverse,Right Associative
        if Prop[i] == '!' and (str(Prop[i+1])).isnumeric():
            Found = 'Found'
            IndexStart = i
            SubProp.append('(')
            SubProp.append(Prop[IndexStart])
            SubProp.append(Prop[IndexStart + 1])
            SubProp.append(')')
            break
    return [Found, SubProp, [IndexStart, IndexStart+1]]


def CheckForAndOr(Prop):
    Found = 'NotFound'
    IndexStart = 0
    SubProp = []
    PropLength = len(Prop)

    for i in range(PropLength - 1, -1, -1):
        if Prop[i] == '^' or Prop[i] == '|':
            Found = 'Found'
            IndexStart = i
            SubProp.append('(')
            SubProp.append(Prop[IndexStart - 1])
            SubProp.append(Prop[IndexStart])
            SubProp.append(Prop[IndexStart + 1])
            SubProp.append(')')
            break
    return [Found, SubProp, [IndexStart-1, IndexStart+1]]


def CheckForImplication(Prop):
    Found = 'NotFound'
    IndexStart = 0
    SubProp = []
    PropLength = len(Prop)

    for i in range(PropLength - 1, -1, -1):
        if Prop[i] == '>':
            Found = 'Found'
            IndexStart = i
            SubProp.append('(')
            SubProp.append(Prop[IndexStart - 1])
            SubProp.append(Prop[IndexStart])
            SubProp.append(Prop[IndexStart + 1])
            SubProp.append(')')
            break
    return [Found, SubProp, [IndexStart-1, IndexStart+1]]


def CheckForEquivalence(Prop):
    Found = 'NotFound'
    IndexStart = 0
    SubProp = []
    PropLength = len(Prop)

    for i in range(PropLength - 1, -1, -1):
        if Prop[i] == '-':
            Found = 'Found'
            IndexStart = i
            SubProp.append('(')
            SubProp.append(Prop[IndexStart - 1])
            SubProp.append(Prop[IndexStart])
            SubProp.append(Prop[IndexStart + 1])
            SubProp.append(')')
            break
    return [Found, SubProp, [IndexStart-1, IndexStart+1]]


def GetHighestAtomID(SubProp, NoOfAtoms):
    HighestID = 0
    for Element in SubProp:
        if (str(Element)).isnumeric():
            if Element > HighestID and Element < NoOfAtoms:
                HighestID = Element
    return HighestID


def FinalReplace(Final, SubProps):
    while StillHasToReplace(Final):
        i = 0

        while i < len(Final):
            if (str(Final[i])).isnumeric():
                LocCopy = Final[i]
                Final.pop(i)
                Final = ReplaceNoList(
                    Final, SubProps[LocCopy], i)
                i = 0
            else:
                i += 1
                if i == len(Final):
                    break
    return Final


def BreakListResolveChain(BreakListIDs, SubProps, NoOfAtoms, SubPropNumberID):
    SmallSubPropsID = SubPropNumberID
    for ID in BreakListIDs:
        SubProp = SubProps[ID]
        SubProp.pop(len(SubProp) - 1)
        SubProp.pop(0)
        SmallSubProps = {}
        while PropIsFinished(SubProp) == 'NotFinished':
            while CheckForNegation(SubProp)[0] == 'Found':
                SmallSubProps[SmallSubPropsID] = (CheckForNegation(SubProp)[1])
                SubLoc = CheckForNegation(SubProp)[2]
                SubProp = SubstractSubProp(SubProp, SubLoc[0], SubLoc[1])
                SubProp.insert(SubLoc[0], SmallSubPropsID)
                SmallSubPropsID += 1

            while CheckForAndOr(SubProp)[0] == 'Found':
                SmallSubProps[SmallSubPropsID] = (CheckForAndOr(SubProp)[1])
                SubLoc = CheckForAndOr(SubProp)[2]
                SubProp = SubstractSubProp(SubProp, SubLoc[0], SubLoc[1])
                SubProp.insert(SubLoc[0], SmallSubPropsID)
                SmallSubPropsID += 1

            while CheckForImplication(SubProp)[0] == 'Found':
                SmallSubProps[SmallSubPropsID] = (
                    CheckForImplication(SubProp)[1])
                SubLoc = CheckForImplication(SubProp)[2]
                SubProp = SubstractSubProp(SubProp, SubLoc[0], SubLoc[1])
                SubProp.insert(SubLoc[0], SmallSubPropsID)
                SmallSubPropsID += 1

            while CheckForEquivalence(SubProp)[0] == 'Found':
                SmallSubProps[SmallSubPropsID] = (
                    CheckForEquivalence(SubProp)[1])
                SubLoc = CheckForEquivalence(SubProp)[2]
                SubProp = SubstractSubProp(SubProp, SubLoc[0], SubLoc[1])
                SubProp.insert(SubLoc[0], SmallSubPropsID)
                SmallSubPropsID += 1
            # print('ok')
        SmallSubProps[SmallSubPropsID] = SmallSubPropsID-1
        #print('From Break: ', SmallSubProps)

        SubPr = Reconstruct(SmallSubProps, SubProps,
                            SmallSubPropsID)
        SubProps[ID] = SubPr


def StillHasToReplace(Prop):
    for Element in Prop:
        if (str(Element)).isnumeric():
            return True
    return False


def Reconstruct(SmallSubProps, SubProps, ID):
    ReconstructedProp = [SmallSubProps[ID]]
    SmallSubProps.pop(ID)
    SmallSubPropsLen = len(SmallSubProps)
    while StillHasToReplace(ReconstructedProp):
        i = 0

        while i < len(ReconstructedProp):
            if (str(ReconstructedProp[i])).isnumeric() and (ReconstructedProp[i] in SmallSubProps):
                LocCopy = ReconstructedProp[i]
                ReconstructedProp.pop(i)
                ReconstructedProp = ReplaceNoList(
                    ReconstructedProp, SmallSubProps[LocCopy], i)
                i = 0
            elif (str(ReconstructedProp[i])).isnumeric() and (ReconstructedProp[i] not in SmallSubProps):
                LocCopy = ReconstructedProp[i]
                ReconstructedProp.pop(i)
                ReconstructedProp = ReplaceNoList(
                    ReconstructedProp, SubProps[LocCopy], i)
                i = 0
            else:
                i += 1
                if i == len(ReconstructedProp):
                    break
   # print('Rec: ', ReconstructedProp)
    return ReconstructedProp


def ReplaceNoList(Prop, SubProp, i):
    SubPropLen = len(SubProp)

    for x in range(0, SubPropLen):
        Prop.insert(i + x, SubProp[x])
    return Prop


def ContainsAtoms(SubProp, NoOfAtoms):
    for Element in SubProp:
        if (str(Element)).isnumeric() and Element < NoOfAtoms:
            return 'ContainsAtoms'
    return 'NotContainsAtoms'


def PrintChain(Prop):
    Chain = ''
    for Element in Prop:
        Chain += str(Element)
    print('Strong Form: ',Chain)
    return Chain
