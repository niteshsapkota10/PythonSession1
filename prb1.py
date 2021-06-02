string="Hello My name is Abcd"
newlist=[]
m=0
for c in range(len(string)):
    if string[c]==" ":
        newlist.append(string[m:c])
        m=c+1
newlist.append(string[m::])
print(newlist)
result=""
for i in newlist:
    result=result+" "+i[::-1]
print(result)

list1=["Nitesh","Pravhat","Riju","Kabita"]
print(list1)
list1[0],list1[len(list1)-1]=list1[len(list1)-1],list1[0]
print(list1)
list1[1],list1[len(list1)-2]=list1[len(list1)-2],list1[1]
print(list1)

list2=[1,2,3,4,5,6]
def swaplists(list2,pos1,pos2):
    list2[pos1],list2[pos2]=list2[pos2],list2[pos1]
    return list2

print(swaplists(list2,1,2))

string="helloWorldz"
print(ord('z'))

predesor="$zqashkaddsfnms"
successor="asdasbdnbad!@#"

newhashedString=""
for i in string:
    if(ord(i)==ord('z')):
        newhashedString=newhashedString+'a'
    else:
        newhashedString=newhashedString+chr(ord(i)+1)
result=predesor+str(len(newhashedString)+5)+newhashedString+str(len(newhashedString)+10)+successor
print(newhashedString)
print(result)

def decrypt(hashed_string):
    predesor="$zqashkaddsfnms"
    successor="asdasbdnbad!@#"
    new_string=hashed_string.replace(predesor,'')
    new_string=new_string.replace(successor,'')
    new_string=new_string.replace(new_string[0:2],'')
    decrpyted_string=""
    for i in new_string[:-2]:
        if(ord(i)==ord('a')):
            decrpyted_string=decrpyted_string+'z'
        else:
            decrpyted_string=decrpyted_string+chr(ord(i)-1)
    return decrpyted_string
    
print(decrypt(result))
# print(type(5))

def nameExchange(name):
    names=name.split(" ")
    names[0],names[1]=names[1],names[0]
    return ' '.join(names)

print(nameExchange("Nitesh Sapkota"))

def namesReverse(name):
    names=name.split(" ")
    names.reverse()
    return ' '.join(names)

print(namesReverse("My name is Nitesh"))
