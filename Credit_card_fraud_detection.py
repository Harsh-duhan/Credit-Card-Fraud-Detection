import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV


data = pd.read_csv('creditcard.csv')

X = data.drop('Class', axis=1)
y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()

parameter = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [4, 5, 6, 8, 10, 15, 20, 30, 50, None],
    'max_features': ['sqrt', 'log2', None],
    'splitter': ['best', 'random'],
    'min_samples_split': [2, 3, 5, 8, 10]
}

random_clf = RandomizedSearchCV(
    estimator=clf,
    param_distributions=parameter,
    n_iter=15,
    cv=5,               # 5 folds keeps calculation highly efficient
    scoring='f1',       # Essential metric to optimize for credit fraud
    n_jobs=-1,          # Uses all CPU cores available
    verbose=2,          # Prints live updates so you know it's working
    random_state=42     # Ensures exact reproducibility
)

random_clf.fit(X_train, y_train)
y_pred = random_clf.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
