from flask import *
import  mlab
from mongoengine import  *
import os
from werkzeug.utils import secure_filename

app = Flask ( __name__ )

mlab.connect()
app.config["IMG_PATH"]=os.path.join(app.root_path,"images")
app.secret_key = "sgd4t4t"



class Pain(Document):
    image = StringField()
    name = StringField()
    age  = IntField()
    breast = FloatField()
    waist = FloatField()
    hips = FloatField()
pain = Pain(image="http://www.themovienetwork.com/sites/themovienetwork.com/files/u261/scarlet-witch-elizabeth-olsen.jpg",
            name="6 Elizabeth Olsent",
            age =28,
            breast=91,
            waist=60,
            hips = 95)
# pain.save()

@app.route ( '/' )
def index():
    return render_template( "index.html",girls=Pain.objects() )

@app.route("/images/<image_name>")
def image(image_name):
    return send_from_directory(app.config["IMG_PATH"],image_name)

@app.route("/logout")
def logout():
    session["logged_in"]= False
    return redirect(url_for("login"))






@app.route("/login",methods=["GET","POST"])
def login():
    Account = [
        {
        "name": "na",
        "pass": "na"
         },
        {
         "name":"ma",
         "pass":"ma"
        }
               ]
    if request.method=="GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        for account in Account :
            if username == account["name"] and password == account["pass"]:
                session["logged_in"]= True
                return  redirect(url_for("index"))

        return  "Invalid credentials"


@app.route('/add_girl',methods=["GET","POST"])
def add_girl():
    if "logged_in" in session and session["logged_in"]:
        if request.method=="GET":#FORM requested
            return render_template("add_girl.html")
        elif request.method=="POST":#user submited FORM
            #1 get data
            form= request.form
            name = form["title"]
            age = form["age"]
            breast= form["breast"]
            waist = form["waist"]
            hips= form["hips"]
            image = request.files["image"]
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMG_PATH"],filename))


            #2 save data()
            new_girl = Pain(name=name,
                            image="/images/{0}.".format(filename),
                            age=age,
                            breast=breast,
                            waist=waist,
                            hips=hips)
            new_girl.save()
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))
if __name__ == '__main__':
    app.run ()
