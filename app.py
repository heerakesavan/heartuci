#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/Pickle_logreg_Model.pkl', 'rb') as f:
    logistic = pickle.load(f)

with open('Models/Pickle_svm_Model.pkl', 'rb') as f:
    svm_model = pickle.load(f)


def get_predictions(age,sex,chol, req_model):
    mylist = [age, sex, chol]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]

    elif req_model == 'SVM':
        #print(req_model)
        return svm_model.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chol= request.form['chol']
        req_model = request.form['req_model']

        target = get_predictions(age,sex.chol, req_model)

        if target==1:
            value = 'Patient likely has heart disease'
        else:
            value = 'Heart disease unlikely'

        return render_template('home.html', target = target, sale_making = value)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)