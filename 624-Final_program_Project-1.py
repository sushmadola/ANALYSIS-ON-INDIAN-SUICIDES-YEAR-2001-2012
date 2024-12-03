
#AUTHOR NAME : Dola Sushma
#ANALYSIS ON INDIAN SUICIDES : YEAR: 2001-2012
#CWID: 10432431

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import seaborn as sns

read = pd.read_csv('Dataset1.csv')

social = read[read['Type_code']=='Social_Status']

education = read[read['Type_code']=='Education_Status']

causes = read[read['Type_code']=='Causes']

means = read[read['Type_code']=='Means_adopted']

prof_status = read[read['Type_code']=='Professional_Profile']

#################################fig1) Education Status

dataset1 = read.loc[(read.Type_code == 'Education_Status')].groupby(['Type'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(10)

dataset1.set_index(['Type'])

dataset1=dataset1.set_index(['Type'])

plt.subplots(figsize=(10,6))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="PuOr",).set_title('Relation of Education status with suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Education Level')

plt.ylabel('Total no. of suicides')

plt.tight_layout()

#################################fig2) Causes

dataset1 = read.loc[(read.Type_code == 'Causes')].groupby(['Type'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(30)

dataset1.set_index(['Type'])

dataset1=dataset1.set_index(['Type'])

plt.subplots(figsize=(10,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="PuOr",).set_title('Causes of suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Total number of suicides')

plt.xlabel('Causes of suicides')

plt.tight_layout()

################################fig3) Professional Status    

dataset1 = read.loc[(read.Type_code == 'Professional_Profile')].groupby(['Type'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(30)

dataset1.set_index(['Type'])

dataset1=dataset1.set_index(['Type'])

plt.subplots(figsize=(15,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="RdBu",).set_title('Relation of Professional Profile with suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Professional profiles')

plt.ylabel('Total number of suicides')

plt.tight_layout()

#########################fig4) Social Status

dataset1 = read.loc[(read.Type_code == 'Social_Status')].groupby(['Type'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(10)

dataset1.set_index(['Type'])

dataset1=dataset1.set_index(['Type'])

plt.subplots(figsize=(15,7))

plot= sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="RdBu",).set_title('Relation of Social status with suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Social Status')

plt.ylabel('Total number of suicides')

plt.tight_layout()

#####################fig5) Means Adopted

dataset1 = read.loc[(read.Type_code == 'Means_adopted')].groupby(['Type'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(40)

dataset1.set_index(['Type'])

dataset1=dataset1.set_index(['Type'])

plt.subplots(figsize=(15,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="RdYlGn",).set_title('Means adopted for committing suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Means adopted')

plt.ylabel('Total number of suicides')

plt.tight_layout()

#######################fig6) Gender

dataset1 = read.groupby(['Gender'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(2)

dataset1.set_index(['Gender'])

dataset1=dataset1.set_index(['Gender'])

plt.subplots(figsize=(15,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="RdBu").set_title('Gender bifurcation wrt. Suicides in India')

plt.xticks(rotation=90)

plt.xlabel('Gender')

plt.ylabel('Total number of suicides')

plt.tight_layout()

########################fig 7) AGE WISE

dataset1 = read.groupby(['Age_group'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(10)

dataset1.set_index(['Age_group'])

dataset1=dataset1.set_index(['Age_group'])

plt.subplots(figsize=(15,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="RdGy").set_title('Age groups vs Suicides-India(2001-2012)')

plt.xticks(rotation=90)

plt.xlabel('Age groups')

plt.ylabel('Total number of suicides')

plt.tight_layout()

###############fig 8) STATE

dataset1 = read.groupby(['State'])['Total'].sum().reset_index().sort_values('Total',ascending=False).head(50)

dataset1.set_index(['State'])

dataset1=dataset1.set_index(['State'])

plt.subplots(figsize=(15,7))

plot = sns.barplot(y='Total',x=dataset1.index,data=dataset1,palette="Set1",).set_title('State-wise Analysis of suicides')

plt.xticks(rotation=90)

plt.xlabel('State')

plt.ylabel('Total number of suicides')

plt.tight_layout()

plt.show()
