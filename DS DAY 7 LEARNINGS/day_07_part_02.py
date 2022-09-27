#RegeX
# a.k.a regular expression

import re
dir(re)
"""
methods\functions desired to learn under module 're' :
    sub
    findall
    search
    match
    compile
"""    
help(re.A)
help(re.sub)
help(re.findall)
help(re.search)
help(re.match)
help(re.compile)

# SUB METHOD

#data is in string\text format -
mails = 'hemanth2gmail.com nagunoori64@gmail.com pavan01@yahoo.com kumar08@yahoo.com laxminivas1986@outlook.com'

s = 'aaa@gmail.com bbb@yahoo.com ccc@outlook.com'
#call 'sub' function in RegeX 
# sub function code is as follows : re.sub(RegeX pattern we're searching,replacing text, data source )
#re.sub(3 parameters as mentioned above)

substring_s = re.sub('[a-z]*@','ABC@',s)

print(s)
print(substring_s)

str1 = 'abc123xyz456_0789'

substr1 = re.sub('[0-9]{3}','QWERTY', str1)
print(substr1)
                   ----------------------------------
#FINDALL METHOD

#to find desired characters in our data we use findall
#findall code consists of 2 parameters : our pattern searching, data source
#re.findall('pattern','data source')
str1 = '123abc123xyz456_0789'

searched_list_str1 = re.findall('^[0-9]{3}',str1)
print(searched_list_str1)
                      ------------------------------
# SEARCH METHOD

# in search method we get data as 'match object' 
#in search method code will be : re.search(searching pattern, data source)
#the command gives in result only the first match
#refer below for example

str2 = '123ekf230u403jfp233uuf823jrpurrme035u323p032mf'
search_command_str2 = re.search('^\d{3}', str2)
print(search_command_str2)
                      ---------------------------------
"""
in findall method, we get only matches but not location\indices(sig : index)
in search method, we get only initial match but with indices(sig : index)
"""

# MATCH METHOD

#trying out an example to differentiate between match and search

str3 = 'Hemanth hemanth nagunoori of bpharm from malla reddy pharmacy college' 

re.match('hemanth', str3)  = no output here
re.match('Hemanth', str3)  = output
                           
re.search('hemanth', str3) = output
re.search('Hemanth', str3) = output

#search = find something anywhere in the string and return the object
#match = find something at the beginning of the string and return the object
#conclusion from above operations is that : match is search with meta character(^)

#COMPILE METHOD

str4 = 'hemanth@gmail.com 70934@yahoo.in Asvr143@qualcomm.in hgupta@apple.com NAGUNOORI@mrpc.com gland_pharma@QC sahajanand_medical_technologies@QA medicos_medical_writer@writer.in OGHealthCare.co.in optumsolutions.in'

re.findall('\w+@\w+\.\w+', str4)

final_function = re.compile(r'\w+@\w+\.\w+')
final_function.findall(str4)

#compile is used to avoid rewriting regex again and again
#we can try any function sucuh as findall\replace\sub\match etc in line 90 under compile
#---> its advised to mention "r" infront of any regex expression u write in production code (roy string pattern)
 
print('a\tb')
type(print('a\tb'))
print(r'a\tb')

