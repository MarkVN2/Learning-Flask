from flask import Flask, request ,render_template

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # grab A and B from the page
            a = int(request.form.get("a"))
            b = int(request.form.get("b"))
            #Make C equal to the result of the equation
            c = a + b  
            # With post we render the page and also send variable C to the page
            return render_template("index.html", c = c)
        except  ValueError:
            return render_template("index.html")
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run()