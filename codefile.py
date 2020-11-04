def getSum(n):  
    if(n < 0):
    	return -1     
    sum = 0
    while (n != 0):  
        
        sum = sum + (n % 10) 
        n = n//10
        
    return sum
    

