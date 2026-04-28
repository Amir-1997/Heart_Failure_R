import time
import requests


URL = "http://localhost:8000"

# input

# Age = input("Enter your age: ")
# Sex = input("Enter your gender: ")
# Cp = input("Enter your cp: ")
# Trestbps = input("Enter your trestbps: ")
# Fbs = input("Enter your fbs: ")
# Restecg = input("Enter your restecg: ")
# Thalach = input("Enter your thalach: ")
# Exang = input("Enter your exang: ")
# Oldpeak = input("Enter your oldpeak: ")

#json dict

predictors = {
    "age": 45,
    "sex": 1,
    "cp": 4,
    "trestbps": 120,
    "fbs": 0,
    "restecg": 0,
    "thalach": 140,
    "exang": 0,
    "oldpeak": 0,
}

# requests
def predict():
    response = requests.post(url=f"{URL}/predict", params=predictors)
    return response.json()



start = time.perf_counter()
predicted = predict()
print(predicted)
print(time.perf_counter() - start)

