import sys
from flask import Flask
from sklearn.linear_model import HuberRegressor
from housing.exception import HousingException
from housing.logger import logging

app = Flask(__name__)

@app.route("/",methods=('GET','POST'))
def index():
    try:
        raise Exception("We're testing custom exception")
    except Exception as e:
        housing= HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We're testing logging module")
    return "This is my first fully deployment setup project"

if __name__=="__main__":
    app.run(debug=True)
