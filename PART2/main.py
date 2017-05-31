from flask import Flask, render_template, request, redirect
import function
import datetime


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('main_page.html')


@app.route("/mentors")
def show_mentors_and_schools():
    '''Renders the LIst of all mentors with school and country'''
    mentors_and_schools = function.SQL_QUERY_show_mentors_and_schools()
    return render_template('table.html', table=mentors_and_schools)


@app.route('/ all-schools')
def show_all_schools():
    ''' Renders the List of all mentors with school and country, list include all the schools, even if there's no mentor yet!'''
    all_schools = function.SQL_QUERY_show_all_schools()
    return render_template('table.html', table=all_schools)


@app.route('/mentors-by-country')
def show_mentors_by_country():
    mentors_by_country = function.SQL_QUERY_show_mentors_by_country()
    return render_template('table.html', table=mentors_by_country)


@app.route('/contacts')
def show_contacts():
    contacts = function.SQL_QUERY_show_contacts()
    return render_template('table.html', table=contacts)


@app.route('/applicants')
def show_applicants():
    applicants = function.SQL_QUERY_show_applicants()
    return render_template('table.html', table=applicants)


@app.route('/applicants-and-mentors')
def show_applicants_and_mentors():
    applicants_and_mentors = function.SQL_QUERY_show_applicants_and_mentors()
    return render_template('table.html', table=applicants_and_mentors)


if __name__ == '__main__':
    app.run(debug=True)
