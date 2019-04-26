#Michael McGill CSC2280 Final project 2019 michaelmcg52@gmail.com
#This is an original project. Any illegal or or accidental resemblance to other programs is coincidental.

#This project automatically calculates, assigns and completes a high school transcript based on the information given be the user.

#Explanetory print statement 
print('''Hello! And thank you for choosing Transcript Generator Pro. This program is designed to make it easy for you to produce a 
clean and profesional transcript with ease. For the generator to achieve the best results, you must enter course data and grades 
accurately.''')

#Gaining information from the user

#Student information 
def stud_info():
    print('''Your transcript will need to have up to date info. Please answer the follwing questions about the student.''')
    print()
    name = input("Student Name, first and last: ")
    bday = input("Birth date (mm/dd/yyyy): ")
    gender = input("Gender: ")
    guard = input("Parent or legal guardian's name, first and last: ")
    
    print('''
    __________________________________________________          
    |               Student Information                         
    |Full Name: ''', name ,'''                                  
    |Birdthday: ''', bday ,'''                             
    |Gender: ''', gender ,'''                              
    |Parent/Legal Guardian: ''', guard ,'''                                                                      
    --------------------------------------------------''')

#School information 
def school_info():
    print('''Please enter the following information about your student's school/institution. ''')
    print()
    name = input("School name: ")
    phone_num = input("Phone number: ")
    email = input("School email: ")

    print('''
    __________________________________________________          
    |               School Information                         
    |Name: ''', name ,'''                                  
    |Phone #: ''', phone_num ,'''                             
    |School email: ''', email ,'''                                                                                      
    --------------------------------------------------''')

#Function that organizes the information for each semester of school
def semester(year):
    course = "none"
    
    #Assign empty lists for user variables
    courselst = []
    gradelst = []
    cred_hourlst = []
    
    #Running total of credit hours and grades entered for GPA 
    total_cred = 0
    grade_num = []

    print('''Enter the different courses taken by your student during their''',year,'''year and the corresponding credit hours and grades 
    achieved. Press "Space" when all information has been entered.''')
    while(input != "done"):

        course = (input("Enter course title, or \"Space\" if finished: "))
    
        grade = input("Enter the grade earned in: ", course)
        
        #If-Elif for converting letter grade to GPA numbers
        if (grade).lower == "a":
            grade_num.append(4)
        elif (grade).lower == "b":
            grade_num.append(3)
        elif (grade).lower == "c":
            grade_num.append(2)
        elif (grade.lower) == "d":
            grade_num.append(1)
        elif (grade).lower == "f":
            grade_num.append(0)
        else:
            print("Please enter a letter from A-F")
        
        cred_hour = int(input("Enter credit hours earned: "))

        #Assign the variables to lists and keep adding to them
        courselst.append(course)
        gradelst.append(grade)
        cred_hourlst.append(cred_hour)
        temp = []
    for i in grade_num:
        temp[i] = grade_num[i] * cred_hourlst[i]
        temp2 = 0.0
    for i in range (len(temp)):
        temp2 += temp[i]
            
        total_cred += cred_hourlst[i]
    temp3 = [temp2/len(temp), total_cred]
    return temp3

def main():
    stud_info()
    school_info()
    cumu_gpa = []
    total_year_cred = []
    for i in range(4):  
        year = input("What year is the student: ")
        j = semester(year)
        cumu_gpa[i] = j[0]
        total_year_cred[i] = j[1]

main()

         