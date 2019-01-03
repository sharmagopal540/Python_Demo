from flask import Flask, render_template

web1 = Flask(__name__)

@web1.route('/')

def data1():
    return render_template("home.html")

@web1.route('/about/')
def data2():
    return render_template("about.html")

if __name__ == "__main__":
    web1.run(debug=True)
