class Person():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    
    

class Student(Person):

    def __init__(self, firstname, lastname, subjectarea):
        super(Student, self).__init__(firstname, lastname)
        self.subjectarea = subjectarea

    def subjectarea(self):
        return self.subjectarea
    
    #def printNameSubject(self):
     #   return "%s %s, %s" % (self.firstname, self.lastname, self.subjectarea)
    

class Teacher(Person):

    def __init__(self, firstname, lastname, coursename):
        super(Teacher, self).__init__(firstname, lastname)
        self.coursename = coursename

    def coursename(self):
        return self.coursename
    
    def printNameSubject(self):
        return "%s %s, %s" % (self.firstname, self.lastname, self.coursename)   
    