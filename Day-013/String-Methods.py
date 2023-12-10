# strings are immutable
a = "!!!! !!!Harry!! !!!!!! Anjali"
print(len(a))
print(a)

print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace(a,"John"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the console!"
print(len(str1))
print(len(str1.center(50)))

print(str1.endswith("!"))
print(str1.find("t"))
# print(str1.index("g"))
print(str1.count("to"))

str2 = "WelcomeToTheConsole"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isprintable())

print(str1.isspace())
print(str1.istitle())
print(str1.swapcase())
print(str1.title())