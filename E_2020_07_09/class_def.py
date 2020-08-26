class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : {} \n나이 : {} \n".format(self.name, self.age))

    def __add__(self, other):
        self.age += other

    def __ge__(self, other): #크거나 같다
        if self.age >= other:
            return '성인입니다.'
        else:
            return '미 성년입니다.'

    def __bool__(self):
        if self.name == "이주현":
            return  True

        else:
            return False

s = Sample("이x현", 26)
# print(s)
# s+10
print(s>=19)

if s:
    print("이주현이 맞습니다.")
else:
    print("이주현이 아닙니다.")