import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

PATH = "D:/BCIT/PythonFundamental/Datasets/"

CSV_DATA = "heart_original.csv"

df = pd.read_csv(PATH + CSV_DATA,skiprows=1,names=('age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target'))

dfcol=round(df.groupby('age')['chol'].mean().reset_index().rename(columns={'chol':'Emanchol'}),2)
dfpeople=df.groupby('age')['sex'].count().reset_index().rename(columns={'sex':'totalpeople'})
dfcol['Total people']=dfpeople['totalpeople']
print(dfcol)

plt.subplots(nrows=2,ncols=2,figsize=(14,7))
plt.subplot(2,2,3)
plt.hist(['age'], bins=14)
# plt.subplot(2,3,2)
# plt.hist(['chol'],bins=14)
plt.show()
