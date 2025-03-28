import os
import random
import string
import subprocess
import winreg
import time
from colorama import Fore, Style, init

init()

current_color = Fore.WHITE

def install_requirements():
    os.system('pip install colorama')

install_requirements()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_string(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def spoof_mac():
    adapter_name = "Ethernet"
    new_mac = "02:" + ":".join(["%02x" % random.randint(0, 255) for _ in range(5)])
    os.system(f'netsh interface set interface "{adapter_name}" admin=disable')
    os.system(f'reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\0001 /v NetworkAddress /t REG_SZ /d {new_mac} /f')
    os.system(f'netsh interface set interface "{adapter_name}" admin=enable')
    print(current_color + f"Neue MAC-Adresse: {new_mac}" + Style.RESET_ALL)

def spoof_disk():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Disk\Enum", 0, winreg.KEY_SET_VALUE)
    fake_id = random_string(20)
    winreg.SetValueEx(key, "0", 0, winreg.REG_SZ, fake_id)
    winreg.CloseKey(key)
    print(current_color + f"Gespoofte HDD-ID: {fake_id}" + Style.RESET_ALL)

def clear_fivem_cache():
    fivem_path = os.path.expandvars(r"%localappdata%\FiveM\FiveM.app\data\cache")
    if os.path.exists(fivem_path):
        os.system(f'rd /s /q "{fivem_path}"')
        print(current_color + "FiveM-Cache gelöscht." + Style.RESET_ALL)

def clear_temp_files():
    os.system("del /s /f /q %temp%\*")
    os.system("del /s /f /q C:\\Windows\\Temp\\*")
    print(current_color + "Temporäre Dateien wurden gelöscht!" + Style.RESET_ALL)

def optimize_pc():
    os.system("powercfg -h off")
    os.system("bcdedit /set useplatformclock false")
    os.system("bcdedit /set tscsyncpolicy Enhanced")
    os.system("bcdedit /set disabledynamictick yes")
    print(current_color + "PC-Optimierung abgeschlossen!" + Style.RESET_ALL)

def optimize_network():
    os.system("netsh int tcp set global autotuninglevel=normal")
    os.system("netsh int tcp set global rss=enabled")
    os.system("netsh int tcp set global chimney=enabled")
    os.system("netsh int tcp set global dca=enabled")
    print(current_color + "Netzwerk-Optimierung abgeschlossen!" + Style.RESET_ALL)

def change_color():
    global current_color
    print("1. Weiß\n2. Grün\n3. Gelb\n4. Blau\n5. Rot")
    choice = input("Wähle eine Farbe: ")
    colors = {"1": Fore.WHITE, "2": Fore.GREEN, "3": Fore.YELLOW, "4": Fore.BLUE, "5": Fore.RED}
    current_color = colors.get(choice, Fore.WHITE)

def show_menu():
    clear_screen()
    print(current_color + """
██████╗ ████████╗██╗  ██╗
██╔══██╗╚══██╔══╝██║  ██║
██║  ██║   ██║   ███████║
██║  ██║   ██║   ██╔══██║
██████╔╝   ██║   ██║  ██║
╚═════╝    ╚═╝   ╚═╝  ╚═╝
                         
[39 TOOL]
""" + Style.RESET_ALL)
    print(current_color + "\n1. Spoofing\n2. ASCII ART\n3. PC Optimizer\n4. Network Optimizer\n5. Discord Multitool\n6. FiveM Cleaner\n7. Temp Cleaner\n8. Free VPN\n9. DC Selfbot\n10. Credits\n11. Settings\n12. Exit\n" + Style.RESET_ALL)

def main():
    while True:
        show_menu()
        choice = input(current_color + "Wähle eine Option: " + Style.RESET_ALL)
        if choice == "1":
            spoof_mac()
            spoof_disk()
        elif choice == "2":
            os.system("start https://patorjk.com/software/taag/")
        elif choice == "3":
            optimize_pc()
        elif choice == "4":
            optimize_network()
        elif choice == "5":
            os.system("start https://github.com/AstraaDev/Discord-All-Tools-In-One")
        elif choice == "6":
            clear_fivem_cache()
        elif choice == "7":
            clear_temp_files()
        elif choice == "8":
            os.system("start https://protonvpn.com/")
        elif choice == "9":
            os.system("start https://nighty.one/")
        elif choice == "10":
            print(current_color + "\nMade by @d39th\nDiscord add : D39th\nGithub : D39th" + Style.RESET_ALL)
        elif choice == "11":
            change_color()
        elif choice == "12":
            exit()
        else:
            print(Fore.RED + "Ungültige Eingabe!" + Style.RESET_ALL)
        input(current_color + "\nDrücke Enter, um ins Hauptmenü zurückzukehren..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
