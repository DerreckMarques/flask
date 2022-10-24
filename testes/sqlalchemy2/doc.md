https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

pip3 install Flask Flask-SQLAlchemy
sqlite3.exe testes.db

Note:

If you want to use another database engine such as PostgreSQL or MySQL, you’ll need to use the proper URI.

For PostgreSQL, use the following format:

postgresql://username:password@host:port/database_name
For MySQL:

mysql://username:password@host:port/database_name



Creating the Database

export FLASK_APP=app
flask shell

from app import db, Student
db.create_all()

Note:

The db.create_all() function does not recreate or update a table if it already exists. For example, if you modify your model by adding a new column, and run the db.create_all() function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the db.drop_all() function and then recreate them with the db.create_all() function like so:

db.drop_all()
db.create_all()
This will apply the modifications you make to your models, but will also delete all the existing data in the database. To update the database and preserve existing data, you’ll need to use schema migration, which allows you to modify your tables and preserve data. You can use the Flask-Migrate extension to perform SQLAlchemy schema migrations through the Flask command-line interface.


student_john = Student(firstname='john', lastname='doe',
                       email='jd@example.com', age=23,
                       bio='Biology student')

print(student_john.id)

db.session.add(student_john)

db.session.commit()

print(student_john.id)

You can also use the db.session.add() method to edit an item in the database. For example, you can modify the student’s email like so:

student_john.email = 'john_doe@example.com'
db.session.add(student_john)
db.session.commit()

