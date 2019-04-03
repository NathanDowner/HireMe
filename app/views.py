"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserForm, JobForm
from app.models import User, Job
from datetime import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/new-job', methods=["GET", "POST"])
def newJob():
    form = JobForm()
    if request.method == "POST" and form.validate_on_submit():
        #create a job object and add it to the database
        job = Job(
            request.form['jTitle'],
            request.form['jDesc'],
            request.form['category'],
            request.form['company'],
            request.form['jLoc'],
            datetime.now()
        )

        db.session.add(job)
        db.session.commit()
        flash('Job Added', 'success')
        return redirect(url_for("home"))
    return render_template('', form=form)

@app.route('/add-user', methods=["GET", "POST"])
def addUser():
    form = UserForm()
    if request.method =="POST" and form.validate_on_submit():
        #create a user object and add it to the database
        user = User(
            request.form['fname'],
            request.form['lname'],
            request.form['password'],
            request.form['telephone'],
            request.form['email'],
            datetime.now()
        )

        db.session.add(user)
        db.session.commit()
        flash("User Added", 'success')
        return redirect(url_for('home'))
    return render_template('', form=form)



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Nathan Downer")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
