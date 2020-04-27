from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pytz
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import products

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/lr_engine"
mongo = PyMongo(app)


def setup_cron(function):
    """Set up the cron job run my AP Scheduler"""
    sched = BackgroundScheduler()
    sched.add_job(function, 'interval', seconds=10)
    # sched.add_job(set_last_time_run, 'cron', hour=10, minute=25,
    #               timezone=pytz.timezone('US/Eastern'))
    sched.start()
    sched.print_jobs()


# last_time_run = ''


# def set_last_time_run():
#     global last_time_run
#     last_time_run = datetime.datetime.now()


 @app.route('/')
 def root():
     return 'hello'


if __name__ == "__main__":
    setup_cron(products.get_product_inventory)
    app.run()
