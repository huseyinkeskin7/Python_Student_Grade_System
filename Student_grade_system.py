#Written by Hüseyin Berk Keskin
print("Written by Hüseyin Berk Keskin")

def calculate_grade(line):
    line = line[:-1]
    list = line.split(':')
    studentName = list[0]
    grades = list[1].split(',')

    grademidterm = int(grades[0])
    gradefinal = int(grades[1])

    mean = (grademidterm*4/10)+(gradefinal*6/10)
    if mean>=90:
        gradee = 'AA'
    elif mean>=85 and mean<=89.99:
        gradee = 'BA'
    elif mean>=84.99 and mean<=80:
        gradee = 'BB'
    elif mean>=79.99 and mean<=75:
        gradee = 'CB'
    elif mean>=74.99 and mean<=70:
        gradee = 'CC'
    elif mean>=69.99 and mean<=65:
        gradee = 'DC'
    elif mean>=64.99 and mean<=60:
        gradee = 'DD'
    elif mean>=50 and mean<=59.99:
        gradee = 'FD'
    elif mean<=49.99:
        gradee = 'FF'
    else:
        print("Error. You have entered wrong grade!")
    
    return studentName + ' ' + gradee + "\n"

def enter_grade():
    name = input('Student name: ')
    surname = input('Student surname: ')
    grademidterm = input('Midterm Grade: ')
    gradefinal = input('Final Grade: ')

    with open("grade_system.txt","a",encoding="utf-8") as file:
        file.write(name+''+surname+': '+grademidterm+','+gradefinal+'\n')

def view_grades():
    with open("grade_system.txt","r",encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))

def save_grades():
    with open("grade_system.txt","r",encoding="utf-8") as file:
        list1 = []
        for i in file:
            list1.append(calculate_grade(i))
        
    with open("grade_system.txt","w",encoding="utf-8") as file2: 
        for i in list1:
            file2.write(i)



while True:
    operation = input('1. View Grades\n2. Enter Grade\n3. Save Grades\n4. Exit\n---------->')
    if operation == '1':
        view_grades()
    elif operation == '2':
        enter_grade()
    elif operation == '3':
        save_grades()
    elif operation == '4':
        break
    else:
        print('Incorrect Choice. Please Try Again')
