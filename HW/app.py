from flask import Flask
from fibonacci import func_fib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'There are the Fibonacci numbers:'

@app.route('/<int:NumberOfNumbers>')
def num(NumberOfNumbers):
    b = func_fib()
    fib_numbers = [next(b) for i in range(NumberOfNumbers)]
    return fib_numbers

if __name__ == "__main__":
    app.run(debug=True)
