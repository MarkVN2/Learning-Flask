from flask import Flask, request ,render_template
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        eixox1 = request.form.get("eixox1")
        eixox2 = request.form.get("eixox2")
        eixoy1 = request.form.get("eixoy1")
        eixoy2 = request.form.get("eixoy2")

        xaxis = np.array([eixox1, eixox2])
        yaxis = np.array([eixoy1 , eixoy2])

        plt.plot(xaxis, yaxis)
        plt.savefig('static\images\graph.png')
    return render_template("index.html")

@app.route("/graph")
def graph():
    return render_template("graph.html")

if __name__=='__main__':
    app.run()