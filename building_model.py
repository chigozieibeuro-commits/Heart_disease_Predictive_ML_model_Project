import  pandas as pd
import  joblib
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import  RandomForestClassifier
from sklearn.pipeline import Pipeline
from   sklearn.model_selection import  GridSearchCV


records=pd.read_csv(r"C:\Users\Dell\Desktop\Heart Attack.csv")

records.columns=records.columns.str.strip()

records.rename(columns={"K":"Potassium"},inplace=True)
records.rename(columns={"Resut":"Result"},inplace=True)
# print(records.to_string())

X=records.drop(columns=['Result'])
y=records["Result"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=RandomForestClassifier(random_state=42)

para={
    "n_estimators":[100,200,300],
    "max_depth":[5,10,15,20],
    "min_samples_split":[2,5,10]
}

grid=GridSearchCV(
    estimator=model,
    param_grid=para,
    cv=5

)


grid.fit(X_train,y_train)


best_model=grid.best_estimator_

joblib.dump(best_model,"Heart_diseases_model.pkl")

