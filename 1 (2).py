accout = dict()
run = True
about = '''
1. Add user;
2. Delete user;
3. View user;
4. Set payout for the user by name.
5. Reset user position.'''

while run:
    get_func = int(input(f"{about} \n"))
    if get_func == 1:
        name = "".join(input("Type the name of user: ").lower().split())
        position = "".join(input("Type the position of user: ").lower().split())
        salary = int("".join(input("Enter the salary of user: ")))
        start_date = "".join(input("Enter the starting date: ").split())
        
        accout[name] = {"possition": position,  "salary": salary, "start_date": start_date}

    elif get_func == 2:
        del_user = input('Which user do you want to delete(type name)? ').lower().strip()
        if del_user in accout:
            accout.pop(del_user, None)
        else:
            print("User not found")
    
    elif get_func == 3:
        print(accout)

    elif  get_func == 4:
        user = input('Which user do you want to set new payout(type name)? ').lower().strip()
        if user in accout:
            new_salary = int(input(f"Type the new payout for {user}: "))
            accout[user]['salary'] = new_salary

    elif get_func == 5:
        name = input('Who do you want to reset the position?: ')
        print(f"Old position of {name} -  {accout[name]['possition']}")
        position = input(f"Type new position for {name}: ")
        accout[name]["position"] = position
        print("The position change.")
    else:
        print("This ID of func not found.".count(""))
        run = False