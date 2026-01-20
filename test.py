class Parent:
    def welcome(self):
        return "hello parent"


class Child(Parent):
    def welcome(self):
        return super().welcome() + "child here"

with open("questions.txt", "w") as f:
    f.write("Heloo")

with open("questions.txt", "r") as f:
    print(f.read())

numbers = [1,2,3,4]

add = map(lambda x: x+2, numbers)
pl = list(add)
print(pl)


even = list(filter(lambda x: x % 2 == 0, pl))

print(even)

list = [{"test1": "pretty"}]

child = Child()
print(child.welcome())