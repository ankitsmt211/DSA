def countDigits(number):
    count=0
    if number==0:
        return 1
    try:    
        while number>0:
            number=int(number/10)
            count+=1
        return count
    except:
        print('Enter positive values in either decimal or integer form only')
print(countDigits(0))