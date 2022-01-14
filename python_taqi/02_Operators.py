
# # steps involved in data Visualization


# #  Setp 1   # import library 

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks" , color_codes= True )
kashti=sns.load_dataset("titanic")
print(kashti)

p= sns.countplot(x="sex" , data=kashti)
plt.show()





# #steps involved in Data Visualization
# # Step-1 import libraries
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Step-2 set a theme
# sns.set_theme(style="ticks", color_codes=True)

# # Step-3 import data set you can also import your own data
# kashti =  sns.load_dataset("titanic")
# #print(kashti)

#  # Step-4 plot basic graph with 1 variable (count)
# p = sns.countplot(x= "sex", data=kashti)
# plt.show()

# # Step-5 plot basic graph with 2 variable (count plot)
# p = sns.countplot(x= "sex", data=kashti, hue="class")
# plt.show()

# # Step-6 plot basic graph with 2 variable (count plot) wiith Titles
# p = sns.countplot(x= "sex", data=kashti, hue="class")
# p.set_title("Baba_aammar ka count plot for kashti")
# plt.show()