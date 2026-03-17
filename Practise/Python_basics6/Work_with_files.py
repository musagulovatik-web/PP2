import os
import shutil
with open("Data.txt", "a+") as f:
    f.write("By Cesar Vallejo I'm sitting here on the old patio beside your absence. It is a black well. We'd be playing, now. . . I can hear Mama yell Boys! Calm down! We'd laugh, and off I'd go to hide where you'd never look. . . under...")
    f.seek(0)
    print(f.read())
    shutil.copy2("Data.txt", "Data.txt")
with open("Data.txt", "w+") as f:
    f.write("Now i am deleting all content")
    f.close()
    if os.path.exists("Data.txt"):
        os.remove("Data.txt")