class TupleSpace:
    def __init__(self):
        self.tuples = {}

        #{
        #     capteur_CH4 : {
        #         niveau_CH4 : (string, ""), 
        #         valeur_ch4 : float
        #     },
        #     capteur_H2O : {
        #         niveau_H2O : string
        #         valeur_h20 : float
        #     },
        # }
    
    def __str__(self):
        return str(self.tuples)
        # res = ""
        # for i in range(len(self.tuplesTypes)):
        #     res += self.tuplesTypes[i] + " " + str(self.tuples[self.tuplesTypes[i]]) + "\n"
        # return res
    
    def inp(self, tupleName, valueName):
        print("coucou")


    def rd(self, tupleName):
        return self.tuples[tupleName]
    
    def out(self, tupleName, valueName, value):
        # if tuple[0] in self.tuples.keys:
        #     self.tuples[tuple[0]] = tuple[1]
        # else:
        #     self.tuplesTypes.append(tupleType)
        #     self.tuples[tuple[0]] = tuple[1]
        if tupleName in self.tuples:
            self.tuples[tupleName][valueName] = value
        else:
            self.tuples[tupleName] = {valueName: value}
                




if __name__ == "__main__":
    ts = TupleSpace()
    # ts.tuplesTypes = ["a", "b", "c"]
    # ts.tuples = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    # tuplesFinal = [tuplesTypes[0] : tuples[0], tuplesTypes[1] : tuples[1], tuplesTypes[2] : tuples[2]]
    ts.out("String", ("niveau_H2O",))
    print(ts)
    