import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset=pd.read_csv('final_project_dataset_1.csv')
dataset.info() #確認是否有遺失資料

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,6].values 


from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
from sklearn.compose import ColumnTransformer

labelencoder_x=LabelEncoder()
x[:,1]=labelencoder_x.fit_transform(x[:,1]) 
labelencoder_x=LabelEncoder()
x[:,4]=labelencoder_x.fit_transform(x[:,4]) 

labelencoder_x=LabelEncoder()
x[:,5]=labelencoder_x.fit_transform(x[:,5])

region=ColumnTransformer([("region",OneHotEncoder(),[5])],remainder='passthrough') 
X=region.fit_transform(x) 

#留下southeast地區為1其餘為0
t1 = np.arange(0,1338)[:,None]
X = np.concatenate((X,t1),axis=1)
X[:,9]=X[:,2]
X=X[:,4:]
X=X[:,[0,2,4,5]]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test) 

import statsmodels.api as sm
#X的第一行插入1 因為線性函式會有常數，所以要自己手動加入
X_train=np.append(arr=np.ones((1070,1)).astype(int),values=X_train,axis=1)
X_opt=X_train[:,[0,1,2,3,4]]
#必須加這行否則input type(array of object)不支援
X_opt=np.array(X_opt,dtype=float)

#做backward elimination模型
regressor_OLS=sm.OLS(endog=y_train,exog=X_opt).fit()
regressor_OLS.summary() #X4 P值最大且P>0.05 刪除X4

X_opt=X_train[:,[0,1,2,3]]
X_opt=np.array(X_opt,dtype=float)
regressor_OLS=sm.OLS(endog=y_train,exog=X_opt).fit()
regressor_OLS.summary()


X_opt=X_opt[:,[1,2,3]]
regressor.fit(X_opt,y_train)
X_test=X_test[:,[0,1,2]]
y_pred_OLS=regressor.predict(X_test) 

residual = y_test - y_pred_OLS
# Positive residual means that the actual charge > predicted charge
# Negative residual means that the actual charge < predicted charge
plt.scatter(y_test, residual)
plt.title("Residual vs Actual charges(backward elimination)")
plt.xlabel("Actual charges")
plt.ylabel("Residual")
plt.show()


residual = y_test - y_pred
# Positive residual means that the actual charge > predicted charge
# Negative residual means that the actual charge < predicted charge
plt.scatter(y_test, residual)
plt.title("Residual vs Actual charges(LinearRegression)")
plt.xlabel("Actual charges")
plt.ylabel("Residual")
plt.show()

