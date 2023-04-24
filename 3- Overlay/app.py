from flask import Flask, request ,render_template

app = Flask(__name__)

#TODO make the README.md for this exercise for better explanation

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":

        state = str(request.form.get("activate"))

        if state == 'on':
            return render_template("index.html", display = 'display : block;')
        else:
            return render_template("index.html", display = 'display : none;')
    else:
        # if no POST method is requested render only the page.
        return render_template("index.html" , display = 'display : none;')

if __name__=='__main__':
    app.run()