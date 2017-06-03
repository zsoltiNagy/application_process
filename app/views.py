from flask import render_template
from app import app
from db_handling import execute_sql_statement


@app.route('/')
def root():
    return render_template('base.html')


@app.route('/mentors')
def mentors_and_schools():
    '''
    On this page you should show the result of a query that returns the name of the
     mentors plus the name and country of the school (joining with the schools table)
     ordered by the mentors id column (columns: mentors.first_name, mentors.last_name,
     schools.name, schools.country).
    '''
    data_set = execute_sql_statement("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                        FROM mentors JOIN schools
                                        ON (mentors.city=schools.city)
                                        ORDER BY mentors.id;""")
    return render_template('table.html',
                           columns=['first_name', 'last_name', 'schools_name', 'country'],
                           data_set=data_set)


@app.route('/all-school')
def all_schools():
    '''
    On this page you should show the result of a query that returns the name of the
     mentors plus the name and country of the school (joining with the schools table)
     ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country
    '''
    data_set = execute_sql_statement("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                                        FROM mentors RIGHT JOIN schools
                                        ON (mentors.city=schools.city)
                                        ORDER BY mentors.id;""")
    return render_template('table.html',
                           columns=['First Name', 'Last Name', 'Schools Name', 'Country'],
                           data_set=data_set)


@app.route('/mentors-by-country')
def mentors_by_country():
    '''
    On this page you should show the result of a query that returns the number of the
     mentors per country ordered by the name of the countries
    columns: country, count
    '''
    data_set = execute_sql_statement("""SELECT COUNT(mentors.*), schools.country
                                        FROM mentors JOIN schools
                                        ON (mentors.city=schools.city)
                                        GROUP BY schools.country
                                        ORDER BY schools.country;""")
    return render_template('table.html',
                           columns=['Number of Mentors', 'Country'],
                           data_set=data_set)


@app.route('/contacts')
def contacts():
    '''
    On this page you should show the result of a query that returns the name of the
     school plus the name of contact person at the school (from the mentors table)
     ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name
    '''
    data_set = execute_sql_statement("""SELECT mentors.first_name, mentors.last_name, schools.name
                                        FROM mentors JOIN schools
                                        ON schools.contact_person=mentors.id;""")
    return render_template('table.html',
                           columns=['Schools Name', 'First Name', 'Last Name'],
                           data_set=data_set)


@app.route('/applicants')
def applicants():
    '''
    On this page you should show the result of a query that returns the first name
    and the code of the applicants plus the creation_date of the application
    (joining with the applicants_mentors table) ordered by the creation_date in
    descending order BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    '''
    data_set = execute_sql_statement("""SELECT applicants.first_name, applicants.application_code,
                                        applicants_mentors.creation_date
                                        FROM applicants JOIN applicants_mentors
                                        ON applicants.id=applicant_id
                                        WHERE creation_date >'2016-01-01'
                                        ORDER BY creation_date DESC;""")
    return render_template('table.html',
                           columns=['First Name', 'Application Code', 'Creation Date'],
                           data_set=data_set)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    '''
    On this page you should show the result of a query that returns the first name
    and the code of the applicants plus the name of the assigned mentor (joining
    through the applicants_mentors table) ordered by the applicants id column
    Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string 'None' instead of the mentor name
    columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name
    '''
    data_set = execute_sql_statement("""SELECT applicants.first_name, applicants.application_code, mentors.first_name
                                        FROM applicants
                                        LEFT JOIN applicants_mentors
                                        ON applicants.id=applicant_id
                                        LEFT JOIN mentors
                                        ON mentors.id=mentor_id
                                        ORDER BY applicants.id ASC;""")
    return render_template('table.html',
                           columns=['Applicant First Name', 'Application Code', 'First Name of the Assigned Mentor'],
                           data_set=data_set)
