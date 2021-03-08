
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

##  missing data의 갯수
def showMiss(df):
    display(df.isnull().sum())
    
    
def KNNImpute(df):

    imputer=KNNImputer(n_neighbors=5)
    new_df=imputer.fit_transform(df)
    new_df=pd.DataFrame(new_df,columns=df.columns)


    return new_df
