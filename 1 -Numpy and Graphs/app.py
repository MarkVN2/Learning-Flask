from flask import Flask, request ,render_template
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            #This could be done much more efficiently
            
            x1 = request.form.get("x1")
            y1 = request.form.get("y1")
            z1 = request.form.get("z1")

            x2 = request.form.get("x2")
            y2 = request.form.get("y2")
            z2 = request.form.get("z2")

            x3 = request.form.get("x3")
            y3 = request.form.get("y3")
            z3 = request.form.get("z3")

            x= np.array([x1, x2 , z1 ],dtype=float)
            y= np.array([y1 , y2 , z2],dtype=float)
            z= np.array([x3, y3, z3],dtype=float)
            
            #make graph
            ax = plt.figure().add_subplot(projection='3d')
            ax.plot(x,y,z)
            # save the graph as a png
            plt.savefig('static\images\graph.png')

            return render_template("index.html")
        except ValueError:
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/graph")
def graph():
        return render_template("graph.html")

@app.route("/test")
def test():
    return "test"
if __name__=='__main__':
    app.run()