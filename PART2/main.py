from flask import Flask, render_template, request, redirect
import function
import datetime


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('main_page.html')


@app.route("/mentors", methods=["GET"])
def show_mentors_and_schools():
    '''Renders the List of all mentors with school and country'''
    mentors_and_schools = function.SQL_QUERY_show_mentors_and_schools()
    return render_template('mentors.html', table=mentors_and_schools)


@app.route("/mentors/school", methods=["GET"])
def show_one_schools_mentors():
    selected_school = function.SQL_QUERY_select_schools()
    return render_template('mentors.html', table=selected_school)


@app.route('/all-schools', methods=["GET"])
def show_all_schools():
    ''' Renders the List of all mentors with school and country, list include all the schools, even if there's no mentor yet!'''
    all_schools = function.SQL_QUERY_show_all_schools()
    return render_template('mentors.html', table=all_schools)


@app.route('/mentors-by-country', methods=["GET"])
def show_mentors_by_country():
    mentors_by_country = function.SQL_QUERY_show_mentors_by_country()
    return render_template('mentors.html', table=mentors_by_country)


@app.route('/mentors-by-country/country', methods=["GET"])
def show_one_country():
    select_one_country = function.SQL_QUERY_select_country()
    return render_template('mentors.html', table=select_one_country)


@app.route('/contacts', methods=["GET"])
def show_contacts():
    contacts = function.SQL_QUERY_show_contacts()
    return render_template('mentors.html', table=contacts)


@app.route('/applicants', methods=["GET"])
def show_applicants():
    applicants = function.SQL_QUERY_show_applicants()
    return render_template('applicants.html', table=applicants)


@app.route('/applicants/all', methods=["GET"])
def show_all_applicants():
    all_applicants = function.SQL_QUERY_show_all_applicants()
    return render_template('applicants.html', table=all_applicants)


@app.route('/applicants/select', methods=["POST"])
def show_select_applicants():
    year = request.form['year']
    month = request.form['month']
    day = request.form['day']
    print(year, month, day)
    print('ok')
    all_applicants = function.SQL_QUERY_show_select_applicants()
    return render_template('applicants.html', table=all_applicants)


@app.route('/applicants-and-mentors', methods=["GET"])
def show_applicants_and_mentors():
    applicants_and_mentors = function.SQL_QUERY_show_applicants_and_mentors()
    return render_template('applicants.html', table=applicants_and_mentors)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
