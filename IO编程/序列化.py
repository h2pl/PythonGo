import json

d = dict(name = 'Micheal', age = 27, score = 88)
jsonstr = json.dumps(d)
print(jsonstr)

print(json.loads(jsonstr))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {'name':std.name, 'age':std.age, 'score':std.score}

s = Student('Bob', 20, 88)
print(json.dumps(s, default = student2dict))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json.loads(jsonstr, object_hook = dict2student)

obj = {'name':'小明', 'age':27}
s = json.dumps(obj, ensure_ascii=False)
print(s)
