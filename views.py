from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name = "Marx", age = "19", altura = "1.75")

@views.route("/profile")
def profile(username):
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=username,)

@views.route("/json")
def get_json():
    return jsonify({"name": "Marx", "coolness": "19"})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/vai-para-casa")
def vai_para_casa():
    return redirect(url_for("views.home"))