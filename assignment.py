#! Python3

# general param definition
# every class duration is set for 2h long
# every class is only available from monday to saturday.

weekdays = ["mon", "tue", "wed", "thu", "fri", "sat"]
hours = [8, 10, 12, 14, 16, 18, 20]
    
    
class Course:

    def __init__(self, name, day, hour, maximum):
        self.name = name
        self.maximum = maximum
        self.room = None
        self.prof = None
        self.studs = list()
        self.lists = list()
    

        self.lists.append([name, day, hour, max, self.room, self.prof, self.studs ])

    def add(self, course, prof=False, stud=False, room=False):
            
            if prof == True:
                self.lists[5] = input("Insert the professor's name")
            elif room == True:
                self.lists[4] = input(int("Insert the room's number: "))
            elif stud == True:
                #check maximum capacity
                if len(self.studs) >= self.maximum:
                    print('Course full, unavailable')
                student = input("Insert the student's name")
                self.lists[6].append(student)

    def listing(self):
        print(f'Here are the {self.__class__.__name__} list:')
        print(25*'')
        for i in self.lists:
            print(i[0])

    def exclude(self, exclusion):
        for i in self.lists:
            if i[0] == exclusion:
                self.listing.remove(i)

    def make_changes(self):
        pass

    def add(self):
        pass

    def unadd(self):
        pass
    

class Professor(Course):

    def __init__(self, name):
        super().__init__(self)
        self.lists = list()
        self.course = None
        self.room = None
        self.studs = None
        self.day = None
        self.hour = None

        self.lists.append([self.name, self.course, self.room, self.studs, self.day, self.hour])
    


class Student(Course):
    pass

class Room(Course):
    pass


def main():
    #while True:
    #   print("Menu:")
    pass
        

if __name__ == '__main__':
    main()





        
        









'''


# Create class "Student"
class Student:
    # Constructor
    def __init__(self, name, disciplins, timetable,2):
        self.name = name
        self.desiciplins = disciplins
        self.m1 = m1
        self.m2 = m2
         
    # Function to create and append new student   
    def accept(self, Name, Rollno, marks1, marks2 ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2 )
        ls.append(ob)
  
    # Function to display student details     
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("Marks1 : ", ob.m1)
            print("Marks2 : ", ob.m2)
            print("\n")    
         
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
  
    # Delete Function                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    # Update Function   
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;
        '''