# 1. write() Single String
f=open("one.txt","w")
f.write("Hello Students\n")
f.write("Welcome to Python file handling.\n")
f.write("Learning is Fun.\n")
f.close()

# 2. writelines() 
f=open("one.txt","w")
f.write("New content only.\n")
f.close()

# 3. Append mode
f = open("one.txt","a")
f = open("one.txt","w")
lines = [
    "Python Progamming.\n",
    "File Handling.\n",
    "Error Handling.\n",
    "Excepting Handling.\n",
]
f.writelines(lines)
f.close()