# Import Libraries

from joblib import load
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Load model
model = load("../models/water_potability.pkl")


@app.route('/')
@app.route('/index')
def main_page():
    return render_template('index.html', title="Water Potability", result="")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # ph_value = request.args.get('ph_value')
    # hardness = request.args.get('hardness')
    # solids = request.args.get('solids')
    # chloramines = request.args.get('chloramines')
    # sulfate = request.args.get('sulfate')
    # conductivity = request.args.get('conductivity')
    # organic_carbon = request.args.get('organic_carbon')
    # trihalomethanes = request.args.get('trihalomethanes')
    # turbidity = request.args.get('turbidity')

    test_data = list(request.form.values())
    # test_data = [ph_value, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes,
    #              turbidity]
    test_data = [convert_to_float(x) for x in test_data]
    test_data = np.array(test_data).reshape(1, 9)
    result = model.predict(test_data)

    if result[0] == 0:
        result_str = ' Non-Potable.'
    else:
        if result[0] == 1:
            result_str = ' Potable'

    final_result = "Based on the input parameters the model predicts that the water would be" + result_str

    return render_template("index.html", title="Water Potability", result=final_result)


def convert_to_float(x):
    try:
        return float(x)
    except ValueError:
        return 0


def main():
    app.run(port=3001, debug=True)


if __name__ == '__main__':
    main()
