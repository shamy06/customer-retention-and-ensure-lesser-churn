
from flask import request
#  Using library To Process Incoming Request Data in Flask
from flask import Flask, render_template
#used to generate output from a template from templates folder.
from flask import jsonify
import requests
import pickle
#Pickle module implements binary proto.for serializing &
# de-serializing a Python object structure.
import numpy as np
#open-source library for the Python prog lang,
# for scientific computing and working with arrays
import sklearn
# machine learning library for the Python programming language
app = Flask(__name__)
model = pickle.load(open('D:\\Customerchurn\\Telco-Customer-Churn.pkl', 'rb'))
# It is used to load pickled data from a bytes string.
@app.route('/', methods=['GET'])
#The route() fun  is a decorator, which tells the 
# application which URL should call the associated function.
def Home():
    return render_template('index.html')

@app.route("/about")   
def about():
    return render_template('about.html')

@app.route('/predict',methods=['POST'])
def predict():
    #The request.from command is used to 
    # collect values in a form with method="post"
    if request.method == 'POST':
        tenure = int(request.form['tenure']) #tenure field
        MonthlyCharges = float(request.form['MonthlyCharges'])
        TotalCharges = float(request.form['TotalCharges'])
        Contract=request.form['Contract_OneYear']
        if(Contract=='One Year'): #contract field
            Contract_OneYear=1
            Contract_TwoYear=0

        else:
            Contract_OneYear=0
            Contract_TwoYear=1
        Dependents= request.form['Dependents_Yes']
        if(Dependents=='Yes'):
            Dependents_Yes=1
        else:
            Dependents_Yes=0
        DeviceProtection=request.form['DeviceProtection_Yes']
        if(DeviceProtection=='Yes'):
            DeviceProtection_Yes=1
        else:
            DeviceProtection_Yes=0
        gender_Male = request.form['gender_Male']
        if(gender_Male == 'Male'):
            gender_Male = 1
        else:
            gender_Male = 0
        InternetService=request.form['InternetService_No']
        if (InternetService=='Fiberoptic'):
             InternetService_Fiberoptic=1
             InternetService_No=0
        else:
            InternetService_Fiberoptic=0
            InternetService_No=1
        MultipleLines=request.form['MultipleLines_Yes']
        if(MultipleLines=='Yes'):
            MultipleLines_Yes=1
        else:
            MultipleLines_Yes=0
        OnlineBackup=request.form['OnlineBackup_Yes']
        if(OnlineBackup=='Yes'):
            OnlineBackup_Yes=1
        else:
            OnlineBackup_Yes=0
        OnlineSecurity=request.form['OnlineSecurity_Yes']
        if(OnlineSecurity=='Yes'):
            OnlineSecurity_Yes=1
        else:
            OnlineSecurity_Yes=0
        Paperlessbilling=request.form['Paperlessbilling_Yes']
        if(Paperlessbilling=='Yes'):
            Paperlessbilling_Yes=1
        else:
            Paperlessbilling_Yes=0
        Partner=request.form['Partner_Yes']
        if(Partner=='Yes'):
            Partner_Yes=1
        else:
            Partner_Yes=0
        PaymentMethod=request.form['PaymentMethod_Electroniccheck']
        if(PaymentMethod=='Electroniccheck'):
            PaymentMethod_Electroniccheck=1
            PaymentMethod_Creditcard=0
            PaymentMethod_Mailedcheck=0
        elif(PaymentMethod=="Mailedcheck"):
            PaymentMethod_Electroniccheck=0
            PaymentMethod_Creditcard=0
            PaymentMethod_Mailedcheck=1
        else:
            PaymentMethod_Electroniccheck=0
            PaymentMethod_Creditcard=1
            PaymentMethod_Mailedcheck=0
        PhoneService=request.form['PhoneService_Yes']
        if(PhoneService=='Yes'):
            PhoneService_Yes=1
        else:
            PhoneService_Yes=0
        SeniorCitizen =(request.form['SeniorCitizen_1'])
        StreamingMovies=request.form['StreamingMovies_Yes']
        if(StreamingMovies=='Yes'):
            StreamingMovies_Yes=1
        else:
            StreamingMovies_Yes=0
        StreamingTv=request.form['StreamingTv_Yes']
        if(StreamingTv=='Yes'):
            StreamingTv_Yes=1
        else:
            StreamingTv_Yes=0
        TechSupport=request.form['TechSupport_Yes']
        if(TechSupport=='Yes'):
            TechSupport_Yes=1
        else:
            TechSupport_Yes=0
        pred =[(tenure),(MonthlyCharges),(TotalCharges),int(Contract_OneYear),int(Contract_TwoYear),int(Dependents_Yes),int(DeviceProtection_Yes),int(gender_Male),int(InternetService_Fiberoptic),int(InternetService_No),int(MultipleLines_Yes),int(PhoneService_Yes),int(OnlineBackup_Yes),int(OnlineSecurity_Yes),int(Paperlessbilling_Yes),int(Partner_Yes),int(PaymentMethod_Electroniccheck),int(PaymentMethod_Mailedcheck),int(PaymentMethod_Creditcard),int(SeniorCitizen),int(StreamingMovies_Yes),int(StreamingTv_Yes),int(TechSupport_Yes)]     
        final=[np.array(pred)]
        prediction=model.predict(final)
        '''
        For rendering results on HTML GUI
        '''
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave")
        else:   
             return render_template('index.html',prediction_text="The Customer will not leave")
          
if __name__ == "__main__":
    app.run(debug=True)
 