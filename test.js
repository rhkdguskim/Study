class CompletionExecutor {
    constructor(host, apiKey, apiKeyPrimaryVal, requestId) {
        this.host = host;
        this.apiKey = apiKey;
        this.apiKeyPrimaryVal = apiKeyPrimaryVal;
        this.requestId = requestId;
    }

    async _sendRequest(completionRequest) {
        const headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': this.apiKey,
            'X-NCP-APIGW-API-KEY': this.apiKeyPrimaryVal,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': this.requestId
        };

        const requestOptions = {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(completionRequest)
        };

        const response = await fetch(`https://${this.host}/testapp/v1/tasks/stnzsuow/completions/LK-D2`, requestOptions);
        const result = await response.json();
        console.log("결과 : ", result)
        return result;
    }

    async execute(completionRequest) {
        const res = await this._sendRequest(completionRequest);
        if (res.status.code === '20000') {
            return res.result.text;
        } else {
            return 'Error';
        }
    }
}

(async () => {
    const completionExecutor = new CompletionExecutor(
        'clovastudio.apigw.ntruss.com',
        'NTA0MjU2MWZlZTcxNDJiY5tVRn+JNMNOeg9ImaxSDr8nRhXys3hcttMhhVX7c8QT0FcPKKAAl1kXzQrZch+3m8Jr5l9WDSVVPo7N0iugaLG03N+AHCbCAUAEwI+tWrOe1e+N6XNUgDp2dX/T0zWxsxFUImonCVEUw3eG9GfW12pvcgm6tyUbYvgdN2AA+IrKyhRZhYzmvNTAx676bnsrCQ==',
        '7uO13cdRxjNQSWFr0bF0r3eizdSm5q7h8EUHyjDs',
        '91772fc180774efc90599cfe37e941e2'
    );

    const presetText = ' 아래는 AI공공기관챗봇과 사용자의 대화입니다.\n클로바는 민감한 사회적 문제, 욕설, 위험, 폭력적인 발언을 하지 않습니다.\n사용자가 Q를 통하여 답장을 하면 A를 통해서 아래의 내용을 거의 일치하도록 답변합니다.\nQ:개인사업자는연구개발기관에해당하는지?';

    const requestData = {
        text: presetText,
        maxTokens: 32,
        temperature: 0.2,
        topK:0,
        topP: 0.8,
        repeatPenalty: 5.0,
        start: '\nA:',
        restart: ':',
        stopBefore: ['\n', 'Q', 'A'],
        includeTokens: false,
        includeAiFilters: true,
        includeProbs: false
    };

    try{
        const responseText = await completionExecutor.execute(requestData);
        console.log(presetText);
        console.log(responseText);
    }catch(e)
    {
        console.log(e)
    }

})();
