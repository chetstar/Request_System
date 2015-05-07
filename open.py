#!flask/bin/python
from app import app
if __name__ == '__main__':
    # app.config["SECRET_KEY"] = "ITSASECRET"
    # app.run(port=5000,debug=True)
    app.run(host='0.0.0.0', port=8080)
# do not forget to make your script executable chmod a+x run.py		
