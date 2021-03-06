import os
from time import sleep
from os import system, name
import wget
import json
import urllib.request

programver="0.0.3"

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

def menu():
    
    clear()
    if not os.path.exists('OCD-Downloads'):
            os.mkdir("OCD-Downloads")
    os.chdir("OCD-Downloads")
    if not os.path.exists('OpenCore'):
            os.mkdir("OpenCore")
    if not os.path.exists('Kexts'):
            os.mkdir("Kexts")
    os.chdir(os.path.pardir)
    print("Options:\n 1.- Download Latest OpenCore\n 2.- Download Latest Kexts\n 3.- COMING SOON.\n 4.- Quit")
    print("")
    option = input("Select an option: ")
    if option == "1":
        downloadoc()
    elif option == "2":
        downloadkexts()
    elif option == "3":
        clear()
        print("Coming soon...")
        sleep(3)
        menu()
    elif option == "4":
        clear()
        print("Thanks for using this tool!")
        sleep(1)
        print("Closing...")
        sleep(2)
        

def downloadoc():
    clear()
    
    print("Which one?")
    print("1) Debug")
    print("\n NOTE: You can't download the Release version of OpenCore yet, i'm working on re-adding it.")
    option = input("Select an option: ")
    if option == "1":
        url = "https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest"
        data = urllib.request.urlopen(url).read().decode()
        obj = json.loads(data)
        with open('latest_oc_url', 'w') as json_file:
            json.dump(obj['assets_url'], json_file)

        with open('latest_oc_url', 'r') as json_file:
            newurl = json.load(json_file)
            newdata = urllib.request.urlopen(newurl).read().decode()
            newobj = json.loads(newdata)
        os.chdir("OCD-Downloads")
        os.chdir("OpenCore")
        if not os.path.exists('Debug'):
            os.mkdir("Debug")
        os.chdir("Debug")
        print("Alright! Now downloading...")
        wget.download(newobj[0]['browser_download_url'])
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        menu()

def downloadkexts():
    clear()
    print("There are only a few kexts at the moment, more will come soon.")
    print("WARNING: The kexts downloaded in here are the release kexts.")
    print("1) VirtualSMC")
    print("2) FakeSMC")
    print("3) Lilu")
    print("4) WhateverGreen")
    print("5) IntelMausi")
    print("6) AtherosE2200Ethernet")
    print("7) RealtekRTL8111")
    print("8) RealtekRTL8100")
    print("9) USBInjectAll")
    print("10) AppleALC")
    print("Q) Quit")
    print("")
    option = input("Select an option: ")
    if option == "1":
        url = 'https://github.com/acidanthera/VirtualSMC/releases/download/1.1.8/VirtualSMC-1.1.8-RELEASE.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "2":
        url='https://bitbucket.org/RehabMan/os-x-fakesmc-kozlek/downloads/RehabMan-FakeSMC-2018-0915.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "3":
        url='https://github.com/acidanthera/Lilu/releases/download/1.4.9/Lilu-1.4.9-RELEASE.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "4":
        url=''
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "5":
        url='https://github.com/acidanthera/IntelMausi/releases/download/1.0.4/IntelMausi-1.0.4-RELEASE.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "6":
        url='https://github.com/Mieze/AtherosE2200Ethernet/releases/download/2.2.2/AtherosE2200Ethernet-V2.2.2.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "7":
        url='https://github.com/Mieze/RTL8111_driver_for_OS_X/releases/download/V2.3.0/RealtekRTL8111-V2.3.0.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "8":
        url='https://bitbucket.org/RehabMan/os-x-realtek-network/downloads/RehabMan-Realtek-Network-v2-2017-0322.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "9":
        url='https://bitbucket.org/RehabMan/os-x-usb-inject-all/downloads/RehabMan-USBInjectAll-2018-1108.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "10":
        url='https://github.com/acidanthera/AppleALC/releases/download/1.5.4/AppleALC-1.5.4-RELEASE.zip'
        os.chdir("OCD-Downloads")
        os.chdir("Kexts")
        print("Alright! Now downloading...")
        wget.download(url)
        print("\nDone!")
        os.chdir(os.path.pardir)
        os.chdir(os.path.pardir)
        sleep(2)
        downloadkexts()
    elif option == "Q":
        menu()
        


print(f"OpenCore Downloader {programver}")
print("")
print("WARNING:\nOpenCore Downloader isn't an official tool,\nand it may get outdated really quick.")
sleep(3)
menu()

