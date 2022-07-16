def intro():
    global greetings
    greetings = 'HAPPY BIRTHDAY '
    print()
    print('.'*50)
    print()
    global name
    name = input('Enter your name in all caps: ')
    print()
    print('.'*50)
    print()

intro()

global greeting_output
greeting_output = greetings+name

def birthday_greetings():
    i=1
    while i<10**6+1:
        for letter in greeting_output:
            print(letter)

        print()
        print()

        if i==10**6:
            print('ONE MILLION TIMES!')
        else:
            print('{} times'.format(i))
        print()
        i+=1
    print()
    print('.'*len('Many more happy returns of the day to you '+name+' for one Million Times!'))
    print()
    print('Many more happy returns of the day to you '+name+' for one Million Times!')
    print()
    print('.'*len('Many more happy returns of the day to you '+name+' for one Million Times!'))
    print()

ready = ' '
while ready!='yes' and ready!='n':
    print()
    print('.'*50)
    print()
    ready = input('There is a surprise waiting for you. Are you ready? yes or no: ').lower()
    print()
    print('.'*50)
    print()

    if ready=='yes':
        birthday_greetings()
    elif ready=='no':
        print()
        print('.'*50)
        print()
        print("         Still the SURPRISE is waiting for you. Do not miss:)")
        print()
        print('.'*50)
        print()
