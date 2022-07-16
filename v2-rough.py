greeting = 'HAPPY BIRTHDAY'
#generate multiple strings(permutated) and store them in a list and then print them.



i=0
while i<len(greeting):
    greeting_list = []
    global letters_list
    letters_list = []

    for letter in greeting:
        letters_list.append(letter)
    print(greeting_list)
    print(letters_list)


    dummy = ''
    last_letter = letters_list.pop(-1)
    letters_list = letters_list.append(last_letter)
    print(letters_list)

    for i in range(len(letters_list)):
        dummy+=letters_list[i]

    print()
    print(len(greeting_list))
    print(greeting_list)
    print()
    i+=1

#n=len(greeting)
#for i in range(n):
#    print()

#def output(greeting):
#    for i in range(len(greeting)):
#        print(greeting[i])
