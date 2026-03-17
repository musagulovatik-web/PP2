import os
os.chdir("Practise")
os.chdir("Python_basics6")
os.makedirs("My/Python/File1", exist_ok=True)
os.makedirs("My/C++/File2", exist_ok=True)
print(os.listdir("My"))
os.rename("My", "Your")
