## guessing number 
import random
i=0
numer=0
num = random.randint(1,9)
while numer!='no' and numer!=num:
        numer=input('do you want play game? (yes/no)')

        if numer=='no':
           break
       
        numer = int(input('enter number:'))
        i=i+1
        if numer < num:
           print('too low')
        elif numer > num:
           print ('too high')
        else:
           print ('you win')
           print('changing pass using %d',i)
           
        


