import pandas as pd
import seaborn as sns

# making a dataframe
df = pd.read_csv('iris-data.csv')
# 1.    drooping the null values rows
# 2.    can use mean , median , mode property ti fill the NA values
df = df.dropna(subset=['petal_width_cm'])
# print(df.info())

# checking whether the names of the output are same or not whether there is no spelling mistake
# print(df['class'].value_counts())           # diff spellings for same class name

# correcting the spelling
df['class'].replace(['Iris-setossa','versicolor'],['Iris-setosa','Iris-versicolor'], inplace = True)
# print(df['class'].value_counts())

# using only class as Iris-setosa

df_setosa = df[ df['class'] == 'Iris-setosa' ]

aa = sns.pairplot(df_setosa, hue='class', size=2.5)
print(aa)