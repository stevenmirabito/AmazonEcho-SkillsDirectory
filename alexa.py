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
"content": "I can count to five."
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

skills = dict(java=['Andrew Hanes'], python=['Shoyler', 'Andrew Hanes'], bash=['Matt Soucy'], lisp=['Bobby G'])

@app.route('/get/', methods=['GET', 'POST'])
def directory():
    data = request.json
    if (data['request']['type'] == 'LaunchRequest'):
        return initial
    print(data)
    #first = (data['request']['intent']['slots']['first']['value'])
    #last = (data['request']['intent']['slots']['last']['value'])
    skill = (data['request']['intent']['slots']['skill']['value']).lower()
    name = 'no one'
    if skill in skills and len(skills[skill]) > 0:
        if len(skills[skill]) > 1:
            name = skills[skill][0] + ' and ' + skills[skill][1]
        else:
            name = skills[skill][0]
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
    "text": "%s knows %s"
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
    "shouldEndSession": "true"
    }
    }
    """ % (name, skill)
    return resp

if __name__ == '__main__':
    app.run()
