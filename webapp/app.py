from flask import Flask, render_template
from services.motors import Motors

app = Flask(__name__)
motors = Motors(23,24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes !'

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html',name=name)

@app.route('/forward')
def forward():
    motors.move_forward()
    return {"status":"Success","message":"Data recieved, moving forward"}

@app.route('/backward')
def backward():
    motors.move_backward()
    return {"status":"Success","message":"Data recieved, moving backward"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  