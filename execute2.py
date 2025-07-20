
k=open("run-1.txt","r")
c=k.read()
a=int(c)
a=a+1
print("TOTAL EXECUTION TIME:",a)
k.close()
f=open('run-1.txt',"w")
a=int(c)
a=a+1
b=str(a)
f.write(b)
f.close()


