#imports
import webbrowser
import time

#intro

print("")
print("")
print("$$$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$\     $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\      $$$$$$$\  $$\   $$\ $$\     $$\ $$$$$$$$\ $$$$$$$\ ")
print("$$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\    $$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|    $$  __$$\ $$ |  $$ |\$$\   $$  |$$  _____|$$  __$$\ ")
print("$$ |  $$ |$$ /  \__|$$$$\  $$$$ |$$ |  $$ |   $$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |          $$ |  $$ |$$ |  $$ | \$$\ $$  / $$ |      $$ |  $$ |")
print("$$$$$$$  |$$ |      $$\$$\$$ $$ |$$$$$$$  |   $$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\        $$$$$$$\ |$$ |  $$ |  \$$$$  /  $$$$$\    $$$$$$$  |")
print("$$  ____/ $$ |      $$ \$$$  $$ |$$  __$$<    $$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|       $$  __$$\ $$ |  $$ |   \$$  /   $$  __|   $$  __$$<")
print("$$ |      $$ |  $$\ $$ |\$  /$$ |$$ |  $$ |   $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |          $$ |  $$ |$$ |  $$ |    $$ |    $$ |      $$ |  $$ |")
print("$$ |      \$$$$$$  |$$ | \_/ $$ |$$ |  $$ |   \$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\     $$$$$$$  |\$$$$$$  |    $$ |    $$$$$$$$\ $$ |  $$ |")
print("\__|       \______/ \__|     \__|\__|  \__|    \______/ \__|  \__|\__|     \__|\________|    \_______/  \______/     \__|    \________|\__|  \__|")
print("Version 0.01")
print("")
print("It's nice to have choices!")
print("")
print("http://techiephile.tech")
print("")
print("This program will enter your search term on 6 major online game stores and open them in your browser.")
print("")


def redo():
    goagain = input("Do you want to keep searching? [y]/[n]: ")
    if goagain == "y":
    elif goagain == "n":
        print("K bye then")
        exit()
    else:
        print("Please choose y or n")


def main():
    game = input("What game do you want to purchase? ")
    greenmangaming = "https://www.greenmangaming.com/search/" + game
    steam = "http://store.steampowered.com/search/?term=" + game
    g2a = "https://www.g2a.com/?search=" + game
    gog = "https://www.gog.com/games?sort=bestselling&search=" + game + "&page=1"
    origin = "https://www.origin.com/usa/en-us/search?searchString=" + game
    kinguin = "https://www.kinguin.net/catalogsearch/result/index/?q=" + game
    webbrowser.open_new(greenmangaming)
    time.sleep(5)
    webbrowser.open(steam)
    webbrowser.open(g2a)
    webbrowser.open(gog)
    webbrowser.open(origin)
    webbrowser.open(kinguin)
    redo()
    
main()

