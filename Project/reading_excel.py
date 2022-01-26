import pandas as pd

def readPeople():
    df = pd.read_excel('D:\Python Exercises\Python-Exercises\Project\people.xls')
    people_names = df.values.tolist()
    return people_names

def getPersonBySalryAndGender(salary, gender):
    df = pd.read_excel('D:\Python Exercises\Python-Exercises\Project\people.xls')
    people_names = df.values.tolist()
    result = list(filter(lambda x: x[5] > int(salary) and x[2] == gender, people_names))
    return result
