"""Pet Adoption app"""

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thesecretekey898912"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)

    
def serialize_cupcake(cupcake):
    return {
        "id"     : cupcake.id,
        "flavor" : cupcake.flavor,
        "size"   : cupcake.size,
        "rating" : cupcake.rating,
        "image"  : cupcake.image,
    }


@app.route('/')
def home():
    return render_template('cupcakes.html')

# GET FULL LIST OF ALL CUPCAKES
@app.route('/api/cupcakes', methods=["GET"])
def get_cupcake_list():
    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]
    return jsonify(cupcakes=serialized)


# ADD A CUPCAKE
@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():

    flavor = request.json.get("flavor")
    size   = request.json.get("size")
    rating = request.json.get("rating")
    image  = request.json.get("image", "http://somefuckingimage.com")


    cupcake = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
    db.session.add(cupcake)
    db.session.commit()
    serialized= serialize_cupcake(cupcake)

    return (jsonify(cupcake=serialized),201)


# GET A SINGLE CUPCAKES DETAILS
@app.route('/api/cupcakes/<int:cupcake_id>', methods=["GET"])
def get_cupcake_detail(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)
    return jsonify(cupcake=serialized)
    



# EDIT A CUPCAKE
@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def edit_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    id = cupcake_id
    flavor = request.json.get("flavor", cupcake.flavor)
    size   = request.json.get("size"  , cupcake.size)
    rating = request.json.get("rating", cupcake.rating)
    image  = request.json.get("image" , "http://somefuckingimage.com")
    cupcake = Cupcake(id = id, flavor=flavor,size=size,rating=rating,image=image)
    db.session.commit()
    return jsonify(cupcake=serialize_cupcake(cupcake))


# DELETE CUPCAKE
@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
    
    








    
