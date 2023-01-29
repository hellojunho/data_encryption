from flask import Flask
from flask.templating import render_template
from list import *

app = Flask(__name__)


@app.route('/')
def emp():
    empList = list().getEmps()
    return render_template("emp01.html", empList=empList)


if __name__ == "__main__":
    app.run(debug=True)
