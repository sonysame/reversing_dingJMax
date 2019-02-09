from pwn import*
f=open("answer",'r')

data=f.readline()
#data=data.split("7522")
a=[]
str=""
for i in range(0, len(data), 8):
	answer=u64(data[i:i+8])
	if(answer==0x402275):
		a.append("a")
		str+='a'
	elif(answer==0x402284):
		a.append("d")
		str+='d'
	elif(answer==0x40227f):
		a.append("f")
		str+='f'
	elif(answer==0x40227a):
		a.append("j")
		str+='j'
	elif(answer==0x402289):
		a.append("k")
		str+='k'
	else:
		print("ERROR")

print(str)
#print(data)
f.close()