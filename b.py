print('***********************Converting number into WOrd********************')
n = int(input('enter no from 0 to 99,99,99,999:'))
num = {0:'zero', 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
        14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
n1 = {2:'twenty', 3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
n2 = {1:'one hundred', 2:'two hundred',3:'three hundred',4:'four hundred',5:'five hundred',6:'six hundred',
        7:'seven hundred',8:'eight hundred',9:'nine hundred'}
n3 = {1:'one thousand',2:'two thousand',3:'three thousand',4:'four thousand',5:'five thousand',6:'six thousand',
        7:'seven thousand',8:'eight thousand',9:'thousand'}
n4 = {1:'one lakh',2:'two lakh',3:'three lakh',4:'four lakh',5:'five lakh',
        6:'six lakh',7:'seven lakh',8:'eight lakh', 9:'nine lakh'}
n5 = {1:'one crore',2:'two crore',3:'three crore',4:'four crore',5:'five crore',
        6:'six crore',7:'seven crore',8:'eight crore', 9:'nine crore'}
if n<0 and n>999999999:
        print('invalid input')
elif n>=0 and n<19:
        print(num[n])
elif n>19 and n<=99:
        r = n%10 #unit digit
        r1 = n//10 #tenth digit
        if r==0:
                print(n1[r1])
        else:
                print(n1[r] + ' '+num[r1])
elif n>=100 and n<=999:
        r = (n%100)%10  #unit digit
        r1 = (n%100)//10 #tenth digit
        r2 = (n//100)  #hundred digit
        if r == 0 and r1 ==0:
                print(n2[r2])
        elif r ==0 and (r1 == 1 or r1 == 0):
                print(n2[r2]+ ' '+ 'and'+' '+num[r1])
        elif r==0 and r1>=2:
                print(n2[r2]+' '+'and'+' '+n1[r1]+' '+num[r])
        else:
                print(n2[r2]+' '+'and'+' '+n1[r1]+' '+num[r])
