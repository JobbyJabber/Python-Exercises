import reading_excel;
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/people")
def getAllPeople():
    people = reading_excel.readPeople()
    return jsonify(people)

@app.route('/people/<salary>/<gender>')
def getPersonBySalryAndGender(salary, gender):
    person = reading_excel.getPersonBySalryAndGender(salary, gender)
    return jsonify(person)
 
if __name__ == "__main__":
    app.run(debug=True)