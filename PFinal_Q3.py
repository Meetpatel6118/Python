import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('Life_Expectancy_Data.csv')

print(df.sample(10))

print(df.isnull().sum())
df.dropna(inplace=True)  

df = pd.get_dummies(df, columns=['Status'])

df = df.drop(columns=['Country', 'Year', 'Measles', 'percentage expenditure'])

print(df.sample(25))

X = df.drop(columns=['Life expectancy'])
y = df['Life expectancy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Life Expectancy")
plt.ylabel("Predicted Life Expectancy")
plt.title("Actual vs Predicted Life Expectancy")
plt.show()
