# re code replace function

strTest = input("Enter a String : ")
toReplace = input("To Replace ? : ")
rWith = input("To Replace With ? : ")

resultingString = strTest[:strTest.find(toReplace)] + rWith + strTest[strTest.find(toReplace)+ len(toReplace):]

print(resultingString)