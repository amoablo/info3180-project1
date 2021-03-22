"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.form import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
import os



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties')
def properties():
    query_lst = Property.query.all()
    return render_template("properties.html", query_lst = query_lst)

@app.route('/property/<propertyid>')
def getProperty(propertyid):
    query = Property.query.filter_by(id=propertyid).first()
    
    if query  is None:
        return redirect(url_for('home'))
    
    return render_template("property_view.html", query=query)

@app.route("/property", methods=["GET", "POST"])
def newProperty():
    form = PropertyForm()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data 
        bedRoom_number = form.bedRoom_number.data
        bathRoom_number = form.bathRoom_number.data
        location = form.location.data
        price = form.price.data
        property_type = form.property_type.data
        description = form.description.data
        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        pro = Property(title,bedRoom_number,bathRoom_number,location,price,property_type,description,filename)
        db.session.add(pro)
        db.session.commit()

        flash('Property Saved', 'success')
        return redirect('/properties')
    else:
        flash_errors(form)
    return render_template('property.html',form=form)


    
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/uploads/<filename>')
def get_image(filename):
    cd = os.getcwd()
    return send_from_directory(os.path.join(cd,app.config['UPLOAD_FOLDER']), filename)


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
    app.run(debug=True,host="0.0.0.0",port="8080")
