from class_diem import Diem

simpleList = []
for count in xrange(4):
    x = Diem("2001140339","112","ass")
    simpleList.append(x)
for diem in simpleList:
    print diem.mssv
