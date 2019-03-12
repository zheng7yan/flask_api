from unittest import TestCase

import pandas as pd
import json
import requests
from tests import BASE_URL


class DemoTestCase(TestCase):
    def test_demo(self):
        df = pd.read_csv('../flask_api/models/data/demo/test.csv', encoding="utf-8-sig")
        data = df.to_json(orient='records')
        resp = requests.post("{}/predict/demo".format(BASE_URL), json=json.loads(data, encoding="utf-8-sig"))
        # resp = requests.post("{}/predict/demo".format(BASE_URL), json={})  # dummpy test, assume input data error
        # import pdb; pdb.set_trace()
        self.assertIs(resp.status_code, 200)
        print(resp.json())

    def test_heat(self):
        data = [
            {
                'id': 'a',
                'Temperature': -10,
                'Value': 86.670000
            },
            {
                'id': 'b',
                'Temperature': -1,
                'Value': 7
            },
        ]
        resp = requests.post("{}/predict/heat".format(BASE_URL), json=data)
        self.assertIs(resp.status_code, 200)
        print(resp.json())
