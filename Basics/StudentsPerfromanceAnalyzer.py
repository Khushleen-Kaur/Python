#  1. Student Course & Performance Analyzer
students = {}
courses = {"Python", "Java", "React", "Math", "Biology", "English"}
class Student:
    def __init__(self,name,student_id,course):
        self.name = name
        self.student_id = student_id
        self.course = course
        students[student_id] = self
        self.avg()


    def __str__(self):
        return f"Name: {self.name}, Student_id: {self.student_id}"
    def __repr__(self):
        return self.__str__()

    def avg(self):
        total = 0
        for i in self.course:
            total += self.course[i]
        self.avg =  total /  len(self.course) if self.course else 0
        return self.avg


def addStudent(name, student_id, course):
    s = Student(name,student_id, course)

def highestScoring():
    top = {}
    for i in courses:
        max_marks = 0
        name = ''
        for k in students:
            if i in students[k].course and students[k].course[i] > max_marks:
                max_marks = students[k].course[i]
                name = students[k].name
        top[i] = (name, max_marks)

    for i in top:
        print(f"{i} : {top[i]}")
    return top

def topPerforming():
    top = students[1507001]
    for i in students:
        if students[i].avg > top.avg:
            top = students[i]

    return f" ---- Topper Student ---- \nName - {top.name} \nMarks - {top.avg}%"

def findStudent(course1, course2):
    print(f"Students enrolled in {course1} and {course2}:")
    for i in students:
        if course1 in students[i].course and course2 in students[i].course:
            print(students[i].name)

def studentCourses():
    for i in courses:
        print(f"\n--- {i} ---")
        for k in students:
            if i in students[k].course:
                print(students[k].name, students[k].course[i])

def getRollName():
    rollNameSet = set()
    for i in students:
        n = (students[i].name, i)
        rollNameSet.add(n)

    return rollNameSet

def getSubjectDetails():
    for i in courses:
        print(f"\n ---- {i} ----")
        total = 0
        count = 0
        top = None
        for k in students:
            if(i in students[k].course):
                print(students[k].name, students[k].course[i])
                total += students[k].course[i]
                count += 1
                if top is None or students[top].course[i] < students[k].course[i]:
                    top = k
        print(f"Topper: {students[top].name} - {students[top].course[i]}")
        if count > 0:
            print(f"Average marks: {total / count}")
        else:
            print("Average marks: No students enrolled")
        

def getOneSubjectDetails(course):
    print(f"\n ---- {course} ----")
    total = 0
    count = 0
    top = None
    for k in students:
        if(course in students[k].course):
            print(students[k].name, students[k].course[course])
            total += students[k].course[course]
            count += 1
            if top is None or students[top].course[course] < students[k].course[course]:
                top = k
    print(f"Topper: {students[top].name} - {students[top].course[course]}")
    if count > 0:
        print(f"Average marks: {total / count}")
    else:
        print("Average marks: No students enrolled")
    
def menu():
    while(True):
        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Highest Score")
        print("4. Top Performing")
        print("5. Highest Scorer in Course")
        print("6. Unique Courses")
        print("7. Find Students in two Courses")
        print("8. Student_id and Name")
        print("9. One Subject detail")
        print("10. Exit")
        choice = int(input("Enter Choice: "))

        match(choice):
            case 1:
                name = input("Enter Name: ")
                si = int(input("Enter Student_id: "))
                c = {}
                for i in range(3):
                    course_name = input(f"Enter course {i} name: ")
                    course_marks = int(input(f"Enter course {i} marks: "))
                    c[course_name] = course_marks
                addStudent(name, si, c)
                print("Student Added Successfully")
            case 2:
                for i in students:
                    print(f"{i} - {students[i].name}")
            case 3:
                highestScoring()
            case 4:
                print(topPerforming())
            case 5:
                getSubjectDetails()
            case 6:
                for i in courses:
                    print(i)
            case 7:
                findStudent(input("Enter Course 1: "), input("Enter Course 2: "))
            case 8:
                getRollName()
            case 9:
                getOneSubjectDetails(input("Enter course name: "))
            case 10: 
                print("Come Again!")
                break
            case _ :
                print("Enter a Valid choice!")
        

            


addStudent("Khushleen", 1507001, {'Python': 98, 'Java': 99, 'Math': 100})
addStudent("Gopikrishna", 1507002, {'Python': 99, 'Java': 100, 'React': 100})
addStudent("Maya", 1507003, {'Python': 39, 'Math': 55, 'English': 87})
addStudent("Varun", 1507004, {'Biology': 60, 'Math': 51, 'React': 95})

menu()