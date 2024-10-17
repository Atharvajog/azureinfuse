import os
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return f"<html><body><h1>Flask Deployment Successful for CI/CD checking 2nd time</h1></body></html>\n"
 
@app.route("/env")
def show_env():
    env_var = os.getenv('ENV_VAR',None)
    return f"<html><body><h1>Environment Variable: {env_var}</h1></body></html>\n"
