
"""
autor: @anamo 
"""

# Life expectancy & Socio-Economic (world bank)
"""Importing libraries"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Creating Data Frames 
df_life= pd.read_csv('/kaggle/input/life-expectancy-and-socio-economic-world-bank/life expectancy.csv')
print(df_life.head())

print(df_life.head())

#Counting missing values and filling with 0 
print(df_life.isna().sum())
df_life.fillna(0)

#Understanding data
print(df_life.describe())
print(df_life.keys())
print(df_life.info())


# Relationship between the life expectancy and the health expenditure pairplot in a scatterplot
sns.pairplot(data=df_life,
        vars=["Life Expectancy World Bank", "Health Expenditure %"],
        kind='scatter',
        hue='Region',
        palette='RdBu',
        diag_kws={'alpha':.5})
plt.show()
plt.clf()

#Correlation
print(df_life["Life Expectancy World Bank"].corr(df_life["Health Expenditure %"]))

#Boxplot Life expectancy for region
sns.boxplot(data= df_life, x="Region", y= "Life Expectancy World Bank", palette= "Blues")
plt.xticks(rotation= 30)
plt.title("Life Expectancy World Bank per Region")
plt.show()

#the 10 Most Countries with the hights life expectancy
#Average life expectancy per country Scatterplot
df_lifeavg_per_country= df_life.groupby(["Country Name", "Region"], as_index= False)["Life Expectancy World Bank"].mean()
df_sorted_life= df_lifeavg_per_country.sort_values("Life Expectancy World Bank", ascending=False)
df_life10=df_sorted_life.iloc[0:10]

qualitative_colors = sns.color_palette("colorblind", 4)
sns.scatterplot(data= df_life10, x= "Country Name", y= "Life Expectancy World Bank", hue= "Region", palette= qualitative_colors)
plt.title("The 10 Countries with the Highest Life Expectancy Avg")
plt.xticks(rotation= 30)
plt.show()

#CO2 Avg for each income group in a barplot 

df_co2_per_group= df_life.groupby(["IncomeGroup"], as_index= False)["CO2"].mean()
df_co2_sorted= df_co2_per_group.sort_values("CO2", ascending=True)
sns.barplot(data= df_co2_sorted, x= "IncomeGroup", y= "CO2", palette= "crest")
plt.title("CO2 Average per income group from 2001-2019")
plt.ylabel("CO2 (kiloton)")
plt.xticks(rotation= 20)
plt.show()                           


#Education Expenditure and Health Expenditure from 2009 to 2019 in  a lineplot
sns.set_theme(style="whitegrid")
fig, ax= plt.subplots()
years= df_life["Year"].unique()

df_life_health= df_life.groupby(["Year"])["Health Expenditure %"].mean()
df_life_edu= df_life.groupby(["Year"])["Education Expenditure %"].mean()
y= list(years)
ax.plot(years, df_life_health, color="g")
ax.plot(years, df_life_edu, color= "b")
ax.legend(["Health Expenditure %", "Education Expenditure %"], loc="center")
plt.xticks(y, rotation= 90)
plt.ylabel("%")
plt.xlabel("Year")
plt.title("Average health & education expenditure per year")
plt.show()

# Building  a joint plot for injueries and life expectancy
sns.jointplot(x="Injuries",
        y="Life Expectancy World Bank",
        kind='reg',
        data=df_life)
plt.show()
plt.clf()

