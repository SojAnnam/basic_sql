import psycopg2
from flask import request


def get_config():
    with open("config.txt") as config:
        config = config.readlines()
    return config


def if_request_get(query):
    config = get_config()
    try:
        connect_str = "dbname={} user={} host='localhost' password={}".format(config[0], config[0], config[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute(query)
    table = cur.fetchall()
    table = (list(map(list, table)))
    return table


def if_request_post(query):
    config = get_config()
    try:
        connect_str = "dbname={} user={} host='localhost' password={}".format(config[0], config[0], config[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute(query)
    conn.close()
    return None


def SQL_QUERY_show_mentors_and_schools():
    mentors_and_schools = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                    LEFT JOIN schools ON mentors.city=schools.city
                    ORDER BY mentors.id"""
    return if_request_get(str(mentors_and_schools))


def SQL_QUERY_show_all_schools():
    all_schools = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.city=schools.city
                    ORDER BY mentors.id"""
    return if_request_get(str(all_schools))


def SQL_QUERY_show_mentors_by_country():
    mentors_by_country = """SELECT  schools.country, COUNT(mentors.id) AS NumberOfMentors 
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.city=schools.city
                    GROUP BY country
                    ORDER BY country
                   ;"""
    return if_request_get(str(mentors_by_country))


def SQL_QUERY_show_contacts():
    contacts = """SELECT   schools.name, mentors.first_name, mentors.last_name 
                    FROM mentors
                    INNER JOIN schools ON mentors.id=contact_person
                    ORDER BY name"""
    return if_request_get(str(contacts))


def SQL_QUERY_show_applicants():
    applicants = """SELECT   applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants
                    LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    WHERE  creation_date   > make_date(2016,01,01)
                    ORDER BY creation_date DESC"""
    return if_request_get(str(applicants))


def SQL_QUERY_show_applicants_and_mentors():
    applicants_and_mentors = """SELECT   applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
                    FROM applicants
                    FULL OUTER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
                    ORDER BY applicants.id"""
    return if_request_get(str(applicants_and_mentors))
