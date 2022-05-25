from flask import Flask, render_template
import gunicorn


app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name='user'):

   return f'hello {name}'


if __name__ == '__main__':
   app.run(debug = True)