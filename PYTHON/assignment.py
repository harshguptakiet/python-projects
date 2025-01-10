employee_dict = {
    1: {'name': 'John', 'age': 27, 'id': '001'},
    2: {'name': 'Marie', 'age': 22, 'id': '002'}
}

def find_employee_age(employee_dict, target_id):
    for emp_id, details in employee_dict.items():
        if details['id'] == target_id:
            return details['age']
    return -1

target_id = input("Enter the target id :")
employee_age = find_employee_age(employee_dict, target_id)
if employee_age!=-1:
   print("the employee age is:")
   print(employee_age)
else:
    print("employee not found.")

        

        
     
