from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///insti.db"
db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String, nullable=False)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    return "Hello World"

@app.route('/<int:id>')
def get_resource(id):
    return "Item no " + str(id)

@app.route('/<string:id>')
def get_str_resource(id):
    return "Item: " + id

@app.route('/department/<int:id>',methods=['GET'])
def get_department(id):
    dept = Department.query.get_or_404(id)
    return dept.name

@app.route('/department',methods=['POST'])
def add_department():
    name = request.values['name']
    dept = Department()
    dept.name = name
    db.session.add(dept)
    db.session.commit()
    return "The id of the department is "+ str(dept.id)

@app.route('/department/<int:id>',methods=['PUT'])
def update_department(id):
    dept = Department.query.get_or_404(id)
    dept.name = request.values['name']
    db.session.add(dept)
    db.session.commit()
    return "Updated"

if __name__  == '__main__':
    db.create_all()
    app.run(debug=True)
