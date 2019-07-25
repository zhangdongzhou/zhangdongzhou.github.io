# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:17:04 2017

@author: Dongzhou_X99
"""

import re
import os
#import time

# html name list
filenameL = ['allpub','condensedmatter', 'spectroscopy', 'uppermantle', 'lowermantle', 'core']

# Header list
headerL = ['All publications', 'Condensed matter physics and material science research', 'Optical and X-ray spectroscopy development', 'Earth science: crust, upper mantle and transition zone', 'Earth science: lower mantle ', 'Earth science: the core ']

# color list
colorL = ['#888', '#444', '#0ad', '#080', '#f80', '#f00']
colordim = '#bbb'

# Empty template, split mark  = ######

f1 = open('empty.html')
txt1 = f1.read()
L1 = re.split('######', txt1)
f1.close()

### split pdf list
f1 = open('pdf.txt')
txt1 = f1.read()
txt1 = txt1[0:-1]
L3 = re.split('\n', txt1)
f1.close()

###################
Num= 0
### cycle start
filename = '../texts/'+filenameL[Num]+'.html'
header = headerL[Num]
color = colorL[Num]

f2 = open('allpub.txt')
txt2 = f2.read()
txt2 = txt2[0:-1]
f2.close()
L2=re.split('</li>', txt2)
Numpub = len(L2)

txt5 = L1[0]+color+L1[1]+header+L1[2]
for i1 in range(len(L2)):
    txt3 = L2[i1]
    txt4 = re.split('<li>',txt3)[1]
    txt4split = re.search('\(2\d\d\d\)\, ',txt4)
    txt4_1 = txt4[0:txt4split.span()[1]]
    txt4_2 = txt4[txt4split.span()[1]:]
    txt4_f = txt4_1+'<a href="https://zhangdongzhou.github.io/pub/'+L3[i1]+'" style="color:'+color+'">'+txt4_2+'</a>'
    txt5 = txt5+'<li style=\"color:'+color+'\">'+txt4_f+'</li>\n'

txt5=txt5+L1[3]

f3 = open(filename,'w')
f3.write(txt5)
f3.close()
### cycle end

for i2 in range(1,6):
    Num = i2
    filename = '../texts/'+filenameL[Num]+'.html'
    header = headerL[Num]
    color = colorL[Num]
    
    f2 = open('allpub.txt')
    txt2 = f2.read()
    txt2 = txt2[0:-1]
    f2.close()
    L2=re.split('</li>', txt2)
    
    txt5 = L1[0]+color+L1[1]+header+L1[2]
    for i1 in range(len(L2)):
        txt3 = L2[i1]
        txt4 = re.split('<li>',txt3)[1]
        txt4split = re.search('\(2\d\d\d\)\, ',txt4)
        txt4_1 = txt4[0:txt4split.span()[1]]
        txt4_2 = txt4[txt4split.span()[1]:]
        #color determine
        i3 = int(re.split('<li>',txt3)[0])
        if i3==i2:
            color = colorL[Num]
        else:
            color = colordim
        txt4_f = txt4_1+'<a href="https://zhangdongzhou.github.io/pub/'+L3[i1]+'" style="color:'+color+'">'+txt4_2+'</a>'
        txt5 = txt5+'<li style=\"color:'+color+'\">'+txt4_f+'</li>\n'
    
    txt5=txt5+L1[3]
    
    f3 = open(filename,'w')
    f3.write(txt5)
    f3.close()


#update index.html

filename = '../index.html'
f4 = open(filename,'r')
txt6 = f4.read()
f4.close()
PS1t = '<div class=\"col-md-10\">'
PS1 = re.compile(PS1t)
L4 = PS1.split(txt6)
txt7 = L4[0]+PS1t
PS2t = 'height = \"'
PS2 = re.compile(PS2t)
L5 = PS2.split(L4[1])
txt7 = txt7+L5[0]+PS2t
PS3t = 'px\"'
PS3 = re.compile(PS3t)
L6 = PS3.split(L5[1])
newNum = str(int(71*Numpub+100))
txt7 = txt7+newNum+PS3t+L6[1]

os.remove(filename)

f5 = open(filename,'w')
f5.write(txt7)
f5.close()







