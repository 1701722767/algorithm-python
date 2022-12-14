import sys
from apriori import Apriori
from kmenas import Kmeans
from randomForest import RandomForest
from pca import Pca
from knn import Knn
from cmd import Cmd
from decision_tree import DecisionTree



algorithms = [
    {
        "label": "Apriori",
        "performer": Apriori(),
    },
    {
        "label": "Kmeans",
        "performer": Kmeans(),
    },
    {
        "label": "Random Forest",
        "performer": RandomForest(),
    },
    {
        "label": "Pca",
        "performer": Pca(),
    },

    {
        "label": "Knn",
        "performer": Knn(),
    },
    {
        "label": "Decision Tree",
        "performer": DecisionTree(),
    },
]

def cmd():
    print("Select a algorithm: \n")
    countAlgorithms = len(algorithms)
    for i in range(countAlgorithms):
        print(str(i + 1)+". "+algorithms[i]["label"])

    print(str(countAlgorithms + 1)+". Exit")
    selected = Cmd.GetNumber("\nEnter a number of algorithm: ",1,countAlgorithms + 1)
    if selected == countAlgorithms + 1:
        return

    algorithmPerformer = algorithms[int(selected-1)]["performer"]

    algorithmPerformer.getData()
    algorithmPerformer.run()

    cmd()


def gui():
    print("not implemented")

def main():
    args = sys.argv[1:]

    mode = "cmd"
    if len(args) > 0 :
        mode = args[0]

    if mode == "cmd":
        return cmd()

    if mode == "gui":
        return gui()

    print("mode invalid: ",mode)

main()



