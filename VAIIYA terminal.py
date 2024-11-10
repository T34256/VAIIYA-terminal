import time
import os
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
import time
import bcrypt
from datetime import datetime
from prompt_toolkit import print_formatted_text, HTML



# Loading screen with VAIIYA SECURITY ASCII Art
def startup_screen_ASCII():
    print(r"""

                                                                                                                                                                                                                                                                          
                                                          ___________   ____________                                                                                                                                                                                              
                                                         \|||||||||||\ \::::::::::::\                                                                                                           
                                                          \|||||||||||\ \::::::::::::\                                                                                                
                                                           \|||||||||||\ \::::::::::::\                                                                                              
                                                            \|||||||||||\ \::::::::::::\                                                                                              
\-------\             /------------/  /-----------\  \----------\  \----------\  \----------\           /-----------/  /-----------\                                      
 \.......\           /............/  /.............\  \..........\  \..........\  \..........\         /.........../  /.............\                                     
  \.......\         /............/  /...............\  \..........\  \..........\  \..........\       /.........../  /...............\                                   
   \.......\       /............/  /.................\  \..........\  \..........\  \..........\     /.........../  /.................\                                  
    \.......\     /............/  /........__.........\  \..........\  \..........\  \..........\   /.........../  /...................\                                 
     \.......\   /............/  /......../  \.........\  \..........\  \..........\  \..........\_/.........../  /........./  \........\                              
      \.......\ /............/  /......../    \.........\  \..........\  \..........\  \....................../  /........./    \........\                            
       \..................../  /......../      \.........\  \..........\  \..........\  \..................../  /........./      \........\                           
        \................../  /......../        \.........\  \..........\  \..........\  \................../  /........./        \........\                          
         \................/  /......../          \.........\  \..........\  \..........\  \................/  /........./          \........\                        
          \............../  /......../            \.........\  \..........\  \..........\  \............../  /........./            \........\                     
                                                                                           /............./                                                                   
                                                                                          /............./                                                                       
                                                                                         /............./                                                                        
                                                                                        /............./                                                                          
                                                                                       /............./                                                                           
                                                                                      /-------------/                                                                             


                                                               
                                                    Welcome to the VAIIYA SECURITY terminal! 
    """)
#title stuff for new loadin screen 

def loading_bars_intro_1():

    title = HTML('Connecting to the VAIIYA Defender framework....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(300), label=label):
            time.sleep(.01)
    time.sleep(1)
        
def loading_bars_intro_2():

    title = HTML('Checking root for verification codes....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(215), label=label):
            time.sleep(.01)
    time.sleep(1)


def loading_bars_intro_3():

    title = HTML('Sending system logs and debug info for system approval')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(175), label=label):
            time.sleep(.01)
    time.sleep(1)
    
    print("connection: approved")
    time.sleep(0.3)
    print("codes found! checking with system.... approved!")
    time.sleep(0.2)
    print("sending logs.... approved! sending debug... approved! ")
    time.sleep(0.1)
    print("All connections approved! opening VAIIYA terminal....")


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
            Use this handy dandy terminal for all your duties at VAIIYA cybersecurity corp!  
    """)
def timefetch():
#time fetch for login
    curtime = datetime.now().strftime('%H:%M:%S') 
    curdate = datetime.now().strftime('%Y-%m-%d')

    print('Welcome VAIIYA trustee! the time is: ',curtime)
    print('and the date is: ',curdate)
    print("have a wonerful day at VAIIYA cybersecurity corp!")

# Start the TERMINAL and its commands
def open_terminal():

    while True:
        print(" for a list of commands, please type 'commands' ")
        text = prompt('awaiting command(s)>>> ')
#put all the usercommands under here please! 
        


        
        
        
        
        if text == 'CNS':
            print("running secondary program...")
            time.sleep(2)
            CNS_EE_HAKED()

        if text == 't342':
            print('heyy thanks for sayin somthin!')
            continue
        

        if text == 'walker':
            print("welcome walker to your login! please wait while your coffee brews.......")
            time.sleep(3)
            walker_login()

        #BUG: the error "no command" will reply when exiting the FROST EE!
        # FROST EE WIP!! 
        if text == 'frostbyte':
            print("welcome frostbyte to your login! please wait while i startup the supercomputer and freeze these bytes!....")
            time.sleep(3)
            #enters the frostbyte EE
            frostbyte_login()


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

# PLEASE PUT ALL 2ND DEF(S) BELOW THIS NOTE! 






#PUT ALL OTHER NON SUBCOMMAND DEFs BELOW HERE!
# the CNS EE below this messange
def CNS_EE_HAKED():
    result = yes_no_dialog(
    title='CNS.02.06.01',
    text='dO yOU wAnT ThE tRUTh?').run()
    if result == True:
         message_dialog(
    title='CNS.02.06.01',
    text='very well then, we will see you soon enough').run()
         
         print(" FATAL ERROR!: VAIIYA defenter has encountered an error! please restart the program to continue!")
         time.sleep(4)
         exit()
    if result == False:
         message_dialog(
    title='CNS.02.06.01',
    text='how dissapointing, that you dont want tHe TrutH. we will see you soon enough').run()
         
         print(" FATAL ERROR!: VAIIYA defenter has encountered an error! please restart the program to continue!")
         time.sleep(4)
         exit()



#add passwords here for the logins and name the vars respectivly 
#hehe youll never get the passwords now! AHAHAHAHAHA! 
#walkerpasswrd1
walkerhash = b'$2b$12$M7LXCClyfsnN9SjibtnEmuLEOlR68H2ovjCBA0zcAIBs2RHBzOnFy'
#frostEEpswrd1
frosthash = b'$2b$12$AUur7AKX1aGQurOlmM46Pu0OX9HXqx6UHH9SHiEvrCJM56JvUjYfu'


#walker login here
def walker_login():
    
    #password prompt; 
    userpassword = text = input_dialog(
    title='Walker password input',
    text='walker password:').run()
    #encodes the given password for comapare
    userpassword = userpassword.encode('utf-8')

    #comapre password hashes, if identical then "result" == True, then it will move onto walker_entered
    result = bcrypt.checkpw(userpassword, walkerhash)
    if result:
          walker_entered()
#end of walker password varifi 

def walker_entered():
    print("welcome walker! here currnently there is nothing, i have no idea what to put here for you guys.")
    print("but id assume you are familiar with github so if you have an idea i would more than glad take a look and try to implement it! ")
    text = prompt("type EXIT to exit this page; ")
    if text == 'exit':
        return
        #end of walker login

# FROST EE STUFF OVER HERE!
def frostbyte_login():
                
                
    print("to exit, type EXIT in the password!")
    userpassword = text = input_dialog(
    title='frostbyte password input',
    text='frostbyte password:').run()
    
    userpassword = userpassword.encode('utf-8')
               
    #comapre password hashes
    result = bcrypt.checkpw(userpassword, frosthash)
    if result:
          frostbytes_EE_entered()
    if text == 'exit':
        return
# 2nd part to the FROST EE                     
def frostbytes_EE_entered():
    
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA TERMINAL WARNING AWAITING ATTENTION!').run()
    
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA employee T342 has marked you as "requires careful observation and mental medical attention." so the VAIIYA system observation drones will now observe you.').run()

    message_dialog(
    title='VAIIYA Warning systems',
    text='thank you for your attention. you may continue your tasks and have a safe day!').run()
    
    
    print(f"""welcome frostbyte! to your ee/login! dont worry, no one will find your password ^_+ """)
    text = prompt("type EXIT to exit this page;")
    
    if text == 'exit':
        return
#END OF FROST EE CODE, 



# Main system loop
def game_loop():
    startup_screen_ASCII()
    loading_bars_intro_1()
    loading_bars_intro_2()
    loading_bars_intro_3()
    main_menu()
    timefetch()
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


