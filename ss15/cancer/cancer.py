from flask import *
import  mlab
from mongoengine import  *

app = Flask ( __name__ )

mlab.connect()
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
#     {
#         "image=" :"http://images6.fanpop.com/image/photos/35900000/-Thor-The-Dark-World-Premiere-in-London-kat-dennings-35910367-342-500.jpg",
#         "title":"Kat Dennings",
#         "age": 31,
#         "breast" :98,
#         "waist":64,
#         "hips": 92
#     },
#     {
#         "image=": "http://dantricdn.com/N3mzbxba5jSUn4MdTjkldQZ27zJuVH/Image/2015/03/an04031-c3ea9.jpg",
#         "title": "Angelina Jolie",
#         "age": 42,
#         "breast": 90,
#         "waist": 61,
#         "hips": 89
#     },
#     {
#         "image ": "http://baomoi-photo-1-td.zadn.vn/17/04/16/111/22029270/6_24198.jpg",
#         "title" :"Scarlett Johansson",
#         "age":  32,
#         "breast":99 ,
#         "waist": 62,
#         "hips":93
#
#     }
# ]
@app.route ( '/' )
def index():
    return render_template( "index.html",girls=Pain.objects() )
@app.route('/add_girl',methods=["GET"])

def add_flower():
    return render_template("add_girl.html")


if __name__ == '__main__':
    app.run ()
