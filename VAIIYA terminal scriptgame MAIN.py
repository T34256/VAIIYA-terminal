import time
import os
import argparse

# Loading screen with VAIIYA SECURITY ASCII Art
def startup_screen():
    print(r"""
██╗   ██╗ █████╗ ██╗██╗██╗   ██╗ █████╗                       
██║   ██║██╔══██╗██║██║╚██╗ ██╔╝██╔══██╗                      
██║   ██║███████║██║██║ ╚████╔╝ ███████║                      
╚██╗ ██╔╝██╔══██║██║██║  ╚██╔╝  ██╔══██║                      
 ╚████╔╝ ██║  ██║██║██║   ██║   ██║  ██║                      
  ╚═══╝  ╚═╝  ╚═╝╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝                      
███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ 
╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗███████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝ 
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████╗ 
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ 
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║███████║ 
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ 

              Welcome to the VAIIYA SECURITY terminal! 
    """)

    # Simulated animated loading with ASCII art
    frames = [
        r"""
    LOADING VAIIYA SECURITY TERMINAL [=         ] 10%
        """,
        r"""
    LOADING VAIIYA SECURITY TERMINAL [===       ] 30%
        """,
        r"""
    LOADING VAIIYA SECURITY TERMINAL [=====     ] 50%
        """,
        r"""
    LOADING VAIIYA SECURITY TERMINAL [=======   ] 70%
        """,
        r"""
    LOADING VAIIYA SECURITY TERMINAL [========  ] 90%
        """,
        r"""
    LOADING VAIIYA SECURITY TERMINAL [========= ] 100%
        """
    ]
    
    # Loop through the frames to simulate loading animation
    for frame in frames:
        print(frame, end="\r", flush=True)
        time.sleep(1)  # Pause for effect
    print("\nLoading Complete!\n")
    time.sleep(1)  # Small pause after loading

# Display main menu
def main_menu():
    print(r"""
 ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______ 
| |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| |
|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |
|______||______||______||______||______||______||______||______||______||______||______||______||______|
 ______                                                                                          ______ 
| |__| |                                                                                        | |__| |
|  ()  |   __   __ _    ___  ___ __   __ _     ___  ___  ___  _   _  ___  ___  _____ __   __    |  ()  |
|______|   \ \ / //_\  |_ _||_ _|\ \ / //_\   / __|| __|/ __|| | | || _ \|_ _||_   _|\ \ / /    |______|
 ______     \ V // _ \  | |  | |  \ V // _ \  \__ \| _|| (__ | |_| ||   / | |   | |   \ V /      ______ 
| |__| |     \_//_/ \_\|___||___|  |_|/_/ \_\ |___/|___|\___| \___/ |_|_\|___|  |_|    |_|      | |__| |
|  ()  |    ___ __   __ ___  _____  ___  __  __  ___   __  __  ___  _  _  _   _                 |  ()  |
|______|   / __|\ \ / // __||_   _|| __||  \/  |/ __| |  \/  || __|| \| || | | |                |______|
 ______    \__ \ \ V / \__ \  | |  | _| | |\/| |\__ \ | |\/| || _| | .` || |_| |                 ______ 
| |__| |   |___/  |_|  |___/  |_|  |___||_|  |_||___/ |_|  |_||___||_|\_| \___/                 | |__| |
|  ()  |                                                                                        |  ()  |
|______|                                                                                        |______|
 ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______ 
| |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| |
|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |
|______||______||______||______||______||______||______||______||______||______||______||______||______|

                                Welcome to the VAIIYA terminal!
            Use this handy dandy terminal for all your duties at VAIIYA security corp!  
    """)

# Start the TERMINAL and its commands
def open_terminal():
    print("\nYou have entered the VAIIYA Terminal.")
    print("\nTo exit the terminal, please type EXIT to return to the menu.\n")
    print("Type 'help' or 'commands' for a list of commands.")
    while True:
        command = input("Awaiting command(s) >>> ").lower()

        if command == "help":
            print("\nAvailable commands:")
            print("exit - Exit the game.\n")
        elif command == "commands":
            print("\nAvailable commands:")
            print("exit - Exit the terminal.\n")
# abve is a ELIF command to prevent the "undefined repeat"
                
        
        
 # below are the EE commands and the EXIT command! dont change these please!! 
        elif command == "credits":
                print("|")
                print("This script game was proudly made by T342 | your local VAIIYA guard!")
                print("I am very proud of this and i hope there will be a bunch of things that i can add to it!")
                print("|")
        elif command == "t342":
            print("Heyyy thanks! you wanted to say somthng to me? :3")
        elif command == "rob":
            print("what did you really think rob was involved in this?? i wish haha")
        elif command == "exit":
            print("exiting the terminal.... have a good day and stay secure!")
            break
        else:
           print("\nUnknown command, cuz this is a script. not a dictonary of commands! Type 'help' for a list of commands.\n")



# Main game loop
def game_loop():
    startup_screen()
    main_menu()
    open_terminal()
    
    while True:
        
        pass
        


# Start the game
game_loop()


#if __name__ == "__main__":
#        main()



#IMPORTANT NOTES AND BEHAVEIORS IN CODE!!!! 
# 1. NEVER put a IF staement with a OR command!! or any other command will do the same action!! including undefined ones!! 
# the way to get arount this is use a ELIF command, than the OR statement will not reapet undefined or incorrect strings!!! - T342 the owner if you were snooping >:3 

#update above: you cannot use workaround in main menu!! i have no idea why! you will just need to make a dual command instead. 

# 2. UwU dont you say ANYTHING ABOUT THAT - NOT T342, DONT TELL FROST PLEASESSSSSSSSSSSSSSSSSSSSSS


#found new menu system that need the EXIT command:
#  
#command = input("type EXIT to go to main menu>>> ").lower()
#    while True:
        #if command == "exit":
            #break
# use that at the end of a text viewscreen or file viewer - T342 you extra snoop >:3 