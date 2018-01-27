# -*- coding:utf-8 -*-
s = []
while True:
    try:
        s.append(input())
    except:
        break

for e in range(len(s)):
    st = list(map(str,s[e]))
    t = []
    for c in st:
        t.append(ord(c))    

    for i in range(26):
        string = ''
        for j in range(len(st)):
            if t[j] >= 97 and 122 >= t[j]:
                l = 97 + ((t[j] - 97 + i) % 26)
                string += chr(l)
            
            else:
                string += chr(t[j])
        if 'this' in string or 'the' in string or 'that' in string:
            print(string)
