import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

store_data = pd.read_csv("store_data.csv", header=None)

records = []
for i in range(1, 7501):
    records.append([str(store_data.values[i, j]) for j in range(0, 20)])

print(type(records))


association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print("ada {} data.".format(len(association_results)))

for i in range(0, len(association_results)):
    print(association_results[i][0])

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")