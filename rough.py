greeting = 'HAPPY BIRTHDAY'
#generate multiple strings(permutated) and store them in a list and then print them.

greeting_list = []
global letters_list
letters_list = []

for letter in greeting:
    letters_list.append(letter)
#print(greeting_list)
#print(letters_list)
dummy = ''
for ele in letters_list:
    dummy=dummy+ele
print(dummy)
greeting_list.append(dummy)
print(greeting_list)

i=0
while i<len(greeting)-1:
    last_letter = letters_list.pop(-1)
    letters_list = list(last_letter)+letters_list
    print(i)
    #print(letters_list)
    dummy = ''
    for ele in letters_list:
        dummy=dummy+ele
    print(dummy)
    greeting_list.append(dummy)
    i+=1
print(greeting_list)


    #dummy = ''
    #last_letter = letters_list.pop(-1)
    #letters_list = letters_list.append(last_letter)
    #print(letters_list)
