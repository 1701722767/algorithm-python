
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from cmd import Cmd
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

class Pca:

    values={}
    dataset=None




    def getData(self):
        self.dataset = load_digits()
        self.dataset.keys()
        self.dataset.data.shape
        self.dataset.data[0]
        self.dataset.data[0].reshape(8,8)
        plt.gray()
        plt.matshow(self.dataset.data[0].reshape(8,8))
        plt.matshow(self.dataset.data[9].reshape(8,8))
        self.dataset.target[:5]
        self.values = pd.DataFrame(self.dataset.data, columns=self.dataset.feature_names)
  
    def run(self):
        X = self.values
        y = self.dataset.target


        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=30)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        model.score(X_test, y_test)

        

        pca = PCA(0.95)
        X_pca = pca.fit_transform(X)
        print("Score: "+str(X_pca.shape))
        pca.explained_variance_ratio_
        pca.n_components_
