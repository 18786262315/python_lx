from flask import Flask,request
import logging

app = Flask(__name__)
# app.debug = True
handler = logging.FileHandler('app.log', encoding='UTF-8')

logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# @app.route('/')
def hello_world():
    r = request.args.getlist("f")
    print(str(r))
    app.logger.info("adwee")
    app.logger.ERROR("ads")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
