import time
Crew_list = [{"name": "Big Boss", "age": 49, "skill": "sneak"},
             {"name": "Kazuhira Miller", "age": 38, "skill": "debate"},
             {"name": "Revolver Ocelot", "age": 40, "skill": "interrogate"}]

def menu():
    print("-" * 110)
    print("""
 ██████╗           ███╗   ███╗           ███████╗
██╔════╝           ████╗ ████║           ██╔════╝
██║                ██╔████╔██║           ███████╗
██║                ██║╚██╔╝██║           ╚════██║
╚██████╗    ██╗    ██║ ╚═╝ ██║    ██╗    ███████║
 ╚═════╝    ╚═╝    ╚═╝     ╚═╝    ╚═╝    ╚══════╝ Version 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    """)
    print("Kept you waiting huh?")
    print("=" * 110)
    print("-" * 110)
    print("> 1. New Crew Info")
    print("> 2. Dismiss Crew")
    print("> 3. Edit Crew's Info")
    print("> 4. Show All Crew's Info")
    print("> 5. Crew Profile Lookup")
    print("> 6. Deploy Personnel on Mission")
    print("> 7. Exit C.M.S")
    print("> ?. ???")
    print("-" * 110)
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

def ops_list():
    while True:
        print("""
        180 150W  120W  90W   60W   30W  000   30E   60E   90E   120E  150E 180
        |    |     |     |     |     |    |     |     |     |     |     |     |
        +90N-+-----+-----+-----+-----+----+-----+-----+-----+-----+-----+-----+
        |          . _..::__:  ,-"-"._       |7       ,     _,.__             |
        |  _.___ _ _<_>`!(._`.`-.    /        _._     `_ ,_/  '  '-._.---.-.__|
        |.{     " " `-==,',._\{  \  / {)     / _ ">_,-' `                mt-2_|
        + \_.:--.       `._ )`^-. "'      , [_/(                       __,/-' +
        |'"'     \         "    _L       oD_,--'                )     /. (|   |
        |         |           ,'         _)_.\\._<> 6              _,' /  '   |
        |         `.         /          [_/_'` `"(                <'}  )      |
        +30N       \\    .-. )          /   `-'"..' `:._          _)  '       +
        |   `        \  (  `(          /         `:\  > \  ,-^.  /' '         |
        |             `._,   ""        |           \`'   \|   ?_)  {\         |
        |                `=.---.       `._._       ,'     "`  |' ,- '.        |
        +000               |    `-._        |     /          `:`<_|h--._      +
        |                  (        >       .     | ,          `=.__.`-'\     |
        |                   `.     /        |     |{|              ,-.,\     .|
        |                    |   ,'          \   / `'            ,"     \     |
        +30S                 |  /             |_'                |  __  /     +
        |                    | |                                 '-'  `-'   \.|
        |                    |/                                        "    / |
        |                    \.                                            '  |
        +60S                                                                  +
        |                     ,/           ______._.--._ _..---.---------._   |
        |    ,-----"-..?----_/ )      _,-'"             "                  (  |
        |.._(                  `-----'                                      `-|
        +90S-+-----+-----+-----+-----+----+-----+-----+-----+-----+-----+-----+
            """)
        print("-" * 110)
        print("Fetching Available Crew...")
        time.sleep(1.5)
        print("System...OK")
        time.sleep(1)
        print("Crew...OK")
        print("""
         ######  #### ########  ########     #######  ########   ######  
        ##    ##  ##  ##     ## ##          ##     ## ##     ## ##    ## 
        ##        ##  ##     ## ##          ##     ## ##     ## ##       
         ######   ##  ##     ## ######      ##     ## ########   ######  
              ##  ##  ##     ## ##          ##     ## ##              ## 
        ##    ##  ##  ##     ## ##          ##     ## ##        ##    ## 
         ######  #### ########  ########     #######  ##         ######  
            """)
        print("> 1. Assist the Civilian Evacuation")
        print("> 2. Defend the Refugee Camp")
        print("> 3. Secure the Bridgeheads")
        print("> 4. TBA")
        ops_input = int(input("> Select an option: (0 to quit)"))
        if ops_input == 0:
            return
        elif ops_input != 4 and ops_input < 4:
            crew_select()
        elif ops_input == 4:
            print("Not Yet")
            input("> Press Enter to Return")
            continue
        else:
            print("Invalid Input")
            input("> Press Enter to Return")
            continue


def crew_select():
    while True:
        show_crew()
        count_list = len(Crew_list)
        print(f"Use 1 - {count_list} to Select ; 0 to quit)")
        crew_input = input("Select the Personnel: ")
        if crew_input == "0":
            return
        elif crew_input != "0":
            int_crewinput = int(crew_input)
            if int_crewinput - 1 < len(Crew_list):
                print(f"{Crew_list[int_crewinput - 1]['name']} has been dispatched, Transporting is on the way.")
                break
            else:
                print("Invalid Input")
                input("> Press Enter to Return")
                break

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
        print("Waiting System Online...")
        time.sleep(1.5)
        print("System Online")
        ops_list()
        input(" > Enter to return to C.M.S")

    elif user_input == "7":
        print("Exit C.M.S")
        exit_code = input("Are you sure you want to exit C.M.S? (y/n): ")
        if exit_code == "y" or exit_code == "Y":
            print(f"""
 █████╗ ██████╗ ██████╗ ██████╗  ██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗     ███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝     ██║     ╚══███╔╝
███████║██████╔╝██████╔╝██████╔╝██║   ██║███████║██║     ███████║██║██╔██╗ ██║██║  ███╗    ██║       ███╔╝ 
██╔══██║██╔═══╝ ██╔═══╝ ██╔══██╗██║   ██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██║   ██║    ██║      ███╔╝  
██║  ██║██║     ██║     ██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝    ███████╗███████╗
╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚══════╝                                                                                                
            """)
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
