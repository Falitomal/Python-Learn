myText = (input("INPUT TEXT: \n"))
myText.lower()

myLetters = []
myLetters.append(input("INPUT A FIRST LETTER: \n").lower())
myLetters.append(input("INPUT A SECOND LETTER: \n").lower())
myLetters.append(input("INPUT A THIRST LETTER: \n").lower())

print(f"\n RESULT INPUT IS")
print(f"\nYOUR TEXT INPUT IS \n '{myText}'")
print(f"\nYOURS LETTERS INPUT IS \n {myLetters}")

print(f"\n 1-COUNT LETTERS FOUND ON TEXT")
lettcon1 = myText.count(myLetters[0])
lettcon2 = myText.count(myLetters[1])
lettcon3 = myText.count(myLetters[2])
print(f"The letter {myLetters[0]} is found a {lettcon1} times")
print(f"The letter {myLetters[1]} is found a  {lettcon2} times")
print(f"The Letter {myLetters[2]} is found a {lettcon3} times")

print(f"\n 2-COUNT STRING ON TEXT")
listText = myText.split()
print(f"The text has a number {len(listText)} of words")

print(f"\n 3-FIRST AND LAST LETTER ON TEXT")
print("First letter is: " + myText[0] + " and last letter is: " + myText[-1])

print(f"\n 4-REVERSE THE TEXT")
listText.reverse()
listTextReverse = " ".join(listText)
print(f"Reverse the text is :\n '{listTextReverse}'")

print(f"\n 5-FOUND WORD 'PYTHON'")
found_python = "python" in listText
dic = {True:"yes", False:"no"}
print(f"The word 'Python` {dic[found_python]}, if it is found in text")

