import os
folders = os.listdir("data")

print(folders)

# for folder in folders:
#      print(os.listdir(f"data/{folder}"))

print(os.getcwd())                                                                             # to knwo about the current directory
os.chdir("/users")
print(os.getcwd)