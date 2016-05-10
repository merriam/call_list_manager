from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return 'Hello World'


@app.route("/mock")
def show_mock():
  return render_template('/Users/charlesmerriam/p/call/html/call_list.html')


if __name__ == '__main__':
  app.run(debug=True)
