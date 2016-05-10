from flask import Flask, render_template
from data import data as people

app = Flask(__name__)

@app.route("/")
def hello_world():
  return 'Hello World'


@app.route("/mock")
def show_mock():
  return render_template('call_list.html', people=people)


if __name__ == '__main__':
  app.run(debug=True)
