Crew_list = [{"name": "Big Boss", "age": 49, "skill": "sneak"},
             {"name": "Kazuhira Miller", "age": 38, "skill": "debate"},
             {"name": "Revolver Ocelot", "age": 40, "skill": "interrogate"}]


def menu():
    print("^" * 50)
    print("""
     CCCCC   M   M   SSSSS
     C       MM MM   S
     C       MM MM   S
     C       M M M   SSSSS
     C       M   M       S
     C       M   M       S 
     CCCCC . M   M . SSSSS V1.0 by Diamond Dogs
    """)
    print("=" * 50)
    print("> 1. New Crew Info")
    print("> 2. Dismiss Crew")
    print("> 3. Edit Crew's Info")
    print("> 4. Show All Crew's Info")
    print("> 5. Crew Profile Lookup")
    print("> 6. Exit C.M.S")
    print("> ?. ???")
    print("=" * 50)


def add_crew():
    name_input = input("Enter New Crew's Name: ")
    age_input = input("Enter New Crew's Age: ")
    skill_input = input("Enter New Crew's Skill: ")
    Crew_list.append({"name": name_input, "age": age_input, "skill": skill_input})
    # print(Crew_list)


def edit_crew():
    name_input = input("Enter Crew's Name: ")
    for i in Crew_list:
        if i["name"] == name_input:
            print(i)
            edit_name = input("Edit Crew's Name: ")
            edit_age = input("Edit Crew's Age: ")
            edit_skill = input("Edit Crew's Skill: ")
            i["name"] = edit_name
            i["age"] = edit_age
            i["skill"] = edit_skill
            print(i)
            break
        else:
            print("Crew Not Found")


def dismiss_crew():
    dismiss_name = input("Enter the Crew's Name: ")
    for i in Crew_list:
        if i["name"] == dismiss_name:
            Crew_list.remove(i)
            print(f"{dismiss_name} has been dismissed")
            break
    else:
        print("Sorry, Crew Not Found")


def crew_lookup():
    for i in Crew_list:
        lookup_name = input("Enter the Crew's Name: (0 to quit)")
        if lookup_name == i["name"]:
            print(i)
        else:
            print("Sorry, Crew Not Found")


def show_crew():
    for i in Crew_list:
        print(i)


while True:
    menu()
    user_input = input("Select an option: ")
    if user_input == "1":
        print("New Crew Info")
        add_crew()
    elif user_input == "2":
        print("Dismiss Crew")
        dismiss_crew()
    elif user_input == "3":
        print("Edit Crew's Info")
        edit_crew()
    elif user_input == "4":
        print("Show All Crew's Info")
        show_crew()
    elif user_input == "5":
        print("Crew Profile Lookup")
        crew_lookup()
    elif user_input == "6":
        print("Exit C.M.S")
        exit_code = input("Are you sure you want to exit C.M.S? (y/n): ")
        if exit_code == "y" or exit_code == "Y":
            break
        elif exit_code == "n" or exit_code == "N":
            continue
        else:
            continue
    elif user_input == "Boss" or user_input == "boss":
        for abc in range(11):
            print("The man who sold the world")
            print()
        continue
    else:
        for abc in range(11):
            print("Wrong Way")
            print()
        continue
