# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim = float(request.form['CRIM'])
            zn = float(request.form['ZN'])
            indus = float(request.form['INDUS'])
            chas = float(request.form['CHAS'])
            nox = float(request.form['NOX'])
            rm = float(request.form['RM'])

            dis = float(request.form['DIS'])
            rad = float(request.form['RAD'])
            ptratio = float(request.form['PTRATIO'])
            lstat = float(request.form['LSTAT'])
            b = float(request.form['B'])

            filename = 'boston_lr_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[crim, zn, indus, chas, nox, rm, dis, rad, ptratio, b, lstat]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('index.html', prediction=round(prediction[0],4))
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
