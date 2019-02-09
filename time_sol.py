v15=0
answer2=[]
while(v15<=0xA513):
	if(v15 == 20 * ((0xCCCCCCCCCCCCCCCD *v15 >> 64) >> 4)):
		#print("PERFECT");
		answer2.append(v15)
	v15+=1
print(answer2)