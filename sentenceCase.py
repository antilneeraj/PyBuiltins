from os import system

system("cls")
string = input("Enter a String : ").strip().lower().capitalize()
_str = string.replace(". ", ".")

ind = 0;

for i in range(_str.count(".")):
    wrdRep = _str[_str.index(".", ind)+1];
    string = _str = _str[:_str.index(".", ind)+1] + wrdRep.upper() + _str[_str.index(".", ind)+1+len(wrdRep):]
    ind = (_str.index('.', ind))+1


string = string.replace(".", ". ")
print(string)