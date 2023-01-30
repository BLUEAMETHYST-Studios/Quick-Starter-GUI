import tkinter as tk
import os

#needed path variable
USER = os.getlogin()

#definitions
#if you want to change the paths, because on your device they are different, you can do that here!
def openDiscord():
    os.startfile ("C:/Users/" + USER + "/AppData/Local/Discord/app-1.0.9010/Discord.exe")
def openGX():
    os.startfile ("C:/Users/" + USER + "/AppData/Local/Programs/Opera GX/launcher.exe")
def openChrome():
    os.startfile ("C:\Program Files\Google\Chrome\Application\chrome.exe")
def openSteam():
    os.startfile ("C:\Program Files (x86)\Steam\steam.exe")
def openEpic():
    os.startfile ("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")




#window configuration
window = tk.Tk()
window.title("QUICK STARTER GUI (Early Dev 1.0.0)")
window.geometry("1000x1000")
window.configure(bg="white")

#text configuration
text1 = tk.Label(window, text="QUICK STARTER", font=("Consolas", 20), background="#FFFFFF")
text1.pack(padx=20, pady=20)
text2 = tk.Label(window, text="PRESS ON A BUTTON TO START AN APPLICATION", font=("Consolas", 15), background="#FFFFFF")
text2.pack(padx=20, pady=20)

#button configuration
buttonDiscord = tk.Button(window, text=" Discord ", font=("Consolas", 12), command=lambda : openDiscord(), background="#000000", foreground="#007FFF", bd=3)
buttonDiscord.pack(padx=20, pady=20)
buttonGX = tk.Button(window, text=" Opera GX ", font=("Consolas", 12), command=lambda : openGX(), background="#000000", foreground="#007FFF", bd=3)
buttonGX.pack(padx=20, pady=20)
buttonChrome = tk.Button(window, text=" Chrome ", font=("Consolas", 12), command=lambda : openChrome(), background="#000000", foreground="#007FFF", bd=3)
buttonChrome.pack(padx=20, pady=20)
buttonSteam = tk.Button(window, text=" Steam ", font=("Consolas", 12), command=lambda : openSteam(), background="#000000", foreground="#007FFF", bd=3)
buttonSteam.pack(padx=20, pady=20)
buttonEpic = tk.Button(window, text=" Epic Games ", font=("Consolas", 12), command=lambda : openEpic(), background="#000000", foreground="#007FFF", bd=3)
buttonEpic.pack(padx=20, pady=20)




window.mainloop()
