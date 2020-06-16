from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/champs")
def champs():
    return render_template('galery.html')

@app.route("/champs/aatrox")
def aatrox():
    return render_template('/champs/aatrox.html')

@app.route("/champs/anhri")
def anhri():
    return render_template('/champs/anhri.html')

@app.route("/champs/blintzcrank")
def blintzcrank():
    return render_template('/champs/blintzcrank.html')

@app.route("/champs/brand")
def brand():
    return render_template('/champs/brand.html')

@app.route("/champs/cassiopeia")
def cassiopeia():
    return render_template('/champs/cassiopeia.html')

@app.route("/champs/corki")
def corki():
    return render_template('/champs/corki.html')

@app.route("/champs/darius")
def darius():
    return render_template('/champs/darius.html')

@app.route("/champs/diana")
def diana():
    return render_template('/champs/diana.html')

@app.route("/champs/elise")
def elise():
    return render_template('/champs/elise.html')

@app.route("/champs/evelynn")
def evelynn():
    return render_template('/champs/evelynn.html')

@app.route("/champs/janna")
def janna():
    return render_template('/champs/janna.html')

@app.route("/champs/kayn")
def kayn():
    return render_template('/champs/kayn.html')

if __name__ == '__main__':
    app.run(debug=True)