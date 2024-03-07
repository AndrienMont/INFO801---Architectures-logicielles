class TupleSpace:
    def __init__(self):
        self.tuples = {}
        self.tuplesTypes = []
    
    def __str__(self):
        res = ""
        for i in range(len(self.tuplesTypes)):
            res += self.tuplesTypes[i] + " " + str(self.tuples[self.tuplesTypes[i]]) + "\n"
        return res
    
    def inp(self, tupleName):
        if tupleName in self.tuplesTypes:
            del self.tuples[tupleName]
            self.tuplesTypes.remove(tupleName)


    def rd(self, tupleName):
        return self.tuples[tupleName]
    
    def out(self, tupleType, tuple):
        if tuple[0] in self.tuples.keys:
            self.tuples[tuple[0]] = tuple[1]
        else:
            self.tuplesTypes.append(tupleType)
            self.tuples[tuple[0]] = tuple[1]



if __name__ == "__main__":
    ts = TupleSpace()
    ts.tuplesTypes = ["a", "b", "c"]
    ts.tuples = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    print(ts)