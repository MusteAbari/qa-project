from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():  
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squared/<int:number>')
def squared(number):
    return f"{number} squared is {number**2}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")