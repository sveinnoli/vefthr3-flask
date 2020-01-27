kt = [2902003030, 1111111111]
	
sum = 0
for x in kt:
    while (x != 0): 
        sum = sum + int(x % 10) 
        x = int(x/10) 
    print(sum)