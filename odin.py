#!/usr/bin/env python2.7
#coded by Spades and Manisso

import argparse
import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading

#import requests

import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep

def menu():

    print """ \033[91m
============================================================                                                      
        _____         _____    ____  _____   ______   
   ____|\    \    ___|\    \  |    ||\    \ |\     \  
  /     /\    \  |    |\    \ |    | \\    \| \     \ 
 /     /  \    \ |    | |    ||    |  \|    \  \     |\033[32m
|     |    |    ||    | |    ||    |   |     \  |    |
|     |    |    ||    | |    ||    |   |      \ |    |
|\     \  /    /||    | |    ||    |   |    |\ \|    |\033[93m
| \_____\/____/ ||____|/____/||____|   |____||\_____/|
 \ |    ||    | /|    /    | ||    |   |    |/ \|   ||
  \|____||____|/ |____|____|/ |____|   |____|   |___|/
     \(    )/      \(    )/     \(       \(       )/  
      '    '        '    '       '        '       '   
=============================================================
{1}--EZ Dox Template \033[91m
{2}--IP Tools \033[32m
{3}--Password Attacks \033[93m
{4}--Windows Shells \033[91m
"""

    choice = raw_input("Pick a choice from above:")

    if choice == "1":
       doxer()
    elif choice == "2":
       iptools()
    elif choice == "3":
       passwd()
    elif choice == "4":
       shellz() 
os.system('clear')


def doxer():
    print """                                                                         
===========================================================================
    _____           _____                         ______        _____   
 ___|\    \     ____|\    \   _____      _____ ___|\     \   ___|\    \  
|    |\    \   /     /\    \  \    \    /    /|     \     \ |    |\    \ 
|    | |    | /     /  \    \  \    \  /    / |     ,_____/||    | |    |
|    | |    ||     |    |    |  \____\/____/  |     \--'\_|/|    |/____/ 
|    | |    ||     |    |    |  /    /\    \  |     /___/|  |    |\    \ 
|    | |    ||\     \  /    /| /    /  \    \ |     \____|\ |    | |    |
|____|/____/|| \_____\/____/ |/____/ /\ \____\|____ '     /||____| |____|
|    /    | | \ |    ||    | /|    |/  \|    ||    /_____/ ||    | |    |
|____|____|/   \|____||____|/ |____|    |____||____|     | /|____| |____|
  \(    )/        \(    )/      \(        )/    \( |_____|/   \(     )/  
   '    '          '    '        '        '      '    )/       '     '
===========================================================================                                                      '                  
"""
    name = raw_input("Enter the victims name:")
    age = raw_input("Enter victims age:")
    birthdate = raw_input("Enter victims birthdate:")
    family= raw_input("Enter victims family:")
    country = raw_input("Enter victims country:")
    state = raw_input("Enter victims state:")
    city = raw_input("Enter victims city:")
    Postal = raw_input("Enter victims zip/postal code:")
    Address = raw_input("Enter victims address:")
    Facebook = raw_input("Enter victims facebook url:")
    Twitter = raw_input("Enter victims twitter url:")
    Instagram = raw_input("Enter victims instagram url:")
    Skype = raw_input("Enter victims skype name:")
    LinkedIn = raw_input("Enter victims linkedin url:")
    IP = raw_input("Enter vicyims ip address:")
    DNSRecords = raw_input("Enter victims DNS records:")
    Websites = raw_input("Enter victims websites:")
    Blacklisted = raw_input("Enter victims sites the ip has been blacklisted from:")
    Ports = raw_input("Enter victims ports open on network:")
    Vulns = raw_input("Enter victims site/network vulnerabilities:") 
   
    print """
==============================================================================
                                                       _____                  
 ____________          ____    _____       _____  _____\    \ ____________    
 \           \     ____\_  \__ \    \     /    / /    / |    |\           \   
  \           \   /     /     \ \    |   |    / /    /  /___/| \           \  
   |    /\     | /     /\      | \    \ /    / |    |__ |___|/  |    /\     | 
   |   |  |    ||     |  |     |  \    |    /  |       \        |   |  |    | 
   |    \/     ||     |  |     |  /    |    \  |     __/ __     |    \/     | 
  /           /||     | /     /| /    /|\    \ |\    \  /  \   /           /| 
 /___________/ ||\     \_____/ ||____|/ \|____|| \____\/    | /___________/ | 
|           | / | \_____\   | / |    |   |    || |    |____/||           | /  
|___________|/   \ |    |___|/  |____|   |____| \|____|   | ||___________|/   
                  \|____|                             |___|/                  
================================================================================
"""
    print "============================{Basic Personal Info}==============================="
    print name
    print age
    print birthdate
    print family
    print "================================={Location}====================================="
    print country
    print city
    print Postal
    print Address
    print "==============================={Social Media}===================================="
    print Skype
    print Facebook
    print Instagram
    print Twitter
    print LinkedIn
    print "============================{Network Information}================================="
    print IP
    print DNSRecords
    print Ports
    print Blacklisted
    print Vulns
    print "=================================================================================="

def iptools():
    os.system('clear')
    os.system("git clone https://github.com/Manisso/Crips.git")
    os.system("cd Crips && sudo bash ./update.sh")
    os.system("crips")
    os.system("clear")

def cupp():
    print("cupp is a password list generator ")
    print("Usage: python cupp.py -h")
    choicecupp = raw_input("Continue: y/n : ")

    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("file downloaded successfully")
    elif choicecupp in no:
        os.system('clear')
        passwd()
    elif choicecupp == "":
        menu()
    else:
        menu()

yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

def passwd():
    print("   {1}--Cupp ")
    print("   {2}--Ncrack \n ")

    print("   {99}-Back To Main Menu \n")
    choice3 = raw_input("fsociety~# ")
    if choice3 == "1":
        os.system('clear')
        cupp()
    elif choice3 == "2":
        os.system('clear')
        ncrack()
    elif choice3 == "99":
        os.system('clear')
        menu()
    elif choice3 == "":
        menu()
    elif choice3 == "3":
        fb()
    else:
        menu()

def ncrack():
    print("A Ruby interface to Ncrack, Network authentication cracking tool.")
    print("requires : nmap >= 0.3ALPHA / rprogram ~> 0.3")
    print("Continue: y/n")
    choicencrack = raw_input("y / n :")
    if choicencrack in yes:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
        os.system("cd ruby-ncrack")
        os.system("install ruby-ncrack")
    elif choicencrack in no:
        os.system('clear')
        passwd()
    elif choicencrack == "":
        menu()
    else:
        menu()

def shellz():
    print """Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!"""
    cshell = raw_input("Y / N : ")
    if cshell in yes:
        os.system("git clone https://github.com/reyammer/shellnoob.git")
        os.system("mv shellnoob/shellnoob.py shellnoob.py")
        os.system("sudo python shellnoob.py --install")
    if cshell in no:
        exp()
    elif cshell == "":
        menu()
    else:
        menu()

menu()