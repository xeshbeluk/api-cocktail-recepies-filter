import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

raw_data = 'overall_data.csv'

# loading data into a dataframe
df = pd.read_csv(raw_data, index_col=0)

# checking whether it is loaded successfully
print(df.head(10))
#
# # display all column names
print(list(df))
#
# visualization 1 - distribution of alcoholic and non-alcoholic cocktails
plt.hist(df['strAlcoholic'])
plt.title('Histogram of Distribution of Alcoholic and Non-Alcoholic Cocktails')
plt.xlabel('Number of Drinks in Each Category')
plt.ylabel('Number of Occurences')

# visualization 2
# counting the number of ingredients
numIng = []
for index in df.index:
    number_of_ingredients = 0
    for column in range(6,20):
        if not pd.isnull(df.iat[index,column]):
            number_of_ingredients += 1
    numIng.append(number_of_ingredients)
df['numIng'] = numIng

# visualization 2 - counting ingredients
sns.displot(df, x = 'numIng', kind = 'kde')
plt.title('Density Estimation of Number of Ingredients')
plt.xlabel('Number of Ingredients')
plt.ylabel('Density')
plt.axvline(x=df.numIng.mean(),
            color='red')
plt.show()

# visualization 3
# cleaning the glass column
for i in range(0, len(df)):
    df.iat[i, 4] = df.iat[i,4].lower()

sns.countplot(df, y='strGlass')
plt.title('Counts of Glass Types')
plt.xlabel('Count')
plt.ylabel('Type of Glass')
plt.show()

