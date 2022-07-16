msg_sender = "J JEEVAN ROY" # 'HAPPY BIRTHDAY {name} FROM {sender}'.format(name,sender)

mystr = ' HAPPY BIRTHDAY '
print()
print('.'*100)
print()
name=input('YOUR BDAY SURPRISE IS WAITING FOR YOU. ENTER YOUR NAME ALL IN CAPS: ').upper()
mystr = mystr+name

#receiver
receiver = ''
for ele in name:
    receiver+=ele+'░'

sender = ''
for ele in msg_sender:
    sender+=ele+'░'

#sender


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
        dummy = dummy+ele+'░'
    greeting_list.append(dummy)
    #print(greeting_list)
    #print(dummy)
    #print(i)
    i+=1

for ele in greeting_list:
    for letter in ele:
        pass
        #print(letter)

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
print('-'*50)
top_bottom = "¨*•.¸¸.•*¨¨•.¸¸.•*•¨"
middle = "░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░ {} F░R░O░M░ {}"

middle = middle.format(receiver,sender)
print(middle)
len_int = int(len(middle)/21)+1
top_bottom = "ღ♪"+top_bottom*len_int+"♪ღ"
#print(top_bottom)
while len(top_bottom)-4!=len(middle) and len(top_bottom)-4>len(middle):
    middle = " "+middle
    if len(top_bottom)-4==len(middle) and len(top_bottom)-4<len(middle):
        break
    middle = middle+" "
    if len(top_bottom)-4==len(middle) and len(top_bottom)-4<len(middle):
        break


print('-'*len(middle))
middle = "ღ♪"+middle+"♪ღ"
print()
print('.'*len(middle))
print()
print('ONE MILLION WISHES!')
print()
print('.'*len(middle))
print()
print('Many more happy returns of the day to you '+name+' for One Million Times!')
print()
print('.'*len(middle))
print()
#print("ღ♪*•.¸¸.•*¨¨*•.¸¸.•*¨¨*•.¸¸.•*¨¨*•.¸.•*¨¨**•.¸¸.•*¨¨*•.¸¸.•*¨¨•.¸¸.•*•♪ღ♪")
print('-'*len(top_bottom))
print(top_bottom)
print(middle)
print(top_bottom)
print('-'*len(top_bottom))
print()
print('.'*len(middle))
print()
