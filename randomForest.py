

from cmd import Cmd


import pandas as pd
from random import sample
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import tree

class RandomForest:

    
    variables=0
    dataNumbers=0
    dataPredicts=[]
    values={}
    dependentVariable=""
    numberDiv=0
    numberRandom=0



    def getData(self):
        self.variables = Cmd.GetNumber("enter the number of variables: ",1,100)
        self.dataNumbers = Cmd.GetNumber("enter the amount of data: ",1,100)

        for i in range(int(self.variables)):
            name=Cmd.GetString("enter the name of variables "+ str(i+1) + ": ")
            datas=[]
            for j in range(int(self.dataNumbers)):
                datas.append(Cmd.GetNumber("enter the data: ",0,100))
            self.values[name]=datas
            self.dependentVariable=name


        print("Enter variables predict")
        for i in range(int(self.variables-1)):
            self.dataPredicts.append(Cmd.GetNumber("enter the data: ",0,100))

        self.numberRandom=Cmd.GetNumber("insert number random: ",0,100)

        self.values=pd.DataFrame(self.values)        

    
    def run(self):
        print(self.values.columns[:-1], "\n")
        print(sample(set(self.values.columns[:-1]), int(self.numberRandom   )))

        bosque = RandomForestClassifier(n_estimators=100,
                               criterion="gini",
                               max_features="sqrt",
                               bootstrap=True,
                               max_samples=2/3,
                               oob_score=True)

        bosque.fit(self.values[self.values.columns[:-1]].values, self.values[self.dependentVariable].values)

        print(bosque.predict([[50, 16, 1]]))
        print(bosque.score(self.values[self.values.columns[:-1]].values, self.values[self.dependentVariable].values))
        print(bosque.oob_score_)
        for arbol in bosque.estimators_:
            tree.plot_tree(arbol, feature_names=self.values.columns[:-1])
            plt.show()
