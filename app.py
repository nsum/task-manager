import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# Create instance of flask
app = Flask(__name__)


# / refers to default route
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
