fh = open('Practical-10.txt', 'w')
a='10101'   # Number in Base 2
b=int(a,2)
fh.write(str(a) + ' in Base 2 = ' + str(b) + ' in Base 10')
fh.write("\n")
c=23       # Number in Base 10
d=bin(c)
fh.write(str(c) + ' in Base 10 = ' + d[2:] + ' in Base 2')
fh.close()
