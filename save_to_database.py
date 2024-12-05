import sqlite3


def create_database():
    connection = sqlite3.connect('parsed_data.db')
    cursor = connection.cursor()

    cursor.execute('''
            DROP TABLE IF EXISTS courses
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT,
            describe_course TEXT
        )
    ''')

    connection.commit()
    connection.close()


def save_to_database(course_name, describe_course):
    connection = sqlite3.connect('parsed_data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO courses (course_name, describe_course) VALUES (?, ?)', (course_name, describe_course))

    connection.commit()
    connection.close()
