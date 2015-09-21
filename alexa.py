from flask import Flask
from flask import request

app = Flask(__name__)

initial = """
{
"version": "1.0",
"sessionAttributes": {
"countActionList": {
"read": true,
"category": true,
"currentTask": "none",
"currentStep": 0
}
},
"response": {
"outputSpeech": {
"type": "PlainText",
"text": "Welcome to the Computer Science House Skills Directory"
},
"responsecard": {
"type": "Simple",
"title": "CSH Directory Application",
"content": "CSH skills lookup tool"
},
"reprompt": {
"outputSpeech": {
"type": "PlainText",
"text": "Can I help you with anything else?"
}
},
"shouldEndSession": "false"
}
}

"""



@app.route('/get/', methods=['GET', 'POST'])
def directory():
    data = request.json
    if (data['request']['type'] == 'LaunchRequest'):
        return initial
    #first = (data['request']['intent']['slots']['first']['value'])
    #last = (data['request']['intent']['slots']['last']['value'])
    intent = data['request']['intent']['name']
    variables = {}
    if 'slots' in data['request']['intent']:
        for s in data['request']['intent']['slots']:
                variables[s] = (data['request']['intent']['slots'][s]['value'])
    if intent in functions:
        response, done = functions[intent](**variables)
        resp = """
        {
        "version": "1.0",
        "sessionAttributes": {
        "countActionList": {
        "read": true,
        "category": true,
        "currentTask": "none",
        "currentStep":"1" 
        }
        },
        "response": {
        "outputSpeech": {
        "type": "PlainText",
        "text": "%s"
        },
        "card": {
        "type": "Simple",
        "title": "CSH Directory",
        "content": "Skill Lookup"
        },
        "reprompt": {
        "outputSpeech": {
        "type": "PlainText",
        "text": "from python."
        }
        },
        "shouldEndSession": "%s"
        }
        }
        """ % (response, "true" if done else "false")
        return resp
    return error()

def error():
    return "I don't know how to do that", True

def skillcheck(skill=None):
    skills = dict(java=['Andrew Hanes'], python=['Shoyler', 'Andrew Hanes'], bash=['Matt Soucy'], lisp=['Bobby G'])
    if skill in skills and len(skills[skill]) > 0:
        if len(skills[skill]) > 1:
            name = skills[skill][0] + ' and ' + skills[skill][1] + " know " + skill
        else:
            name = skills[skill][0] + " knows " + skill
    else:
        name = 'no one'
    return name, True
    return resp

functions = dict(UserSearch=skillcheck, Error=error)
if __name__ == '__main__':
    app.run()
