class Student():
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
s1 = Student('sai',101,90)
s2 = Student('buddi',102,95)
print('Student1:',s1.name,s1.rollno,s1.marks)
print('Student2:',s2.name,s2.rollno,s2.marks)