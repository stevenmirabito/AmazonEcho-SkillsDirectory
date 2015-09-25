from random import shuffle
"""
Skills echo tool
"""
__author__ = 'ahanes'
import json
def skillcheck(skill=None):
    skills = json.loads(open('skills.pickle').read())
    if skill in skills and len(skills[skill]) > 0:
        shuffle(skills[skill])
        if len(skills[skill]) > 1:
            name = skills[skill][0] + ' and ' + skills[skill][1] + " know " + skill
        else:
            name = skills[skill][0] + " knows " + skill
    else:
        name = 'no one'
    return name, True
