# import "packages" from flask
from flask import Flask, render_template, request
from algorithm.image import image_data


# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("Home Page/index.html")


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


@app.route("/binary/", methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits), pic1= "../static/RiceTypes/Forbidden.PNG", pic2 = "../static/RiceTypes/BasmatiRice.PNG")
        # starting and empty input default
    return render_template("binary.html", bits=8, pic1="../static/RiceTypes/Forbidden.PNG", pic2="../static/RiceTypes/BasmatiRice.PNG")


@app.route('/tpt/', methods=['GET', 'POST'])
def tpt():
    # submit button has been pushed
    var1 = request.form.get("var1")
    var2 = request.form.get("var2")
    var3 = request.form.get("var3")
    var4 = request.form.get("var4")
    var5 = request.form.get("var5")
    var6 = request.form.get("var6")
    if var1 is not None:
        average = ((int(var1) + 3) + (int(var2) + 3) + (int(var3) + 3) + (int(var4) + 3) + (int(var5) + 3) + (int(var6) + 3)) / 6
    else:
        average = 'nothing'

    return render_template("tpt.html", var1=var1, var2=var2, var3=var3, var4=var4, var5=var5, var6=var6, average=average)


@app.route('/riceTypes/')
def ricetypes():
    return render_template("riceTypes.html")


@app.route('/Isaac', methods=['GET', 'POST'])
def isaac():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Isaac.html", name=name)
    # starting and empty input default
    return render_template("Isaac.html", name="World")


@app.route('/Erik', methods=['GET', 'POST'])
def erik():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Erik.html", name=name)
    # starting and empty input default
    return render_template("Erik.html", name="World")


@app.route('/Sahil', methods=['GET', 'POST'])
def sahil():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Sahil.html", name=name)
    # starting and empty input default
    return render_template("Sahil.html", name="World")


@app.route('/Yash', methods=['GET', 'POST'])
def yash():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Yash.html", name=name)
    # starting and empty input default
    return render_template("Yash.html", name="World")


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    return render_template("rgb.html", images=image_data())


@app.route('/binaryrgb/')
def binaryrgb():
    return render_template("binaryrgb.html")

@app.route('/binaryAddition/')
def binaryAddition():
    return render_template("binaryAddition.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)




