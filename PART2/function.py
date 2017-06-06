import psycopg2
from flask import request


def get_config():
    with open("config.txt") as config:
        config = config.readlines()
    return config


def database_connection(query):
    config = get_config()
    try:
        connect_str = "dbname={} user={} host='localhost' password={}".format(config[0], config[0], config[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(query)
        column_header = [desc[0] for desc in cur.description]
        table = cur.fetchall()
        table = (list(map(list, table)))
        column_head_upper = [x.upper() for x in [item for item in column_header]]
        table.insert(0, column_head_upper)
        return table
    except:
        print("I am unable to connect to the database")


def SQL_QUERY_show_mentors_and_schools():
    mentors_and_schools = """SELECT mentors.first_name, mentors.last_name, schools.name AS schools, schools.country
                    FROM mentors
                    LEFT JOIN schools ON mentors.city=schools.city
                    ORDER BY mentors.id"""
    return database_connection(str(mentors_and_schools))


def SQL_QUERY_select_schools():
    for key in request.args:
        condition = request.args.get(key)
    select_schools = """SELECT mentors.first_name, mentors.last_name, schools.name AS Schools, schools.country
                    FROM mentors
                    LEFT JOIN schools ON mentors.city=schools.city
                    WHERE schools.name = '{}'
                    ORDER BY mentors.id""".format(condition)
    return database_connection(str(select_schools))


def SQL_QUERY_select_country():
    for key in request.args:
        condition = request.args.get(key)
    select_country = """SELECT  schools.country, COUNT(mentors.id) AS Number_Of_Mentors
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.city=schools.city
                    WHERE country= '{}'
                    GROUP BY country
                   ;""".format(condition)
    return database_connection(str(select_country))


def SQL_QUERY_show_all_schools():
    all_schools = """SELECT mentors.first_name, mentors.last_name, schools.name As Schools, schools.country
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.city=schools.city
                    ORDER BY mentors.id"""
    return database_connection(str(all_schools))


def SQL_QUERY_show_mentors_by_country():
    mentors_by_country = """SELECT  schools.country, COUNT(mentors.id) AS Number_Of_Mentors
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.city=schools.city
                    GROUP BY country
                    ORDER BY country
                   ;"""
    return database_connection(str(mentors_by_country))


def SQL_QUERY_show_contacts():
    contacts = """SELECT   schools.name AS Schools, mentors.first_name, mentors.last_name
                    FROM mentors
                    INNER JOIN schools ON mentors.id=contact_person
                    ORDER BY name"""
    return database_connection(str(contacts))


def SQL_QUERY_show_applicants():
    applicants = """SELECT   applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants
                    LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    WHERE  creation_date >= make_date(2016,01,01)
                    ORDER BY creation_date DESC"""
    return database_connection(str(applicants))


def SQL_QUERY_show_all_applicants():
    applicants = """SELECT   applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants
                    LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    ORDER BY creation_date DESC"""
    return database_connection(str(applicants))


def SQL_QUERY_show_select_applicants():
    year = request.form['year']
    month = request.form['month']
    day = request.form['day']
    applicants = """SELECT   applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants
                    LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    WHERE  creation_date >= make_date({},{},{})
                    ORDER BY creation_date DESC""".format(year, month, day)
    return database_connection(str(applicants))


def SQL_QUERY_show_applicants_and_mentors():
    applicants_and_mentors = """SELECT   applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
                    FROM applicants
                    FULL OUTER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
                    ORDER BY applicants.id"""
    return database_connection(str(applicants_and_mentors))
