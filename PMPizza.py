from flask import Flask, render_template, request

Pizza = Flask(__name__)

@Pizza.route('/')
def index():
    return render_template('pizzahome.html')

if __name__ == '__main__':
    Pizza.run(debug=True)
