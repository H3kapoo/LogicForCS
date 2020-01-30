
# CLAUSE SET SOLVER (VERY SLOW IF SATISF)


class Clause:
    def __init__(self, id_, form, createdBy):
        self.id_ = id_
        self.form = []
        self.createdBy = createdBy
        self.form.append(form)

    def GetForm(self):
        return self.form[0]

    def GetID(self):
        return self.id_

    def GetHasNeg(self):
        return self.form[0]

    def GetCreator(self):
        return self.createdBy


class ClauseSet:
    def __init__(self, clausesNo):
        self.clauseNo = clausesNo
        self.id_ = 0
        self.clauses = []
        self.resolved = [(-1, -1)]
        self.FOUND = False

    def SetClauses(self):
        for i in range(0, self.clauseNo):
            form = input("Clause: ")
            tupl = 'ROOT'
            self.clauses.append(Clause(self.id_, form.split(','), tupl))
            self.id_ += 1

    def SolveClause_Opposite(self, a, b):
        if len(a) == len(b):
            return False
        if len(a) == 1 and len(b) == 2:
            if a[0] == b[1]:
                return True
        if len(a) == 2 and len(b) == 1:
            if b[0] == a[1]:
                return True
        return False

    def SolveClause_PushUsed(self, x, u):
        if len(x) == 1:
            u.append(x)
            u.append('!' + x)
        if len(x) == 2:
            u.append(x)
            u.append(x[1])

    def SolveClause_Contains(self, frm):
        for cl in self.clauses:
            x = cl.GetForm()
            if x == frm:
                return True
        return False

    def SolveClause(self, C1_, C2_):
        used = []
        id1 = C1_.GetID()
        id2 = C2_.GetID()
        C1__ = C1_.GetForm()
        C2__ = C2_.GetForm()
        C1 = set()
        C2 = set()
        for e in C1__:
            C1.add(e)
        for e in C2__:
            C2.add(e)

        for e in C1:
            if e not in used:
                for f in C2:
                    if self.SolveClause_Opposite(e, f):
                        self.SolveClause_PushUsed(e, used)
                        C1.remove(e)
                        C2.remove(f)
                        form = [list(C1.union(C2))][0]
                        if len(form) == 0:
                            self.FOUND = True
                            print('UNSAT')
                        if not self.SolveClause_Contains(form):
                            self.clauses.append(
                                Clause(self.id_, form, (id1, id2)))
                            # print(len(c.clauses))
                            self.id_ += 1
                        C1.add(e)
                        C2.add(f)

    def PrintClauses(self):
        for c in self.clauses:
            print(c.GetForm(), " ", c.GetID(), "   ", c.GetCreator())


c = ClauseSet(int(input("Number of clauses: ")))
c.SetClauses()
length = len(c.clauses)

while not c.FOUND:

    for i in range(0, length):
        for j in range(i, length):
            if i != j:
                if (i, j) not in c.resolved:
                    c.SolveClause(c.clauses[i], c.clauses[j])
                    c.resolved.append((i, j))
                    c.resolved.append((j, i))
                    # print(length)

    length = len(c.clauses)

print()

c.PrintClauses()
