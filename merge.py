with open("dhairya.txt", "r") as f1, open("dhairya_copy.txt", "w") as f2, open("dhairya_copy2.txt", "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
print("Files merged successfully.")