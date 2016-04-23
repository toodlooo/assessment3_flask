from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def app_form_page():
    """Show the application form page."""

    return render_template("application-form.html")


@app.route("/application", methods = ["POST"])
def collect_submission():
    """Receive the application details submitted"""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary_req = request.form.get("salary-req")
    job = request.form.get("job")

    return render_template("application-response.html",
    	first_name=first_name,
    	last_name=last_name,
    	salary_req=salary_req,
    	job=job.replace("-"," "))


    print first_name, last_name, salary_req, job


if __name__ == "__main__":
    app.run(debug=True)
