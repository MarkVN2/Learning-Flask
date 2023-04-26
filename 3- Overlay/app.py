from flask import Flask, request ,render_template

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":

        state = str(request.form.get("activate"))

        if state == 'on':
            return render_template("index.html", display = 'display : block;')
        else:
            return render_template("index.html")
    else:
        # if no POST method is requested render only the page.
        return render_template("index.html")

if __name__=='__main__':
    app.run()