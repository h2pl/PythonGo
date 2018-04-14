print(type('str'))

# 使用isinstance()
#
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
#
# 我们回顾上次的例子，如果继承关系是：
#
# object -> Animal -> Dog -> Husky


class Animal:
    pass


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Rabbit(Animal):
    pass

a = Animal()
b = Tortoise()
c = Rabbit()

print(isinstance(a,Rabbit))
print(isinstance(b,Animal))
print(isinstance(c,object))


# 一个正确的用法的例子如下：

def readimage(fp):
    if hasattr(fp, 'read'):
        return readimage(fp)
    return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#
# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

print(dir(Rabbit))
print(dir('das'))