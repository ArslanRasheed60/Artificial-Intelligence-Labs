import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

data = pd.read_csv("fifa_data.csv")

mylabels = ["under 125", "125-150", "150-175", "175-200", "over 200"]

data = np.array([data["Weight"][(data.Weight < "125lbs")].count(),
       data["Weight"][(data.Weight >= "125lbs") & (data.Weight < "150lbs")].count(),
                data["Weight"][(data.Weight >= "150lbs") & (data.Weight < "175lbs")].count(),
                data["Weight"][(data.Weight >= "175lbs") & (data.Weight < "200lbs")].count(),
                data["Weight"][(data.Weight >= "200lbs")].count()])

myexplode = [0.5, 0.2, 0, 0, 0.4]

pt.pie(data, labels=mylabels, explode=myexplode, autopct='%1.1f%%')
pt.legend()
pt.show()

# print(data)


pt.bar(mylabels, data)
pt.show()

pt.hist(data)
pt.show()

pt.boxplot(data)
pt.show()
