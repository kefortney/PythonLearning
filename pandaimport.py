import pandas as pd
import matplotlib.pyplot as plt
import numpy as nm
dataimport = pd.read_csv('~/Desktop/pythonexplore/ProperySalesPrice.csv',header='infer')

plt.hist(dataimport['Sale Date'], bins=100)
dataimport.describe()