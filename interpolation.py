

## 인덱스가 의미 있을 경우에만 사용가능하며, 시계열 데이터에서 사용하고 싶다면
##  datetime type의 변수를 index에 넣어주어야만 함

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import numpy as np

##  missing data의 갯수
def showMiss(df):
    display(df.isnull().sum())
    
    
def imputing(df):
    if isinstance(df.index,pd.DatetimeIndex):
        method="time"
        df=df.sort_index()
    else: method="values"
    print(f"{method} 방법을 이용합니다.")
    
    df_re=df.select_dtypes(include=np.number)
    df_re=df_re.interpolate(method=method)
    df_re=df_re.fillna(method='bfill')

    cols=df_re.columns
    for col in cols:
        df[col]=df_re[col]

    return df

     
