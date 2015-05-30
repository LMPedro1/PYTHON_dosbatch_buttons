from Tkinter import *
import os
rootk = Tk()
Label(rootk, text='Click buttons to execute').pack()
rootk.title("Run Shell/Bat Files")
rootk.iconbitmap(default='img.ico')
Canvas(rootk, width=200, height=10).pack()

f = []
for line in open('files.txt','r'):
	#print(line)
	in_line = line[:-1]
	f.append(in_line)
size = len(f)
p = size / 2
#print "valor de n = size/2 --> ", p 
global m
global n
m = 1
n = 0
for i in range(p):
	exec("def RunShellBatFile%d(): os.system(f[%d])" % (m,m));
	exec("B%d = Button(rootk, text =f[%d], command = RunShellBatFile%d)" % (m,n,m));
	exec("B%d.pack()" % (m));
	m = m + 2
	n = n + 2
	separator = Frame(height=2, bd=1, relief=SUNKEN)
	separator.pack(fill=X, padx=5, pady=5)


rootk.mainloop()
