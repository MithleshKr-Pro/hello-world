import os
from flask import Flask
app = Flask(__name__)
app_version = "0.0.1"

@app.route("/")
def hello_world():
    return f"hello! This is version {app_version} of my application."

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=int(os.environ.get("PORT",8080)))    
