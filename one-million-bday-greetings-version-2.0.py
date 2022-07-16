mystr = ' HAPPY BIRTHDAY '

print()
print('.'*100)
print()
name=input('ENTER YOUR NAME ALL IN CAPS: ').upper()

mystr = mystr+name

letters_list,greeting_list = [],[]
for ele in mystr:
    letters_list.append(ele)

first_letter = letters_list.pop(0)
letters_list = letters_list+list(first_letter)

i=0
while i<len(mystr):
    last_letter = letters_list.pop(-1)
    letters_list = list(last_letter)+letters_list
    #print(letters_list)
    dummy = ''
    for ele in letters_list:
        dummy += ele
    greeting_list.append(dummy)
    #print(greeting_list)
    #print(dummy)
    #print(i)
    i+=1

#print(greeting_list)
print()
print('.'*100)
print()
j=1
while j<10*6+1:
    for ele in greeting_list:
        print(ele)
        #print(j)
        j+=1



while len(mystr)!=100:
    mystr = ' '+mystr
    if len(mystr)==100:
        break
    mystr = mystr+' '
    if len(mystr)==100:
        break

print('-'*100)
print()
print('.'*100)
print()
print('ONE MILLION WISHES!')
print()
print('.'*100)
print()
print('Many more happy returns of the day to you '+name+' for One Million Times!')
print()
print('.'*100)
print()
#print("ღ♪*•.¸¸.•*¨¨*•.¸¸.•*¨¨*•.¸¸.•*¨¨*•.¸.•*¨¨**•.¸¸.•*¨¨*•.¸¸.•*¨¨•.¸¸.•*•♪ღ♪")
print('-'*100)
print(mystr)#FINAL GREETING
print('-'*100)
print()
print('.'*100)
print()



#print("ღ♪*•.¸¸.•*¨¨*•.¸.•*¨¨*•.¸¸.•*•♪ღ♪")
#print("ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░♪ღ")
#print("•♪ღ♪*•.¸¸.•*¨¨*••*¨¨*•.¸¸.•*•♪ღ♪")
