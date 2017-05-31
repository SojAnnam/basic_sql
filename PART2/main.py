from flask import Flask, render_template, request, redirect
import function
import datetime


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('main_page.html')


@app.route("/mentors")
def show_mentors_and_schools():
    '''Renders the LIst of mentors with school and country'''
    mentors_and_schools = SQL_QUERY_show_mentors_and_schools()
    return render_template('table.html', table=mentors_and_schools)


@app.route('/ all-schools')
def show_all_schools():


@app.route('/mentors-by-country')
def show_mentors_by_country():


@app.route('/contacts')
def show_contacts():


@app.route('/applicants')
def show_applicants():


@app.route('/applicants-and-mentors')
def show_applicants_and_mentors():


if __name__ == '__main__':
    app.run()