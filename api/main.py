from flask import Flask, render_template, url_for
from api.utils import list_dirs_from_dir, list_files_from_dir
from os.path import join


app = Flask(__name__)
app.debug = True
DEVLOGS_DIR = join("api", "templates", "devlogs")


@app.route("/")
def home():
    # TODO: make proper home page
    return render_template(
        "routes/home.html",
        page_name="home",
    )


@app.route("/projects/")
def projects_index():
    projects = list_dirs_from_dir(DEVLOGS_DIR)
    return render_template(
        "routes/index_of.html",
        items=projects,
        title="My Projects",
        page_name="projects",
    )


@app.route("/projects/<project_name>/")
def devlogs_index(project_name: str):
    project_dir = join(DEVLOGS_DIR, project_name)
    files = list_files_from_dir(project_dir)
    project_name = project_name.replace("-", " ").title()

    return render_template(
        "routes/index_of.html",
        items=files,
        title=project_name,
        page_name=project_name.lower(),
    )


@app.route("/projects/<project_name>/<devlog_name>")
def devlog_read(project_name: str, devlog_name: str):
    devlog_file_path = join("devlogs", project_name, devlog_name + ".html")
    devlog_index_path = url_for("devlogs_index", project_name=project_name)

    return render_template(
        devlog_file_path,
        index_page=devlog_index_path,
        project_name=project_name.replace("-", " ").lower(),
        page_name=devlog_name.lower(),
    )
