# Input
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
#############################################################
localNames = []
domainNames = []

''' Program validations '''
if 1<=len(emails)<=100:
  for email in emails:
    try:
      indice = email.index('@')

      if 1<=len(email)<=100:
        localEmail = email[:indice]
        dominioEmail = email[indice:]
          
        if len(localEmail) != 0 and len(dominioEmail) != 0:
          localNames.append(localEmail)
          domainNames.append(dominioEmail)
        else:
          print("empty local field name")
      else:
        print("Email character limit exceeded")
    except:
      print("Some email does not contain the @ character")
else:
  print("Mailing list exceeds limit")

for locales in localNames:
  if locales[0] == "+":
    break
for dominios in domainNames:
  if dominios[-4:] != '.com':
    break

def validatedEmails(emails):
    
    listaNombre_nueva = []
    listaDominio_nueva = []
    for elemento in localNames:
        e = elemento.lower()
        characters = "."
        for x in range(len(characters)):
            local = e.replace(characters[x],"")  

        letra = '+'
        if letra in local:
            indicenuevo = local.index('+')
            localnuevo =  local[:indicenuevo]
            listaNombre_nueva.append(localnuevo)
        else:
            listaNombre_nueva.append(local)
    
    for elemento in domainNames:
        e = elemento.lower()
        listaDominio_nueva.append(e)

    listafinal = []
    for i in range(len(listaNombre_nueva)):
        x = listaNombre_nueva[i] + listaDominio_nueva[i]
        listafinal.append(x)

    resultantList = []
     
    for element in listafinal:
        if element not in resultantList:
            resultantList.append(element)
        
    return len(resultantList)

# Output
a = validatedEmails(emails)
print(a)