from flask import Flask, jsonify, request
from SOAPpy import WSDL
from time import sleep
from json import loads
from os import getenv


app = Flask(__name__)
wsdlObject = WSDL.Proxy('http://ideone.com/api/1/service.wsdl')

languages = {
    'python': 4,
    'ruby': 17,
    'java': 10,
    'javascript': 35,
    'go': 114
}

user = 'gavincabbage'
password = getenv('KODEKATA_API_PASSWORD') 



def parse(response):
    rd = dict()
    for item in response['item']:
        rd[str(item.key)] = item.value
    return rd
    
    
@app.route('/run/<string:lang>', methods=['POST'])
def run(lang):

    data = loads(request.data)
    
    try:
        source = data['code'] + "\n\n" + data['tests']
    except KeyError:
        result = 'ERROR: code and/or tests not provided'
        return jsonify({'result': result}), 200
        
    try:
        lang_code = languages[lang]
    except KeyError:
        result = 'ERROR: requested language not supported'
        return jsonify({'result': result}), 200
    else:
        response = wsdlObject.createSubmission(
            user, password, source, lang_code, '', True, True)
    
    try:
        link = parse(response)['link']
    except KeyError:
        result = 'ERROR: no link provided by API'
        return jsonify({'result': result}), 200
    else:
        sleep(3)
        response = wsdlObject.getSubmissionDetails(
            user, password, link, False, False, True, True, False)
        
    try:
        result = parse(response)['output']
    except KeyError:
        result = 'ERROR: no output provided by API'
    else:
        return jsonify({'result': result}), 200
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4242)
