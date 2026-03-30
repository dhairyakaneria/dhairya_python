src = open("dhairya.txt", "r")
data = src.read()
src.close()

dst = open("dhairya_copy.txt", "w")
dst.write(data)
dst.close() 
print("File copied successfully.")