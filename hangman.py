#! /usr/bin/python2
an="lion tiger zebra elephant deer bear"
bd="crow eagle parrot duck penguin pigeon"
list1={'A':an,'B':bd}
optn=raw_input("Enter Category : A for Animal or B for Bird\n ")
a=list1[optn]
a= a.split()
import random
cd=random.randrange(len(a))
word=a[cd]
b=word[0]
hint=3
tries =0
cmpr=''
for i in range(len(word)):
    cmpr+='_'
print 'It is a '+str(len(word))+' letter word'
print 'You can enter ** if you want a hint\n'
while cmpr != word:
    ch=raw_input('Guess the Letter\n')
    if tries ==5:
        break
    if ch=='**':
        ans=raw_input("Do you want a Hint? (Y/N)\n")
        if ans=='y':
            if hint==0:
                print "No Hints left"
            else:
                hint-=1
                while b in cmpr:
                    b=random.choice(word)
                    print b
                for i in range(len(word)):
                    if word[i]==b:
                        cmpr=cmpr[0:i]+b+cmpr[i+1:]
                print cmpr
    elif ch in word:
        for i in range(len(word)):
            if word[i]==ch:
                cmpr=cmpr[0:i]+ch+cmpr[i+1:]
        print cmpr
    else:
        print 'Wrong Guess'
        tries+=1
if tries ==5:
    print 'YOU LOSE'.center(20,'(')
else: print 'YOU WIN'.center(20,')')
