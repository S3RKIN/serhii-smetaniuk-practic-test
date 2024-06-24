str1 = "Hello"
str2 = "World"
combo1 = (len(str1) > 3) and (str2 == "World")  
combo2 = (str1 != str2) and (str2 != "")   
combo3 = (len(str1) < 3) and (str2 == "Hello")
combo4 = (str1 == str2) and (str2 == "")       
print(combo1)
print(combo2)
print(combo3)
print(combo4)