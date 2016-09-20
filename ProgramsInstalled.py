import re
import subprocess
import socket
import os

host_name = socket.gethostname()
file_name = host_name + "_ProgramsInstalled.txt"

subprocess.call(['Powershell.exe', 'Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName | Out-File ProgramsInstalled.txt -encoding ASCII'])

hand = open('ProgramsInstalled.txt', 'r')

new_txt = ""

for line in hand :
    line = line.rstrip()
    if re.search('Update\sfor\sMicrosoft', line) or re.search('Service\sPack', line) or re.search('(?m)^\s*$\s*', line):
        continue
    else :
    	new_txt += (str(line) + "\n")

hand.close()

os.remove('ProgramsInstalled.txt')

hand = open(file_name, 'w')
hand.write(new_txt)
hand.close()
