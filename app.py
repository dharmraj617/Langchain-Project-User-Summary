from flask import Flask, request, render_template, jsonify
from langchain_app import langchain_app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = langchain_app(name=name)

    return jsonify(
        {"summary":person_info.summary,
         "facts": person_info.facts,
         "picture_url": profile_pic_url.picture_url
        }
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
