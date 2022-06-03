n = int(input('enter the no from 0 to 99'))
d = {0:'zero',1:'one',2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'TWELVE',13:'THIRTEEN',
14:'FOURTEEN',15:'FIFTEEN',16:'SIXTEEN',17:'SEVENTEEN',18:'EIGHTEEN',19:'NINTEEN'}
d1 = {2:'twenty', 3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty'}
n2=n%10  #unit gigit
n3=n//10  #tenth digit
n4=n3-2
print(n4)
if n<20:
    print(d[n])
if n2==0:    
    print(d1[n4])
else:
    print(d1[n4]+''+d[n2])