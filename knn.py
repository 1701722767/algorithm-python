import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class Knn:
    def getData(self):
        print("getting data")

    def run(self):
        print("running")

        plt.rcParams['figure.figsize'] = (16, 9)
        plt.style.use('ggplot')

        dataframe = pd.read_csv(r"data.csv",sep=';')


        Xs = dataframe[['x1']].values
        Ys = dataframe[['y1']].values

        print(Xs)
        print(Ys)

        X_train, X_test, y_train, y_test = train_test_split(Xs, Ys)
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        print('---------------------------------------------')

        print(X_train)
        print('---------------------------------------------')
        print(X_test)
        print('---------------------------------------------')
        print(y_train)
        print('---------------------------------------------')
        print(y_test)
        print('---------------------------------------------')


        n_neighbors = 2

        knnV = KNeighborsClassifier(n_neighbors=n_neighbors)
        knnV.fit(X_train,y_test)


        print(knnV.predict(Xs))
        print('Accuracy of K-NN classifier on training set')
        print(knnV.score(Xs, Ys))
        print('Accuracy of K-NN classifier on test set:')
       # print(knnV.score(X_test, y_test))





