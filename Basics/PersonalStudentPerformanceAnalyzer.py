#    1. Student Performance Analyzer

class InvalidMarks(Exception):
    pass

class Student:
    name = ""
    marks = []
    subjects = ["DS", "DBMS", "DSGT", "MATH", "JAVA"]
    def __init__(self):
        self.name = input("Enter Student Name: ")

        for i in range(5):
            try:
                self.marks.append(int(input(f"Enter {self.subjects[i]} marks: ")))
                if self.marks[i] > 100 or self.marks[i] < 0:
                    raise InvalidMarks("Marks must be in the range [0,100].")

            except ValueError:
                print("Please, Enter a valid number of marks")
                break
            except InvalidMarks as err:
                print(f"Error: {err}")
                break

    def total(self):
        total = 0
        for i in self.marks:
            total += i
        return total

    def avg(self):
        avg = self.total()/len(self.marks)
        return avg

    def percentage(self):
        percentage = self.total()/5
        return percentage

    def grade(self):
        per = self.percentage()
        grade = ''
        if 80 <= per <= 100:
            grade = 'A'
        elif 70 <= per < 80:
            grade = 'B'
        elif 60 <= per < 70:
            grade = 'C'
        elif 50 <= per < 60:
            grade = 'D'
        elif 40 <= per < 50:
            grade = 'E'
        elif per < 40:
            grade = 'F'
        else:
            grade = 'X'

        return grade

    
    def passOrFail(self):
        for ele in self.marks:
            if(ele < 40):
                self.result = 'Fail'
                break
            else:
                self.result = 'Pass'

        return self.result

    def displalyReportCard(self):
        print("\n---- Student Report Card ----")
        print(f"Student Name: {self.name}")
        print(f"Student Marks:")
        for i in range(5):
            print(f"{self.subjects[i]} - {self.marks[i]}")
        print(f"Status: {self.passOrFail()}")
        print(f"Total marks: {self.total()}/500")
        print(f"Student Percenrage: {self.percentage()}%")
        print(f"Student Grade: {self.grade()}")


try:
    student1 = Student()
    student1.displalyReportCard()
except ValueError as ve:
    pass
except IndexError as ie:
    pass

