import pandas as pd
import dill as pickle
from flask import jsonify, request, Blueprint, render_template, abort
from flask_api.models import model_dict

predict = Blueprint('predict', __name__, template_folder='../predict/templates', static_folder='../predict/static',
                    url_prefix='/predict')


@predict.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@predict.route('/demo', methods=['POST'], endpoint='predict_demo')
def predict_demo():
    try:
        test_json = str(request.data, encoding='utf-8')
        test = pd.read_json(test_json, orient='records')
        # To resolve the issue of TypeError: Cannot compare types 'ndarray(dtype=int64)' and 'str'
        test['Dependents'] = [str(x) for x in list(test['Dependents'])]
        loan_ids = test['Loan_ID']
    except Exception as e:
        abort(400)

    if test.empty:
        abort(400)

    filename = model_dict.get('demo', '')
    if not filename:
        abort(500)

    loaded_model = None
    with open('flask_api/models/models/' + filename, 'rb') as f:  # Load the saved model
        loaded_model = pickle.load(f)

    predictions = loaded_model.predict(test)

    prediction_series = list(pd.Series(predictions))

    final_predictions = pd.DataFrame(list(zip(loan_ids, prediction_series)))

    responses = jsonify(predictions=final_predictions.to_json(orient="records"))
    responses.status_code = 200

    return responses
