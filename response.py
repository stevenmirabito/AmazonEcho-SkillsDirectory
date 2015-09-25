__author__ = 'ahanes'


def initial(say):
    i = """
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
    "text": "%s"
    },
    "responsecard": {
    "type": "Simple",
    "title": "CSH Directory Application",
    "content": "%s"
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

    """ % (say, say)
    return i


def voice_response(say, end=False):
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
        """ %(say, "true" if end else "false")
    return resp

