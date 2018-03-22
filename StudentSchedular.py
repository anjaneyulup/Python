from bean import Student


students = {}

class StudentSchedular:

    def addstudent(self,rollno,name):
        s=Student()
        s.setrollno(rollno)
        s.setname(name)
        students.update({rollno:s})

    def showallstudents(self):
        for rollno in students.keys():
            student=students[rollno]
            print(student.getrollno())
            print(student.getname())