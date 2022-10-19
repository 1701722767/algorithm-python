

from cmd import Cmd

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

class Kmeans:

    
    variables=0
    dataNumbers=0
    values={}
    clusters=0




    def getData(self):
        self.clusters= Cmd.GetNumber("enter the number of clusters: ",1,100)
        self.variables = Cmd.GetNumber("enter the number of variables: ",1,100)
        self.dataNumbers = Cmd.GetNumber("enter the amount of data: ",1,100)

        for i in range(int(self.variables)):
            name=Cmd.GetString("enter the name of variables "+ str(i+1) + ": ")
            datas=[]
            for j in range(int(self.dataNumbers)):
                datas.append(Cmd.GetNumber("enter the data: ",1,100))
            self.values[name]=datas

        self.values=pd.DataFrame(self.values)



    
    def run(self):

        kmeans = KMeans(n_clusters=int(self.clusters)).fit(self.values.values)
        self.values["cluster"] = kmeans.labels_
        print(self.values)
