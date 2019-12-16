from app import app
from flask_script  import Manager
manager = Manager(app)
app.debug = True
app.run(debug = True,port=7777,host='0.0.0.0')
if __name__ == '__main__':
    manager.run()