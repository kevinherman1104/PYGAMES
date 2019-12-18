import string
def newStaff():
    print("NewStaff")
    global id
    global name
    global position
    global position_available
    global salary
    id = input("Input ID[SXXXX] = ")
    print(id.casefold())
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for element in id:
        if element != "S" and element not in numbers:
            print("WRONG SYNTAX!")
            print(id.casefold())
        else:
            total_id.append(id)
            pass
    
    name = input("Input Name[0...20] = ")
    print(name)
    char_name = name.count(string.ascii_letters)
    if char_name > 20:
        print("TOO LONG!")
        print(name)
    else:
        total_name.append(name)
        total_name.sorted()
        pass

    position = input("Input Position [Staff|Officer|Manager] =  ")
    position_available = ["Staff","Officer","Manager"]
    print(position)
    if position not in position_available:
        print(position)
    else:
        total_position.append
        pass
    salary = input(int("Input Salary for "  + position + "= "))
    print(salary)
    if position == position_available[0]:
        if salary >= 3500000 or salary<= 7000000:
            total_salary_staff.append(salary)
    if position == position_available[1]:
        if salary >= 7000000 or salary<= 10000000:
            total_salary_officer.append(salary)
    if position == position_available[2]:
        if salary > 10000000
            total_salary_manager.append(salary)
    for elements in total_salary_manager:
        total_salary.append(elements)
    for elements1 in total_salary_officer:
        total_salary.append(elements1)
    for elements2 in total_salary_staff:
        total_salary.append(elements2)
    
def deleteStaff():
    print("Delete Staff")
    print(id.casefold())
    if id not in total_id:
        print("Data not Found")
    else:
        a = total_id[total_id.index(id)]
        del a
        for elements in total_name:
            del total_name[total_id.index(id)]
        for elements in total_position:
            del total_position[total_id.index(id)]
        for elements in total_salary:
            del total_salary[total_id.index(id)]




def viewSummaryData():
    if data[2] == position_available[0]:
        print("1." + position_available[0])
        maximum = max(total_salary_staff)
        print("maximum salary = ",maximum)
        minimum = min(total_salary_staff)
        total1 = 0
        for salaries in total_salary_staff:
            total1 += salaries
        average = total1 / len(total_salary_staff)
        print("average salary = ",average)
    if data[2] == position_available[1]:
        print("2." + position_available[1])
        maximum = max(total_salary_officer)
        print("maximum salary = ",maximum)
        minimum = min(total_salary_officer)
        total2 = 0
        for salaries in total_salary_officer:
            total2 += salaries
        average1 = total2 / len(total_salary_officer)
        print("average salary = ",average1)
    if data[2] == position_available[2]:
        print("3." + position_available[2])
        maximum = max(total_salary_manager)
        print("maximum salary = ",maximum)
        minimum = min(total_salary_manager)
        total3 = 0
        for salaries in total_salary_manager:
            total3 += salaries
        average2 = total3 / len(total_salary_manager)
        print("average salary = ",average2)
    

    
        









def saveAndExit():
    with open("data.txt","a") as file2:
    file2.write(total_id)
    file2.write(total_name)
    file2.write(total_position)
    file2.write(total_salary)



    

    


        

    
        





with open("data.txt","r") as file1:
    datas = file1.readlines()
    total_id = []
    total_name = []
    total_position = []
    total_salary = []
    total_salary_officer = []
    total_salary_staff = []
    total_salary_manager = []
    for data in datas:
        data = datas.split("#")
        print(data)
    id.append(data[0])
    name.append(data[1])
    position.append(data[2])
    salary.append(data[3])
        

    print("1. New Staff")
    print("2. Delete Staff") 
    print("3. View Summary Data") 
    print("4. Save and Exit" )
    toDo = input("Input Choice = ")
    if toDo == 1:
        newStaff()
    if toDo == 2:
        deleteStaff()
    if toDo == 3:
        viewSummaryData()
    if toDo == 4:
        saveAndExit()

    

    
