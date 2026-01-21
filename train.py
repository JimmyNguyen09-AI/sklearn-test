from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
x,y = load_iris(return_X_y=True)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=9)
model = LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)
acc = accuracy_score(y_test,y_pred)
print("Accuracy",acc)