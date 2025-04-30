from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__)


@app.route("/")
def home():
    # TODO: make proper home page
    return render_template("routes/home.html")


# TODO: make projects index

# TODO: make devlogs index


@app.route("/devlogs/")
def devlog_read():
    # TODO: read devlogs from directory passed as url-path argument
    return render_template(
        "routes/devlog-read.html",
        content=Markup("<h1>hello world</h1>"),
    )
