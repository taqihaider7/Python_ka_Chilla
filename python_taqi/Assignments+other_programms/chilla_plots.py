# importing the different libraries i.e: pandas library because it deals with the Data Analysis
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Loading the data from the file
chilla= pd.read_csv("Chilla_data.csv")
sns.set_theme(style="ticks", color_codes=True)

sns.countplot(x="Gender", hue="What are you?", data=chilla)
plt.show()



