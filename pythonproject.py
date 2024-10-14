#!/bin/usr/python3

import re
import time

# Define file path for auth.log. auth.log in a fixed path for easier reference

file_path = '/home/kali/Desktop/python/project/auth.log'

# Read content of auth.log file

with open(file_path,'r') as file:
		
	# Making sure that it's always starting from the top regardless
	file.seek(0)
		
	# Read as list for text manipulation
	authlog_content = file.readlines() 


# Lists to store information

new_users = []
deleted_users = []
password_change = []
su_commands = []
sudo_commands = []
sudo_alerts = []


# 2.1 Print details of newly added users, including Timestamp

newuser = re.compile(r'new user: name=(\w+)')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if newuser.search(line):
        new_users.append(line.strip())
        
print('Newly Added Users')
for entry in new_users:
	print(entry)


# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)


# 2.2 Details of deleted users, including Timestamp

deluser = re.compile(r'delete user')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if deluser.search(line):
        deleted_users.append(line.strip())
        
print('Deleted Users')
for entry in deleted_users:
	print(entry)

# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)


# 2.3 Details of changing passwords, including Timestamp

changepasswd = re.compile(r'password changed')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if changepasswd.search(line):
        password_change.append(line.strip())
        
print('Password changed')
for entry in password_change:
	print(entry)

# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)



# 2.4 Details of when users used su command

sucommand = re.compile(r'\bsu\b')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if sucommand.search(line):
        su_commands.append(line.strip())
        
print('Users using su commands')
for entry in su_commands:
	print(entry)

# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)



# 2.5 Details of users who used the sudo; include command

sudocommand = re.compile(r'sudo.*COMMAND=(.*)')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if sudocommand.search(line):
        sudo_commands.append(line.strip())
        
print('Users using sudo commands')
for entry in sudo_commands:
	print(entry)

# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)



# ~ # 2.6 Print ALERT! if users failed to use the sudo command; include command

sudoalert = re.compile(r'(sudo:.*(authentication failure|incorrect password|NOT))')

for line in authlog_content:
    # ~ timestamp = extract_timestamp(line)
    
    if sudoalert.search(line):
        sudo_alerts.append(line.strip())
        
print('Users failed to use sudo command')
for entry in sudo_alerts:
	print('ALERT!', entry)
	

# Empty lines and for python to wait for 3 seconds before printing the next data for easier reference
print('\n' *3)
time.sleep(3)
