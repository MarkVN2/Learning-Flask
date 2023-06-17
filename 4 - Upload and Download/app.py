import os
from flask import Flask , request , render_template, redirect , flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'usercontent/uploads'
ALLOWED_EXTENSIONS = {'png','jpeg','jpg','gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '123'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET","POST"])
def index():
    if request.method =="POST":

        if 'file' not in request.files:
            flash('NO FILE PART')
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            flash("NO FILE HAS BEEN SELECTED")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        return redirect(url_for('files', name = filename))
    return render_template("index.html")

@app.route("/usercontet/uploads/<name>")
def files(name):
    return f'<a href="{name}" download = "{name}">Download Uploaded Image</a>' 