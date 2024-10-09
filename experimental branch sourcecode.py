import time
import os
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
import time

# Loading screen with VAIIYA SECURITY ASCII Art
def startup_screen_ASCII():
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
#title stuff for new loadin screen 

def loading_bars_into():

    title = HTML('<style bg="blue" fg="black">Connecting to the VAIIYA Defender framework....</style>')
    label = HTML('<ansired>Connecting</ansired>.... ')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(300), label=label):
            time.sleep(.01)
        

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

    while True:
        text = prompt('awaiting commands>>>> ')
#put all the usercommands under here please! 

        if text == 't342':
            print('wrong answer')
            continue
        
        # FROST EE WIP!! 
        if text == 'frostbyte':
            print("loading frostbyte EE...")
            frostbyte_EE()


#below are all the non-user commands, DO NOT REMOVE!
            #the COMMANDS directory, DO NOT REMOVE!
        if text == 'commands':
            print("Commands;")
            print("placeholder here | explanation here")
            print("placeholder here | explanation here")
            print("placeholder here | explanation here")
            print("placeholder here | explanation here")
            print("placeholder here | explanation here")
            
            
            #the EXIT command, DO NOT REMOVE!! 
        if text == 'exit':
            print('exiting the terminal... have a nice day!')
            time.sleep(0.5)
            exit()
        
        #error response
        else:
            print("uhh, hmm, i dont think thats a command friend! type 'commands' for a list of commands!")


# FROST EE STUFF OVER HERE!
def frostbyte_EE():
                print("to exit, type EXIT in the password!")
                text = prompt('frotbytes password: ', is_password=True)
                if text == 'frostbyte_somthing_i_dont_know':
                    frostbytes_EE_entered()
                if text == 'exit':
                    return
                else:
                    print("Sorry! wrong password!")

# 2nd part to the FROST EE                     
def frostbytes_EE_entered():

                        text = prompt('type EXIT to exit this page; ')
                        if text == 'exit':
                            return

# Main system loop
def game_loop():
    #startup_screen_ASCII()
    #loading_bars_into()
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


