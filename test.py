# -*- coding: utf-8 -*-

import base64
import json
import http.client


class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/testapp/v1/tasks/stnzsuow/completions/LK-D2', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['text']
        else:
            return 'Error'


if __name__ == '__main__':
    completion_executor = CompletionExecutor(
        host='clovastudio.apigw.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiY5tVRn+JNMNOeg9ImaxSDr8nRhXys3hcttMhhVX7c8QT0FcPKKAAl1kXzQrZch+3m8Jr5l9WDSVVPo7N0iugaLG03N+AHCbCAUAEwI+tWrOe1e+N6XNUgDp2dX/T0zWxsxFUImonCVEUw3eG9GfW12pvcgm6tyUbYvgdN2AA+IrKyhRZhYzmvNTAx676bnsrCQ==',
        api_key_primary_val = '7uO13cdRxjNQSWFr0bF0r3eizdSm5q7h8EUHyjDs',
        request_id='91772fc180774efc90599cfe37e941e2'
    )

    preset_text = 'input text'

    request_data = {
        'text': preset_text,
        'maxTokens': 300,
        'temperature': 0.85,
        'topK': 4,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '',
        'restart': '',
        'stopBefore': ['<|endoftext|>'],
        'includeTokens': False,
        'includeAiFilters': True,
        'includeProbs': False
    }

    response_text = completion_executor.execute(request_data)
    print(preset_text)
    print(response_text)
