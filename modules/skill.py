"""
Skills echo tool
"""
__author__ = 'ahanes'


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
