print("Hello Simon!")
a1=[]
a2=[]
a3=[]
a1
with open(r'c:\Users\IMOE001\downloads\assign1_data.txt_\assign1_data.txt') as f:
	next(f) # skip 1 line
	next(f) # skip 1 line
	for line in f:
		data=line.split()
		a1.append(float(data[0]))
		a2.append(float(data[1]))
		a3.append(float(data[2]))
        
"""for i in a1:
    print(i, end = ' ')"""
