class Student(object):
    pass

bart = Student()

print(Student)
print(bart)
bart.name = 'Bart Simpson'

print(bart.name)

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

def print_score(std):
    print('%s: %s' % (std.name, std.score))

bart = Student('dasda',1221)
bart.print_score()
bart.name = 'das'
bart.score = 111
print_score(bart)

