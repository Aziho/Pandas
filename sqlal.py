import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
PATH = "D:/BCIT/PythonFundamental/Datasets/"
FILE = "fruit.csv"
df = pd.read_csv(PATH + FILE)
def showQueryResult(sql):
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='fruit', con=connection, if_exists='replace', index=False)
    queryResult = pd.read_sql(sql, connection)
    return queryResult
def getPosition(result,columnName):
    columnList=result.keys()
    for i in range(0,len(columnList)):
        columnPosition = 0
        for i in range(0, len(columnList)):
            if (columnList[i] == columnName):
                columnPosition = i
                break
        return columnPosition


SQL = "SELECT Region, Product, SUM(Quantity) As TotalSold FROM  fruit  WHERE  Product = 'apples'   GROUP   BY  Region, Product"
result=showQueryResult(SQL)

region=getPosition(result,'Region')
Sold= getPosition(result,'TotalSold')
for i in range (0,len(result)):
    plt.bar(result.iat[i,region],result.iat[i,Sold],color='green')
plt.title('Total Amounts Sold Apples')
plt.show()



