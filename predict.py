import pandas as pd
from sklearn.externals import joblib

# Load from file
joblib_model = joblib.load("joblib_model.pkl")

train = {'AGE_GBN': ['2'], "MARRY_Y": ['2'], "JOB_GBN": ['4'], "ADD_GBN": ['5'], "INCOME_GBN": ['3'], "NUMCHILD": ['0'],
         'TOT_ASSET': ['5000'], 'CHUNG_Y': ['5'], 'TOT_DEBT': [0], 'D_JUTEAKDAMBO': 0, 'RETIRE_NEED': 0,
         'FOR_RETIRE': ['0'], 'TOT_SOBI': ['200']}



train = pd.DataFrame(train)

Y_predict = joblib_model.predict(train)
print(Y_predict)

