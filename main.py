from flask import Flask,request,render_template, redirect, url_for,flash
import pickle
import requests
from werkzeug.utils import secure_filename
import os

#login validation
def login_check(user,password):
    url = "http://localhost:8000/login"
    _data = {"username": user,"password": password}
    x = requests.post(url, json = _data)

    return x.json()['status']

#setting the upload folder in local
UPLOAD_FOLDER = "uploads"
#allowed extensions for the file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#check for the allowed file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


#Login page route
@app.route('/')
def hello_world():
    return render_template("login2.html")


#Home page route
@app.route('/form_login',methods=['POST'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    
    
    if login_check(name1,pwd):
        # def upload_file():
        #     if request.method == 'POST':
        #              # check if the post request has the file part
        #         if 'file' not in request.files:
        #             flash('No file part')
        #             return redirect(request.url)
        #         file = request.files['file']
        #         # if user does not select file, browser also
        #         # submit an empty part without filename
        #         if file.filename == '':
        #             flash('No selected file')
        #             return redirect(request.url)
        #         if file and allowed_file(file.filename):
        #             filename = secure_filename(file.filename)
        #             file.save(os.path.join(UPLOAD_FOLDER, filename))
        #             return redirect(url_for('uploaded_file',
        #                             filename=filename))

        return render_template('home.html',name=name1)
    else:
        return render_template('login2.html',info='Invalid Data')


#Upload success page
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload_status.html',status='No file part')
            
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('upload_status.html',status='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return render_template('upload_status.html',status='File uploaded successfully')
   #if request.method == 'POST':
      #f = request.files['file']
      #filename= secure_filename(f.filename)
      #f.save(os.path.join(UPLOAD_FOLDER, filename))
      #return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()
