miText = "This training is for str "
result = miText[3]
print(result)
result = miText.index("ain")
print(result)

myAbc="ABCDEFGHhijk123465789"
myfrag = myAbc[0::2]
print((myfrag))
myreverse = myAbc[::-1]
print(myreverse)

print(myAbc.upper())
print(myAbc.lower())
print(myAbc.split("H"))
myspace =" "

print(myAbc.join([myspace,miText,myspace,myreverse]))
myList = ["a", "bcd", "123"]
print(" - ".join(myList))
print(myAbc.replace("A","z"))

myPoema="""Hola este
es mi poema en
diferentes lineas"""
print(myPoema)
print("Hola" in myPoema)
print(len(myPoema))
