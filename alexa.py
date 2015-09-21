from flask import Flask
from flask import request
import actions
from response import initial, voice_response
import modules

app = Flask(__name__)

@app.route('/get/', methods=['GET', 'POST'])
def directory():
    data = request.json
    if data['request']['type'] == 'LaunchRequest':
        return initial("Welcome to the Computer Science House Skills Directory")
    intent = data['request']['intent']['name']
    variables = {}
    if 'slots' in data['request']['intent']:
        for s in data['request']['intent']['slots']:
                variables[s] = (data['request']['intent']['slots'][s]['value'])
    if intent in functions:
        response, done = functions[intent](**variables)
        return voice_response(response, done)
    return modules.err_handle.error()



functions = actions.actions
if __name__ == '__main__':
    app.run()
