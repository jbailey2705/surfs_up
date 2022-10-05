from flask import Flask
app = Flask(__name__)
@app.route('/')
def Hello_World():
    return 'Hello World'

# for the above code, in terminal use ~ export FLASK_APP=app.py (enter) then flask run

# if you use the below code you will need to add the following to terminal ~ python app.py
if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/

