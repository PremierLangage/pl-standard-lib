# sandboxio.py
#
# Authors:
#   - Coumes Quentin <coumes.quentin@gmail.com>

import json
import sys

import jsonpickle

from components import Component



def get_answers() -> dict:
    """Return a dictionary containing every answer."""
    with open(sys.argv[1], "r") as f:
        answers = json.load(f)
    return answers



def get_context() -> dict:
    """Return the dictionary containing the context of the exercise."""
    with open(sys.argv[2], "r") as f:
        context = json.load(f)
    Component.sync_context(context)
    return context



def output(grade: int, feedback: str, context: dict):
    """Used to output the grade, feedback and context to the sandbox.
    
    Parameters:
        grade - (int) Grade of the student.
        feedback - (str) Feedback shown to the student.
        context - (dict) New context of the exercise."""
    with open(sys.argv[3], "w+") as f:
        f.write(jsonpickle.encode({
            "context":  context,
            "feedback": str(feedback),
            "grade":    int(grade),
        }, unpicklable=False))
