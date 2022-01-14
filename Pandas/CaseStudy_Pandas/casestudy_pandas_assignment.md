# Pandas Case study on FAO Stat Data
- In this Panda Case study we have analyze share of employment in agriculture, forestry and fishing in total employment in Pakistan from 2009 to 2018.
- Note: Data is Taken from the Website of [Food and Agriculture organization of United Nation.](https://www.fao.org/faostat/en/#data/OE)

> # Code

```
# importing the Different Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pakdata=pd.read_csv("faostat.csv")

pakdata.head(3)
#dropping/ Ignoring the Data (few columns) to make new data

pakdata.drop(["Domain Code", "Source Code","Domain","Indicator Code","Note","Area Code (FAO)", "Flag"],  axis=1).head(3)
# setting theme of the Plot

sns.set_theme(style="whitegrid", palette="muted")
# loading data from File
pakdata=pd.read_csv("faostat.csv")

# Drawing a categorical scatterplot to show each observation
ax = sns.swarmplot(data=pakdata, x="Year", y="Value", hue="Source")
plt.title("Share of Employment in Agriculture, Forestry and Fishing in total employment in Pakistan")
ax.set(ylabel="Share of Employment")
```

