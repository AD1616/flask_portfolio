# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers')
def hawkers():
    return render_template("hawkers.html")

@app.route('/Journals/')
def Journals():
    return render_template("Journals.html")


@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/brainWrite/')
def brainWrite():
    return render_template("brainWrite.html")

@app.route('/wireframes/')
def wireframes():
    return render_template("wireframes.html")

@app.route('/binary/')
def binary():
    return render_template("binary.html")

@app.route('/Isaac', methods=['GET', 'POST'])
def Isaac():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Isaac.html", name=name)
    # starting and empty input default
    return render_template("Isaac.html", name="World")

@app.route('/Erik', methods=['GET', 'POST'])
def Erik():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Erik.html", name=name)
    # starting and empty input default
    return render_template("Erik.html", name="World")

@app.route('/Sahil', methods=['GET', 'POST'])
def Sahil():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Sahil.html", name=name)
    # starting and empty input default
    return render_template("Sahil.html", name="World")

@app.route('/Yash', methods=['GET', 'POST'])
def Yash():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Yash.html", name=name)
    # starting and empty input default
    return render_template("Yash.html", name="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
