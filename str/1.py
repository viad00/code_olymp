def clean(s, ss):
    g = ''
    for ch in s:
        if (ss.find(ch)!=-1):
            g += ch
    gg = ''
    for ch in ss:
        if (s.find(ch)!=-1):
            gg+=ch
    g = g.replace(' ','')
    gg = gg.replace(' ','')
    return g, gg
s1, s2 = clean(input(), input())
print(s1)
print(s2)
