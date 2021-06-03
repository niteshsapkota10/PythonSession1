password="abcdez"
new_hashed="bcdefa"

print(chr(ord('a')+1))

a='z'
if(ord('z')==ord('a')):
    print(chr(ord('a')))

def my_hash(password):
    hashed_password=""
    for i in password:
        if(ord('z')==ord(i)):
            hashed_password=hashed_password+'a'
        else:
            hashed_password=hashed_password+chr(ord(i)+1)
    
    return "pbkdf2_sha256$216000$"+hashed_password+"/"

print(my_hash(password))


st='abcdez'
output=''
print(ord('z'))
for i in range(len(st)):
    if(ord(st[i])==ord('z')):
        output=output+chr(ord('a'))
    else:
        output=output+chr(ord(st[i])+1)
        len(output)*98

    
print(output)


# pswd1="pbkdf2_sha256$216000$R698njseKQzJ$csag927gjLU/x3IBY8MU9FPWhkplq3BCWo7cUMG1t7E="

# pswd2="pbkdf2_sha256$216000$umXQuyVB50j5$9+kuKCPmDSqjNDVXDmhIKlbp67OpaRR2xKm4dsiY25I="