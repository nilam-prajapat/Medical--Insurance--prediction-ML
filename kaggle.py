import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
df = pd.read_csv(r"C:\Users\HP\Desktop\madical premium\Medicalpremium.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.columns)
correlation = df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(correlation, annot=True, cmap='PuBuGn')
plt.title('correlation matrix')
plt.show()
#let's split the data into X, and y variable
X = df.drop('PremiumPrice',axis=1)
y = df['PremiumPrice']

#split the data into test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#import libraries
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

#create a pipeline for preprocessing and model
pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('model',RandomForestRegressor())
])

#fit the pipeline on training data
pipeline.fit(X_train,y_train)

#predict on X_test
y_pred = pipeline.predict(X_test)
from sklearn.metrics import mean_squared_error,r2_score

mse = mean_squared_error(y_pred, y_test)
r2 = r2_score(y_test, y_pred)

print('Mean squared error :',r2)
print('R^2 :', r2)

joblib.dump(pipeline, "premium_model.pkl")
print("✅ Model saved as premium_model.pkl")