import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd_data = pd.read_csv('final_project_dataset_2.csv')
pd_data.shape

pd_data=pd_data.dropna(how='any')


#drop something column
drop_columns_list = ['WindGustDir', 'WindDir9am', 'WindDir3pm','Date','Location']
pd_data = pd_data.drop(drop_columns_list, axis=1)



X = pd_data.iloc[:,0:-1]
Y = pd_data.iloc[:,17:18]

from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
from sklearn.compose import ColumnTransformer
labelencoder_X=LabelEncoder()
X['RainToday']=labelencoder_X.fit_transform(X['RainToday'].astype(str))

labelencoder_Y=LabelEncoder()
Y['RainTomorrow']=labelencoder_Y.fit_transform(Y['RainTomorrow'].astype(str))


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)


"""
#fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

#fitting SVM to training set
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(X_train,y_train)


y_pred=classifier.predict(X_test)

#混淆矩陣
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

n=(10477+1631)/(10477+542+1455+1631)
print(n) >0.85





from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(bootstrap=True,n_estimators=1000,max_depth=7)#(多少棵樹在森林裡，)
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

n=(10585+1482)/(10585+434+1604+1482)
print(n) >0.85


#fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

#fitting SVM to training set
from sklearn.svm import SVC
classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(X_train,y_train)


y_pred=classifier.predict(X_test)

#混淆矩陣
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

n=(10781+1123)/(10781+238+1963+1123)
print(n) >0.84
"""