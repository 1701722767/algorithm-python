
# page: https://pypi.org/project/efficient-apriori/
from cProfile import label
from efficient_apriori import apriori
from cmd import Cmd


class Apriori:
    # For example
    # transactions = [('EGGS', 'BACON', 'SOUP'), ('EGGS', 'BACON', 'APPLE'), ('SOUP', 'BAACON', 'BANANA'), ('BANANA', 'APPLE', 'SOUP')]


    transactions = None
    minSupport = 0
    minConfidence = 0


    def getData(self):
        self.minSupport = Cmd.GetNumber("Enter the minimum support: ",0,1)
        self.minConfidence = Cmd.GetNumber(label="Enter the confidence: ")

        transactions = []

        while True:
            res = Cmd.GetString("Want to add a transaction? (Y/N) ").upper()
            if res == "N":
                break

            transaction = Cmd.GetString("Enter transactions separated by commas: \n").upper().split(",")
            transactions.append(transaction)

        self.transactions = transactions

    def run(self):
        _, rules = apriori(self.transactions, min_support=self.minSupport, min_confidence=self.minConfidence)

        print('---------------------------------------------')
        print("                 TRANSACTIONS                ")
        print('---------------------------------------------')
        for rule in rules:
            print(rule)

        print('---------------------------------------------')

