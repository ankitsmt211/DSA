def ispalindrom(number):
    temp=number
    reverse=0
    while(temp!=0):
        lastdigit=temp%10               # when we get remainder it gives us last digit of any number
        reverse=(reverse*10)+lastdigit  # reverse stores the reverse of our number
        temp=int(temp/10)               # once we got last digit in first step we wanted to remove it so we could get second last and so on
    if reverse==number:                 # if reverse of a number is equal to its original form it returns true
        return True
    else:
        return False
print(ispalindrom(232))
