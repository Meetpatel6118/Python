import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('Grainsize_Por.csv')

print(df.sample(10))

print(df.isnull().sum())
df.dropna(inplace=True)  

X = df[['Grainsize']]  
y = df['Porosity'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

plt.scatter(X_train, y_train, color='red', label='Training data')
plt.scatter(X_test, y_test, color='blue', label='Test data')
plt.plot(X_train, y_pred_train, color='green', label='Predictions (Training)')
plt.plot(X_test, y_pred_test, color='yellow', label='Predictions (Test)')
plt.xlabel('Grain Size')
plt.ylabel('Porosity')
plt.title('Linear Regression Model')
plt.legend()

grain_size_70 = [[70]]  
porosity_70 = model.predict(grain_size_70)
print("Porosity of a grain with size 70:", porosity_70)

plt.show()
