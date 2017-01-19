import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
yummy = pd.read_csv('~/Desktop/pythonexplore/BurlingtonPropertyDetails.csv')


shortyummy = yummy[['Bath1','Bath2','NumofBedrooms']]
# shows the data types
print(shortyummy)

# pd.to_numeric(bvtdata[Bath1], errors='ignore')
# print(bvtdata)
# print(bvtdata['AccountNumber'])
# plt.hist(shortyummy['NumofBedrooms'], bins=100)
plt.scatter(shortyummy['NumofBedrooms'],shortyummy['Bath1'])