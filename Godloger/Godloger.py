print("""\033[0m\033[32m
         ....        .                  ..             ..                                                 
   .x88" `^x~  xH(`                dF         x .d88"                                                  
  X888   x8 ` 8888h          u.   '88bu.       5888R          u.                             .u    .   
 88888  888.  %8888    ...ue888b  '*88888bu    '888R    ...ue888b       uL          .u     .d88B :@8c  
<8888X X8888   X8?     888R Y888r   ^"*8888N    888R    888R Y888r  .ue888Nc..   ud8888.  ="8888f8888r 
X8888> 488888>"8888x   888R I888>  beWE "888L   888R    888R I888> d88E`"888E` :888'8888.   4888>'88"  
X8888>  888888 '8888L  888R I888>  888E  888E   888R    888R I888> 888E  888E  d888 '88%"   4888> '    
?8888X   ?8888>'8888X  888R I888>  888E  888E   888R    888R I888> 888E  888E  8888.+"      4888>      
 8888X h  8888 '8888~ u8888cJ888   888E  888F   888R   u8888cJ888  888E  888E  8888L       .d888L .+   
  ?888  -:8*"  <888"   "*888*P"   .888N..888   .888B .  "*888*P"   888& .888E  '8888c. .+  ^"8888*"    
   `*88.      :88%       'Y"       `"888*""    ^*888%     'Y"      *888" 888&   "88888%       "Y"      
      ^"~====""`                      ""         "%                 `"   "888E    "YP'                 
                                                                   .dWi   `88E                         
                                                                   4888~  J^"===*"`                          
                                        made by Boat on boat
                                                                   """)
import smtplib

from email.mime.text import MIMEText
print("\033[37m----------------------------------------")
print("     1.mail sender~~~")
print("     2.socket hacker")
print("----------------------------------------")
c = input('select>')
if c == '1':
    print("mail Sender...start")
    print("______________________________________")
    print("Google Mail , Google password\033[36m")
    ID = input("Google Mail:")
    Password = input("Google password:")
    title = input("title:")
    RRR = input("to~:")
    what = input("content:")
    time = input("how many?:")
    print("starting...")
    msg = MIMEText(what, "html", _charset="utf-8")
    msg['Subject'] = title
    msg['From'] = ID
    msg['To'] = RRR
    #msg['Date'] = Utils.formatdate(localtime=1)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(ID,Password)
    for i in range(int(time)):
         s.sendmail(ID, RRR, msg.as_string())
         print("\033[36m[",i+1,"]mail sending...")
    s.quit()
else:
	print("NO?")



