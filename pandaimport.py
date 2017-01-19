%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
property = pd.read_csv('~/Desktop/pythonexplore/BurlingtonPropertyDetails.csv')
property.head(20)
# list(property)

baths = property[['Bath1','Bath2','NumofBedrooms']]
plt.scatter(baths['Bath2'],baths['Bath1'])

onefamily = property[property['LandUse'] == "1 Family"]
sizeonefamily = onefamily.ix[:,'CurrentAcres':'FinishedArea']
sizeonefamilyrefined = sizeonefamily[(sizeonefamily['FinishedArea'] < 150000) & (sizeonefamily['TotalGrossArea'] < 150000)]
plt.scatter(sizeonefamilyrefined['TotalGrossArea'],sizeonefamilyrefined['FinishedArea'])

twofamily = property[property['LandUse'] == "2 Family"]
sizetwofamily = twofamily.ix[:,'CurrentAcres':'FinishedArea']
sizetwofamilyrefined = sizetwofamily[(sizetwofamily['FinishedArea'] < 150000) & (sizetwofamily['TotalGrossArea'] < 150000)]
plt.scatter(sizetwofamilyrefined['TotalGrossArea'],sizetwofamilyrefined['FinishedArea'])