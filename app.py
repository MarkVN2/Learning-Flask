from flask import Flask, request ,render_template
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        eixox1 = request.form.get("eixox1")
        eixoy1 = request.form.get("eixoy1")
        eixoz1 = request.form.get("eixoz1")

        eixox2 = request.form.get("eixox2")
        eixoy2 = request.form.get("eixoy2")
        eixoz2 = request.form.get("eixoz2")

        eixox3 = request.form.get("eixox3")
        eixoy3 = request.form.get("eixoy3")
        eixoz3 = request.form.get("eixoz3")

        x= np.array([eixox1, eixox2 , eixoz1 ],dtype=float)
        y= np.array([eixoy1 , eixoy2 , eixoz2],dtype=float)
        z= np.array([eixox3, eixoy3, eixoz3],dtype=float)
        ax = plt.figure().add_subplot(projection='3d')
        ax.plot(x,y,z)
        plt.savefig('static\images\graph.png')
        plt.show()
    return render_template("index.html")

@app.route("/graph")
def graph():
    return render_template("graph.html")

if __name__=='__main__':
    app.run()