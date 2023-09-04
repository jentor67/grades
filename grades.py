#!/usr/bin/python3

#************----------------------------------------------*************

# class grades
class Grades():
    gradeList=[]
    maxPoints=-1


    # Dictionary of grades    
    gradeParametersDict = {
      "A": {
         "gradepoint": 4.0,
         "high": 100,
         "low": 90
      },
      "BA": {
         "gradepoint": 3.5 ,
         "high": 90,
         "low": 85 
      },
      "B": {
         "gradepoint": 3.0,
         "high": 85,
         "low": 80 
      },
      "CB": {
         "gradepoint": 2.5,
         "high": 80,
         "low": 75 
      },
      "C": {
         "gradepoint": 2.0,
         "high": 75,
         "low": 70 
      },
      "DC": {
         "gradepoint": 1.5,
         "high": 70,
         "low": 65 
      },
      "D": {
         "gradepoint": 1.0,
         "high": 65,
         "low": 60 
      },
      "E": {
         "gradepoint": 0.0,
         "high": 60,
         "low": 0 
      },
    }


    # initial welcome
    def __init__(self):
        print("Hello, Welcome to grade calculator")
        print("First, set the Maximum points for the tests")
        print("")


    # add grade to student list
    def addGrade(self,student):

        goodNumber = False
        while goodNumber == False :
            sStudent=student
            if( student == -1 ): sStudent=len(self.gradeList)+1 
            print("Put in a points for student " + 
                str(sStudent) + " or type 'q' to exit")
            grade = input()
            if grade == 'q' :
                print("Exiting")
                goodNumber = True
            elif grade.isdigit() == False :
                print("")
                print("***WARNING***")
                print("That is not a positive integer")
                print("")
            elif int(grade) > int(self.maxPoints) :
                print("")
                print("***WARNING***")
                print("Grade is over Max points")
                print("")
            else:
                if student == -1 : 
                    self.gradeList.append(grade)
                else:
                    self.gradeList[int(student)-1]= grade
                    goodNumber = True


    # format and print summary
    def calculateSummary(self):
        fail = False
        if self.maxPoints == -1 :
            print("No max poins given")
            fail = True
        
        if len(self.gradeList) == 0 :
            print("No grades given")
            fail = True

        if fail == False :
            print("")
            print("Summary")
            print("************************************")
            totalPoints=0
            i=1
            for x in self.gradeList :
                totalPoints += int(x)
                grade=int(x)/int(self.maxPoints)*100
                letterGrade, gradePoint = self.grade(grade)
                print("Student " + str(i) + " earned: " + 
                str(int(round(grade))) + "%," + letterGrade + "," 
                + str(gradePoint))  
                i += 1 
            grade=int(totalPoints/len(self.gradeList))/\
                int(self.maxPoints)*100
            letterGrade, gradePoint = self.grade(grade)
            print("")
            print("The class average was: " +  
            str(int(round(grade))) + "%," + letterGrade + "," 
            + str(gradePoint))  

            print("************************************")
            print("")


    # delete student
    def deleteStudent(self):
        self.reviewView()
        print("Which student point would you like to delete?")
        student = input()
        editPass = False
        while( editPass == False ): 
            if( student.isdigit() == False ): 
                print("This is not a positive integer")
            elif( (int(student)-1) >= len(self.gradeList) or 
                   int(student) == 0  ):
                print("Student number is out of range")
            else:
                editPass = True

            if( editPass == False ):
                print("Which student would you like to delete?")
                self.reviewView()
                student = input()
            else:
                print("")
                print("Delete student" + str(student))
                del self.gradeList[int(student)-1] 


    # deteremine which route to take from start of program
    def doSelection(self,n):
        if ( n == 0 ) :
            print("Good by")
        elif ( n == 2 ):
            if self.maxPoints == -1 :
                print("***WARNING***")
                print("Need to set a max points")
                print("")
            else:
                print("")
                self.addGrade(-1)
        elif ( n == 3 ):
            self.reviewView()
        elif ( n == 4 ):
            print("Calculate Summary")
            self.calculateSummary()
        elif ( n == 1 ):
            print("Maximum Points")
            self.maxPoints=self.setMaxPoints()
        elif ( n == 5 ):
            self.editPoints()
        elif ( n == 6 ):
            self.deleteStudent()
        else:
            print("wrong option try again")

        return(999)


    # edit points of student test 
    def editPoints(self):
        self.reviewView()
        print("Which student point would you like to edit?")
        student = input()
        editPass = False
        while( editPass == False ): 
            if( student.isdigit() == False ): 
                print("This is not a positive integer")
            elif( (int(student)-1) >= len(self.gradeList) or 
                   int(student) == 0  ):
                print("Student number is out of range")
            else:
                editPass = True

            if( editPass == False ):
                print("Which student point would you like to edit?")
                self.reviewView()
                student = input()
            else:
                print("")
                self.addGrade(student)

                
    # determine the letter grade and gradePoint from 
    # gradeParametersDict dictionary 
    def grade(self,points):
        for id, info in self.gradeParametersDict.items():
            grade=id
            gradePoint=info['gradepoint']
            high=info['high']
            low=info['low']
            if int(points) >= low :
                Grade=grade
                GP=gradePoint
                break

        return(Grade,GP)


    # start of class
    def grades(self):
        self.maxPoints = self.setMaxPoints()
 
        choice = 999 
        while choice > 0:
            print("")
            print("Please choose an option:")
            print("0. End")
            print("1. Reset Maximum Points")
            print("2. Add points for students")
            print("3. Review")
            print("4. Calculate Summary")
            print("5. Edit Student Points")
            print("6. Delete Student Points")
            choice = input()

            if( choice.isdigit() == True ):
                choice = int(choice)
                self.doSelection(choice)
            
            else:
                choice = 999
                print(" ")
                print("***Warning*** I don't understand your choice***")
                print(" ")

        return


    # review max points and student points
    def reviewView(self):
        print("")
        iStudent=1
        print("Maximum points: " + str(self.maxPoints))
        for x in self.gradeList :
            print("Student " + str(iStudent) + " points: " + str(x))
            iStudent += 1 

        print("")


    # set max points for a test
    def setMaxPoints(self):
        maxPoints=-1
             
        while maxPoints == -1 :
            print("What is the Maximum Points?")
            maxPoints=input() 
            if( maxPoints.isdigit() == False ):
                maxPoints=-1
                print("")
                print("***WARNING***")
                print("This is not a positive integer")
                print("")

        return(maxPoints)
                


gd = Grades() 


gd.grades()
