from StudentSchedular import StudentSchedular


stud = StudentSchedular()

class Admin:

    def showMenu(self):
        print("1. add student")
        print("2. show all students")
        print("3. exit")

        while(True):
            ch=input("Enter your choice")

            if ch=="1":
                self.acceptstudentdetails()
            elif ch=="2":
                self.showallstudentdetails()
            else:
                break;

    def acceptstudentdetails(self):
        rollno=int(input("Enter roll number"))
        name=input("Enter name")
        stud.addstudent(rollno,name)

    def showallstudentdetails(self):
        stud.showallstudents()


a = Admin()
a.showMenu()