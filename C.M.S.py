Crew_list = [{"name": "Big Boss", "age": 49, "skill": "sneak"},
             {"name": "Kazuhira Miller", "age": 38, "skill": "debate"},
             {"name": "Revolver Ocelot", "age": 40, "skill": "interrogate"}]


def menu():
    print("-" * 110)
    print("""                                                                                                                                                                                                                    
        CCCCCCCCCCCCC                  MMMMMMMM               MMMMMMMM                     SSSSSSSSSSSSSSS 
     CCC::::::::::::C                  M:::::::M             M:::::::M                   SS:::::::::::::::S
   CC:::::::::::::::C                  M::::::::M           M::::::::M                  S:::::SSSSSS::::::S
  C:::::CCCCCCCC::::C                  M:::::::::M         M:::::::::M                  S:::::S     SSSSSSS
 C:::::C       CCCCCC                  M::::::::::M       M::::::::::M                  S:::::S            
C:::::C                                M:::::::::::M     M:::::::::::M                  S:::::S            
C:::::C                                M:::::::M::::M   M::::M:::::::M                   S::::SSSS         
C:::::C                                M::::::M M::::M M::::M M::::::M                    SS::::::SSSSS    
C:::::C                                M::::::M  M::::M::::M  M::::::M                      SSS::::::::SS  
C:::::C                                M::::::M   M:::::::M   M::::::M                         SSSSSS::::S 
C:::::C                                M::::::M    M:::::M    M::::::M                              S:::::S
 C:::::C       CCCCCC                  M::::::M     MMMMM     M::::::M                              S:::::S
  C:::::CCCCCCCC::::C                  M::::::M               M::::::M                  SSSSSSS     S:::::S
   CC:::::::::::::::C      ......      M::::::M               M::::::M      ......      S::::::SSSSSS:::::S
     CCC::::::::::::C      .::::.      M::::::M               M::::::M      .::::.      S:::::::::::::::SS 
        CCCCCCCCCCCCC      ......      MMMMMMMM               MMMMMMMM      ......       SSSSSSSSSSSSSSS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    """)
    print("Kept you waiting huh?")
    print("=" * 110)
    print("> 1. New Crew Info")
    print("> 2. Dismiss Crew")
    print("> 3. Edit Crew's Info")
    print("> 4. Show All Crew's Info")
    print("> 5. Crew Profile Lookup")
    print("> 6. Exit C.M.S")
    print("> ?. ???")
    print("=" * 110)


def add_crew():
    name_input = input("Enter New Crew's Name: (0 to quit)")
    if name_input == "0":
        return
    else:
        age_input = input("Enter New Crew's Age: ")
        skill_input = input("Enter New Crew's Skill: ")
        Crew_list.append({"name": name_input, "age": age_input, "skill": skill_input})
        print(f"Adding {name_input} to the Crew List successfully.")


def edit_crew():
    name_input = input("Enter Crew's Name: (0 to quit)")
    for i in Crew_list:
        if i["name"] == name_input:
            print(i)
            edit_name = input("Edit Crew's Name: ")
            edit_age = input("Edit Crew's Age: ")
            edit_skill = input("Edit Crew's Skill: ")
            i["name"] = edit_name
            i["age"] = edit_age
            i["skill"] = edit_skill
            print(f"Editing {edit_name} successfully.")
            print(i)
            break
        elif name_input == "0":
            return
        else:
            print("Crew Not Found")



def dismiss_crew():
    dismiss_name = input("Enter the Crew's Name: (0 to quit)")
    if dismiss_name == "0":
        return
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

        elif lookup_name == "0":
            break
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
        input(" > Enter to return to C.M.S")

    elif user_input == "2":
        print("Dismiss Crew")
        dismiss_crew()
        input(" > Enter to return to C.M.S")

    elif user_input == "3":
        print("Edit Crew's Info")
        edit_crew()
        input(" > Enter to return to C.M.S")

    elif user_input == "4":
        print("Show All Crew's Info")
        show_crew()
        input(" > Enter to return to C.M.S")

    elif user_input == "5":
        print("Crew Profile Lookup")
        crew_lookup()
        input(" > Enter to return to C.M.S")

    elif user_input == "6":
        print("Exit C.M.S")
        exit_code = input("Are you sure you want to exit C.M.S? (y/n): ")
        if exit_code == "y" or exit_code == "Y":
            break
        elif exit_code == "n" or exit_code == "N":
            continue
        else:
            continue
    elif user_input.lower() == "boss":
        print("""
  _______ _            __  __              __          ___              _____       _     _   _______ _           __          __        _     _ 
 |__   __| |          |  \/  |             \ \        / / |            / ____|     | |   | | |__   __| |          \ \        / /       | |   | |
    | |  | |__   ___  | \  / | __ _ _ __    \ \  /\  / /| |__   ___   | (___   ___ | | __| |    | |  | |__   ___   \ \  /\  / /__  _ __| | __| |
    | |  | '_ \ / _ \ | |\/| |/ _` | '_ \    \ \/  \/ / | '_ \ / _ \   \___ \ / _ \| |/ _` |    | |  | '_ \ / _ \   \ \/  \/ / _ \| '__| |/ _` |
    | |  | | | |  __/ | |  | | (_| | | | |    \  /\  /  | | | | (_) |  ____) | (_) | | (_| |    | |  | | | |  __/    \  /\  / (_) | |  | | (_| |
    |_|  |_| |_|\___| |_|  |_|\__,_|_| |_|     \/  \/   |_| |_|\___/  |_____/ \___/|_|\__,_|    |_|  |_| |_|\___|     \/  \/ \___/|_|  |_|\__,_|                                                                                                                                                                                                                                                                                              
        """)
        input(" > Enter to return to C.M.S")
        continue
    elif user_input == "?":
        print("""      
███╗   ██╗ ██████╗     ███████╗ █████╗ ███████╗████████╗███████╗██████╗     ███████╗ ██████╗  ██████╗ 
████╗  ██║██╔═══██╗    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔════╝ ██╔════╝ 
██╔██╗ ██║██║   ██║    █████╗  ███████║███████╗   ██║   █████╗  ██████╔╝    █████╗  ██║  ███╗██║  ███╗
██║╚██╗██║██║   ██║    ██╔══╝  ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██║   ██║
██║ ╚████║╚██████╔╝    ███████╗██║  ██║███████║   ██║   ███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝                                                                                                                                                                                                                                                                                          
        """)
        input(" > Enter to return to C.M.S")
    else:
        print("""
        ██╗    ██╗██████╗  ██████╗ ███╗   ██╗ ██████╗     ██╗    ██╗ █████╗ ██╗   ██╗
        ██║    ██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝     ██║    ██║██╔══██╗╚██╗ ██╔╝
        ██║ █╗ ██║██████╔╝██║   ██║██╔██╗ ██║██║  ███╗    ██║ █╗ ██║███████║ ╚████╔╝ 
        ██║███╗██║██╔══██╗██║   ██║██║╚██╗██║██║   ██║    ██║███╗██║██╔══██║  ╚██╔╝  
        ╚███╔███╔╝██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝    ╚███╔███╔╝██║  ██║   ██║   
         ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝      ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝
                    """)
        input(" > Enter to return to C.M.S")
        menu()
