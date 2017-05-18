import psycopg2


def select_name(cur):
    cur.execute("SELECT first_name,last_name from mentors")
    rows = cur.fetchall()
    mentors_name = []
    for row in rows:
        mentors_name.append([row[0], row[1]])
    return mentors_name


def miskolc_nick_name(cur):
    cur.execute("SELECT nick_name FROM mentors WHERE city='Miskolc'")
    rows = cur.fetchall()
    nick_name_miskolc = []
    for row in rows:
        nick_name_miskolc.append([row[0]])
    return nick_name_miskolc


def find_carol(cur, conn):
    cur.execute("UPDATE applicants SET full_name = first_name ||' '|| last_name ")
    conn.commit()
    cur.execute("SELECT full_name,phone_number FROM applicants WHERE first_name='Carol'")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])


def find_hat_girl(cur, conn):
    cur.execute("UPDATE applicants SET full_name = first_name ||' '|| last_name ")
    conn.commit()
    cur.execute("SELECT full_name,phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])


def new_applicant_data(cur, conn):
    cur.execute("INSERT INTO applicants (first_name,last_name, phone_number,email,application_code) SELECT * FROM (SELECT 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com',54823) AS tmp WHERE NOT EXISTS (SELECT application_code FROM applicants WHERE application_code = 54823) LIMIT 1")
    conn.commit()
    cur.execute("SELECT * FROM applicants WHERE application_code='54823'")
    rows = cur.fetchall()
    for row in rows:
        print(row[1], row[2], row[3], row[4], row[5])


def change_phone_number(cur, conn):
    cur.execute("UPDATE applicants SET phone_number='003670/223-7459' WHERE last_name='Foreman'")
    conn.commit()
    cur.execute("SELECT * FROM applicants WHERE last_name='Foreman'")
    rows = cur.fetchall()
    for row in rows:
        print(row[1], row[2], row[3], row[4], row[5])


def delete_applicant(cur, conn):
    cur.execute("DELETE FROM applicants WHERE email LIKE '%mauriseu.net'")
    conn.commit()
    cur.execute("SELECT * FROM applicants")
    rows = cur.fetchall()
    for row in rows:
        print(row[1], row[2], row[3], row[4], row[5])


def database_connection(some_function):
    conn = psycopg2.connect(database="potyi", user="potyi", password="joinme9", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    try:
        result = some_function(cur, conn)
    except TypeError:
        result = some_function(cur)
    conn.close()
    return result


if __name__ == '__main__':
    database_connection(select_name)
