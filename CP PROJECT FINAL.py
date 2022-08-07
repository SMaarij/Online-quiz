#_________WALIYA'S_MODULE_____________
def Display(n):
        'Function Display() is directed to display the Questions and calculate score accordingly.'                     
        with open(n,encoding='utf-8-sig') as f:                                                            
                count=0
                lines=f.read()
                i=lines.split('\n')                                                       
                for p in range(0,len(i),5):
                        while True:
                                print(i[p],i[p+1],i[p+2],i[p+3],sep='\n')                           
                                m=input('your answer: ')
                                print()
                                if m=='a' or m=='b' or m=='c':
                                        if m==i[p+4]:
                                                count+=1                                                
                                        break
                                else:
                                        print('Please enter valid choice and choose again')
                                        continue                           
                print('your marks are:',count)
#_________RAYYAN'S_MODULE_____________
def diff():
        'Function diff() helps user choose the difficulty level of quiz he/she wants to attempt.'
        print('Select difficulty level?\na.Moderate\nb.Master level')
        u=input('Your choice(a,b):')                                                     
        print()
        return u                                                                      
def Family_Easy():
        'Function Family_Easy() displays Questions in the domain of Family Trivia, the Moderate level'
        n='CS21034_1.txt'
        Display(n)
def Religious_Master():
        'Function Religious_Master() displays Questions in the domain of Religious Trivia, the Master level'
        n='CS21034_6.txt'
        Display(n)
def Religious_Easy():
        'Function Religious_Easy() displays Questions in the domain of Religious Trivia, the Moderate level'
        n='CS21034_5.txt'
        Display(n)
def Family_Master():
         'Function Family_Master() displays Questions in the domain of Family Trivia, the Master level'
         n='CS21034_2.txt'
         Display(n)
def GK_Easy():
        'Function GK_Easy() displays Questions in the domain of General Knowledge Trivia, the Moderate level'
        n='CS21034_3.txt'
        Display(n)
def GK_Master():
         'Function GK_Master() displays Questions in the domain of General knowledge Trivia, the Master level'
         n='CS21034_4.txt'
         Display(n)
#_________MARIJ'S_MODULE_______________
def student():
        'Function student() asks the student which domain he/she wants to attempt and proceed accordingly'
        while True:
            print('Which portion do you want to attempt?')
            print('a.Family Trivia\nb.General Knowledge\nc.Religious Trivia')
            o=input('Your choice(a,b,c):')                                     
            print()
            if o=='a':
                u=diff()
                if u=='a':
                        Family_Easy()
                elif u=='b':
                        Family_Master()
            elif o=='b':
                u=diff()
                if u=='a':
                        GK_Easy()
                elif u=='b':
                        GK_Master()
            elif o=='c':
                u=diff()
                if u=='a':
                        Religious_Easy()
                elif u=='b':
                        Religious_Master()
            choice=input('Dear student,do you want to attempt again?(y/n)\n')
            if choice=='y':
                continue
            else:
                break
#__________RAYYAN'S_MODULE_______________
def Show_Quiz():
        'Function Show_Quiz() helps administrator view existing quizzes'
        print('Enter domain from which you want to read Questions:\na.Family Trivia\nb.General Knowledge\nc.Religious Trivia')
        domain=input('enter your choice(a,b,c): ')
        print()
        if domain=='a':
                u=diff()
                if u=='a':
                    with open('CS21034_1.txt') as f:
                        print(f.read())                                                  
                elif u=='b':
                    with open('CS21034_2.txt') as f:
                        print(f.read())
        elif domain=='b':
                u=diff()
                if u=='a':
                    with open('CS21034_3.txt') as f:
                        print(f.read())
                elif u=='b':
                    with open('CS21034_4.txt') as f:
                        print(f.read())
        elif domain=='c':
                u=diff()
                if u=='a':
                    with open('CS21034_5.txt') as f:
                        print(f.read())
                elif u=='b':
                    with open('CS21034_6.txt') as f:
                        print(f.read())
#_________MARIJ'S_MODULE__________________
def append(n):
        'Function append() helps administrator add questions in exisiting quiz'
        with open(n,'a+') as k:                                                                          
                r=int(input('Enter number of Questions to be added:'))
                for m in range(1,r+1):
                        t=input('Enter in the given Format:\nQuestion,option1,option2,option3,correct option\n')    
                        t=t.split(',')                                                                               
                        for a in t:
                                k.write('\n'+a)                                                                      
#________WALIYA'S_MODULE_________________
def Add_Quiz():
        'Function Add_Quiz() allows the administrator to append in the quiz'
        print('Enter domain in which you want to add questions:\na.Family Trivia\nb.General Knowledge\nc.Religious Trivia')
        x=input('Enter your choice(a,b,c):')
        print()
        if x=='a':
                u=diff()
                if u=='a':
                        n='CS21034_1.txt'
                        append(n)
                elif u=='b':
                        n='CS21034_2.txt'
                        append(n)
        elif x=='b':
                u=diff()
                if u=='a':
                        n='CS21034_3.txt'
                        append(n)
                elif u=='b':
                        n='CS21034_4.txt'
                        append(n)
        elif x=='c':
                u=diff()
                if u=='a':
                        n='CS21034_5.txt'
                        append(n)
                elif u=='b':
                        n='CS21034_6.txt'
                        append(n)
def Analysis():
        'Function Analysis() helps Code Analyst view all the function used in the program'
        while True:
                print('Hey Analyst, What do you want to see?\na. Description of Functions.\nb. Project Details')
                g=input('Answer(a,b): ')
                if g=='a':
                    print('\n1. Display(n)\n2. diff()\n3. Family_Easy()\n4. Family_Master()\n5. GK_Easy()\n6. GK_Master()\n7.Religious_Easy()\n8. Religious_Master()\n9. student()\n10. Show_Quiz()\n11. append(n)\n12. Add_Quiz()\n13. Analysis()\n')
                    L=input('Enter your choice:')
                    if L=='1':
                          help(Display)
                          describe=input('\nDo you want to see the function code?(y/n)\n')
                          if describe=='y':
                                  with open ('functionss.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(0,18):
                                                  print(l[i])
                    elif L=='2':
                            help(diff)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(18,23):
                                                  print(l[i])            
                    elif L=='3':
                            help(Family_Easy)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(23,26):
                                                  print(l[i])
                    elif L=='4':
                            help(Family_Master)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(26,29):
                                                  print(l[i])
                    elif L=='5':
                            help(GK_Easy)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(29,32):
                                                  print(l[i])
                                    
                    elif L=='6':
                            help(GK_Master)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(32,35):
                                                  print(l[i])
                    elif L=='7':
                            help(Religious_Easy)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(35,38):
                                                  print(l[i])
                    elif L=='8':
                            help(Religious_Master)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(38,41):
                                                  print(l[i])
                    elif L=='9':
                            help(student)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(41,70):
                                                  print(l[i])
                    elif L=='10':
                            help(Show_Quiz)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(70,98):
                                                  print(l[i])

                    elif L=='11':
                            help(append)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                          a=f.read()
                                          l=a.split('\n')
                                          for i in range(98,106):
                                                  print(l[i])
                    elif L=='12':
                            help(Add_Quiz)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                            a=f.read()
                                            l=a.split('\n')
                                            for i in range(106,135):
                                                    print(l[i])
                    elif L=='13':
                            help(Analysis)
                            describe=input('\nDo you want to see the function code?(y/n)\n')
                            if describe=='y':
                                    with open ('CS21034_7.txt') as f:
                                            a=f.read()
                                            l=a.split('\n')
                                            for i in range(135,265):
                                                    print(l[i])
                            
                elif g=='b':
                        print('\nfile open krwani he\n')       
                else:
                        print('\nInvalid input\n')
                        break
#___________MAIN_MODULE_____________
while True:
    print('\t\t\t\tThe Sagacious Charlatans')
    print('Are u an administrator or a student?')
    x=input('a.Student\nb.Admin\nc.Code Analyst\nAnswer:')
    print()
    count=0
    if x=='a':
            student()
    elif x=='b':
        y=input('Enter username: ')                                                       
        z=input('Enter password: ')    
        if y=='project' and z=='cp':
            while True:
                print ('What do you want to do?\na. Show Quiz\nb. Add to existing quiz')
                a=input('Answer: ')
                print()
                if a=='a':
                        Show_Quiz()                                                     
                elif a=='b':
                        Add_Quiz()                                                      
                choice=input('Mr Administrator,do you want to do anything else?(y/n)\n')
                if choice=='y':
                    continue
                else:
                    break
        else:
                print('Enter valid username or password!!!!!')
    elif x=='c':
            Analysis()
    choice=input('Do you want to re-run the program?(y/n)\n')
    if choice=='y':
        continue
    else:
        break
