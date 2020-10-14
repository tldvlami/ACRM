
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
#import data
travelers = pd.read_excel("/Users/thomasdevlaminck/Desktop/Documents/School Thomas/1e Master Data/Eerste semester/Analytical Customer Relationship Management /travelers.xlsx")
#fill missing values with the value 0
travelers.fillna(value = 0)
#create new column with total travelers during the weekend
travelers["Total travelers during the weekend"] = travelers["Avg number of travelers on Saturday"] + travelers["Avg number of travelers on Sunday"]
#fill missing values again with 0
travelers.fillna(value = 0)
#calculate the ratio of travelers during the weekend over travels during the week
travelers["Ratio weekend / week"] = travelers["Total travelers during the weekend"] / travelers["Avg number of travelers in the week"]
#fill missing values again with 0
travelers.fillna(value = 0)
#sort the percentage by descending mode
travelers = travelers.sort_values(by=["Ratio weekend / week"], ascending = False)

#print the top 10 with highest ratio
print(travelers.head(10))



















