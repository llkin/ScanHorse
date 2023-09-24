import os
import sys


def banner():
    print("""\033[1;34m⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢱⠐⠄⠙⠽⡲⣤⡀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡾⠃⠀⠀⢀⠈⠻⣿⣿⣶⡶⢃⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡼⣧⣀⣠⡴⠀⢂⠀⠙⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣅⣩⠟⠁⢰⠀⠸⡄⠀⠐⢻⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠁⠀⠀⢀⠀⠀⡇⠀⠀⠄⠻⠿⢷⣋⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⠀⢠⠇⢀⡜⠀⠀⠐⡄⠀⠀⠈⠈⠐⢤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠀⢈⡴⠋⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀⢻⣿⣶⣦⣄⠀
⠀⠀⠀⠀⠀⡾⠀⡄⡎⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⡠⠀⢀⡇⠙⣿⣿⡷
⠀⠀⠀⠀⡠⠣⠀⠇⡄⠀⠀⠀⢠⠔⠁⠀⠀⠀⣠⠞⠀⢀⡜⣠⣾⢿⠟⠀
⠀⠀⢀⡴⠁⣀⠤⠊⠘⡆⠀⣠⠣⢤⠤⠴⢲⠋⠙⠀⣰⠋⠘⡝⠁⠘⠄⠀
⠀⣰⡿⠖⠉⠀⠀⢀⠊⡀⠚⠁⠀⠈⠀⡰⠁⠀⡆⡜⠁⠀⠀⠁⠀⠀⠀⠀
⢀⡿⠁⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⡀⢰⠁⢀⣼⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⡇⠀⠀⠀⠀⠀⢻⣧⣶⡄⠀⠀⣇⠎⣠⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣷⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⣼⢏⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[1;m⠀\n\n""")

    print("""\033[1;91m  #####                       #     #                             
 #     #  ####    ##   #    # #     #  ####  #####   ####  ###### 
 #       #    #  #  #  ##   # #     # #    # #    # #      #      
  #####  #      #    # # #  # ####### #    # #    #  ####  #####  
       # #      ###### #  # # #     # #    # #####       # #      
 #     # #    # #    # #   ## #     # #    # #   #  #    # #      
  #####   ####  #    # #    # #     #  ####  #    #  ####  ###### 
                                                                 \033[1;m """)

    print("1=> Default scan \n2=> Active scan \n3=> Portscan \n4=> Max verbose and info \n5=> Script scan only \n6=> portscan + Script ")

def Scanning():
    banner()
    print("\n\033[1;91mChoose one of them\033[1;m")
    choosen = input("*")
    if choosen == "ex" and choosen =="exit":
        print(exit(0))
    else:
        ip=input("\n\033[1;91mEnter ip address\033[1;m\n*")
    if choosen == "1":
        os.system("nmap "+ip)
        Scanning()
    if choosen == "2":
        os.system("nmap -A -p 1-1024 " + ip)
        Scanning()
    if choosen == "3":
        p=input("\n\033[1;91mDo you want to scan spesific port range (y/n) =>\033[1;m")
        Scanning()
        if p == "y" :
            pn=input("\nEnter port number*")
            os.system("nmap -p "+pn+" -sV "+ip)
            Scanning()
        if p == "n":
            os.system("nmap -p- "+ip)
            Scanning()
    if choosen == "4":
        os.system("nmap -sS -A -p- -vvv " + ip)
        Scanning()
    if choosen == "5":
        os.system("nmap --script vuln " + ip)
        Scanning()
    if choosen == "6":
        os.system("nmap -p- -vvv --script vuln " + ip)
        Scanning()
Scanning()

