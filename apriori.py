
# page: https://pypi.org/project/efficient-apriori/
from cProfile import label
from efficient_apriori import apriori
from cmd import Cmd


class Apriori:
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
        self.transactions = [('EGGS', 'BACON', 'SOUP'), ('EGGS', 'BACON', 'APPLE'), ('SOUP', 'BAACON', 'BANANA'), ('BANANA', 'APPLE', 'SOUP')]

    def run(self):
        _, rules = apriori(self.transactions, min_support=self.minSupport, min_confidence=self.minConfidence)

        # Print out every rule with 2 items on the left hand side,
        # 1 item on the right hand side, sorted by lift

        print('---------------------------------------------')
        print("                 TRANSACTIONS                ")
        print('---------------------------------------------')
        rules_rhs = filter(lambda rule: len(rule.lhs) == 2 and len(rule.rhs) == 1, rules)
        for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
            print(rule)

        print('---------------------------------------------')

