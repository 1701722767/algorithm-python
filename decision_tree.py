# Tratamiento de datos
# ------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Gráficos
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# Preprocesado y modelado
# ------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.tree import export_graphviz
from sklearn.tree import export_text
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Configuración warnings
# ------------------------------------------------------------------------------
import warnings
warnings.filterwarnings('once')

from cmd import Cmd

class DecisionTree:
    # For axample
    # classes1 = ["NORMAL","CANCER"]
    # classesValues1 = ["NORMAL","CANCER"]
    # attributes1 = ["ANTENAS","COLAS","NUCLEOS","CUERPO"]
    # rows1 = [
    #     ['NORMAL', 1.0, 0.0, 2.0, 1],#rayado3
    #     ['CANCER', 1.0, 0.0, 1.0, 0],
    #     ['NORMAL', 1.0, 2.0, 0.0, 1],
    #     ['NORMAL', 0.0, 2.0, 1.0, 1],
    #     ['CANCER', 1.0, 1.0, 1.0, 1],
    #     ['CANCER', 2.0, 2.0, 1.0, 1],
    # ]

    classes = []
    classesValues = []
    rows = []
    attributes = []

    def getData(self):
        self.classes = []
        self.classesValues = []
        self.rows = []
        self.attributes = []

        self.classes = [Cmd.GetString("Clase 1: ").upper(),Cmd.GetString("Clase 2: ").upper()]
        self.classesValues = [Cmd.GetString("Valor clase 1: ").upper(),Cmd.GetString("Valor clase 2: ").upper()]

        while True:
            res = Cmd.GetString("Desea crear un nuevo atributo? (Y/N) ").upper()
            if res == "N":
                break

            attribute = Cmd.GetString("Nombre atributo: \n").upper()
            self.attributes.append(attribute)


        while True:
            res = Cmd.GetString("Desea agregar una nueva fila? (Y/N) ").upper()
            if res == "N":
                break

            classRow = Cmd.GetString("clase: \n").upper()
            row = [classRow]

            for attribute in self.attributes:
                row.append(Cmd.GetNumber("valor para el attributo "+ attribute +": \n"))

            self.rows.append(row)


    def run(self):
        datos = pd.DataFrame(self.rows, columns = ["CLASS"] + self.attributes)
        datos['CLASS_NUM'] = np.where(datos.CLASS == self.classes[0], 0, 1)
        datos = datos.drop(columns = 'CLASS')

        # División de los datos en train y test
        # ------------------------------------------------------------------------------
        X_train, X_test, y_train, y_test = train_test_split(
                                                datos.drop(columns = 'CLASS_NUM'),
                                                datos['CLASS_NUM'],
                                            )

        # One-hot-encoding de las variables categóricas
        # ------------------------------------------------------------------------------
        # Se identifica el nombre de las columnas numéricas y categóricas
        cat_cols = X_train.select_dtypes(include=['object', 'category']).columns.to_list()
        numeric_cols = X_train.select_dtypes(include=['float64', 'int']).columns.to_list()

        # Se aplica one-hot-encoding solo a las columnas categóricas
        preprocessor = ColumnTransformer(
                            [('onehot', OneHotEncoder(handle_unknown='ignore'), cat_cols)],
                            remainder='passthrough'
                    )

        # Una vez que se ha definido el objeto ColumnTransformer, con el método fit()
        # se aprenden las transformaciones con los datos de entrenamiento y se aplican a
        # los dos conjuntos con transform(). Ambas operaciones a la vez con fit_transform().
        X_train_prep = preprocessor.fit_transform(X_train)
        X_test_prep  = preprocessor.transform(X_test)


        # Convertir el output del ColumnTransformer en dataframe y añadir el nombre de las columnas
        # ------------------------------------------------------------------------------
        # Nombre de todas las columnas
        encoded_cat = []
        if len(cat_cols) > 0:
            encoded_cat = preprocessor.named_transformers_['onehot'].get_feature_names(cat_cols)

        labels = np.concatenate([numeric_cols, encoded_cat])

        # Conversión a dataframe
        X_train_prep = pd.DataFrame(X_train_prep, columns=labels)
        X_test_prep  = pd.DataFrame(X_test_prep, columns=labels)
        X_train_prep.info()


        # Creación del modelo
        # ------------------------------------------------------------------------------
        modelo = DecisionTreeClassifier(
                    max_depth         = 5,
                    criterion         = 'gini'
                )

        # Entrenamiento del modelo
        # ------------------------------------------------------------------------------
        modelo.fit(X_train_prep, y_train)

        # Estructura del árbol creado
        # ------------------------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(13, 6))

        plot = plot_tree(
                    decision_tree = modelo,
                    feature_names = labels.tolist(),
                    class_names   = self.classes,
                    filled        = True,
                    impurity      = False,
                    fontsize      = 12,
                    ax            = ax
            )

        plt.title("Decision tree")
        plt.show()

