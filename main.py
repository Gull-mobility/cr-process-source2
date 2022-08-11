import os
from flask import Flask
from markupsafe import escape

#Import to show date
from datetime import datetime

#Import all process
from process import execution

app = Flask(__name__)


@app.route("/<name>")
def param(name):

    #Execute process
    execution(name)

    #Print time
    date = datetime.now()
    
    return f"Tadk donde for id, {escape(name)} at {date}!"

@app.route("/hello/<name>")
def hello(name):
    execution(escape(name))
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))