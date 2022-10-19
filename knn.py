from math import sqrt
from cmd import Cmd


class Knn:
    # For example
    # dataset = [
    # [10,"niño"],
    # [12,"niño"],
    # [13,"niño"],[55,"adulto"],
    # [66,"adulto"],
    # [2,"bebe"],
    # [1,"bebe"],
    # [22,"joven"],
    # [24,"joven"],
    # [18,"joven"],
    # [40,"adulto"]]
    # test = [13]
    # vecinos = 2

    dataset = []
    test = []
    vecinos = 3

    # calculate the Euclidean distance between two vectors
    def euclidean_distance(self,row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (float(row1[i]) - float(row2[i]))**2
        return sqrt(distance)

    # Locate the most similar neighbors
    def get_neighbors(self,train, test_row, num_neighbors):
        distances = list()
        for train_row in train:
            dist = self.euclidean_distance(test_row, train_row)
            distances.append((train_row, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = list()
        for i in range(num_neighbors):
            neighbors.append(distances[i][0])
        return neighbors

    # Make a classification prediction with neighbors
    def predict_classification(self,train, test_row, num_neighbors):
        neighbors = self.get_neighbors(train, test_row, num_neighbors)
        output_values = [row[-1] for row in neighbors]
        prediction = max(set(output_values), key=output_values.count)
        return prediction

    def getData(self):
        while True:
            res = Cmd.GetString("Want to add a data? (Y/N) ").upper()
            if res == "N":
                break

            data = Cmd.GetString("Enter the data separated by commas, remember the class in the last position: \n").upper().split(",")
            self.dataset.append(data)

        self.test = Cmd.GetString("Enter the data separated by commas to predict: \n").upper().split(",")

    def run(self):
        print('------------------------------------')
        print("Clase: ",self.predict_classification(self.dataset,self.test,self.vecinos))
        print('------------------------------------')