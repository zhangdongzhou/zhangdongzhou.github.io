# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:17:04 2017

@author: Dongzhou_X99
"""

import re

# html name list
filenameL = ['allpub','condensedmatter', 'spectroscopy', 'uppermantle', 'lowermantle', 'core']

# Header list
headerL = ['All publications', 'Condensed matter physics and material science research', 'Optical and X-ray spectroscopy development', 'Earth science: crust, upper mantle and transition zone', 'Earth science: lower mantle ', 'Earth science: the core ']

# color list
colorL = ['#888', '#444', '#0bb', '#080', '#f80', '#f00']
colordim = '#bbb'

# Empty template, split mark  = ######

f1 = open('empty.html')
txt1 = f1.read()
L1 = re.split('######', txt1)
f1.close()

###################
Num= 0
### cycle start
filename = filenameL[Num]+'.html'
header = headerL[Num]
color = colorL[Num]

f2 = open('allpub.txt')
txt2 = f2.read()
f2.close()
L2=re.split('</li>', txt2)

txt5 = L1[0]+color+L1[1]+header+L1[2]
for i1 in range(len(L2)):
    txt3 = L2[i1]
    txt4 = re.split('<li>',txt3)[1]
    txt5 = txt5+'<li style=\"color:'+color+'\">'+txt4+'</li>\n'

txt5=txt5+L1[3]

f3 = open(filename,'w')
f3.write(txt5)
f3.close()
### cycle end

for i2 in range(1,6):
    Num = i2
    filename = filenameL[Num]+'.html'
    header = headerL[Num]
    color = colorL[Num]
    
    f2 = open('allpub.txt')
    txt2 = f2.read()
    f2.close()
    L2=re.split('</li>', txt2)
    
    txt5 = L1[0]+color+L1[1]+header+L1[2]
    for i1 in range(len(L2)):
        txt3 = L2[i1]
        txt4 = re.split('<li>',txt3)[1]
        #color determine
        i3 = int(re.split('<li>',txt3)[0])
        if i3==i2:
            color = colorL[Num]
        else:
            color = colordim
        txt5 = txt5+'<li style=\"color:'+color+'\">'+txt4+'</li>\n'
    
    txt5=txt5+L1[3]
    
    f3 = open(filename,'w')
    f3.write(txt5)
    f3.close()











