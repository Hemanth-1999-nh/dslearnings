#minitask question :

"""
Code Challenge
  Name: 
    Reading and Writing CSV
  Filename: 
    csv.py
  Problem Statement:
    Create a program that reads from one CSV file (/etc/passwd), 
    and writes to another one. 
    
    You are to read from data/passwd,
    and produce a file whose contents are the username (index 0) 
    and the user ID (index 2).
    Note that a record may contain a comment, 
    in which it will not have anything at index 2; 
    you should take that into consideration when writing the file.  
    The output file should use TAB characters to separate the elements.
 
    Thus, the input will look like:
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    _ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
    
    and the output will look like:
 
        root    0
        daemon  1
        _ftp    98
    
"""

"""
what i understood from the question : 
save a file with the  name "csv.py"
print below statement :  
create a program that reads from one CSV file (/etc/passwd), 
and writes to another one. 

read & produce thhe file where, the contents of file should be :-
index 1 - username
index 2 - user ID
"""

#solution to task :
    
"""
users={}
with open('passwd.txt') as f:
    for line in f:
        if not line.startswith("#") and line.strip():
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
for username , user_id in sorted(users.items()):
    print(f"{username}: {user_id}")
"""    
