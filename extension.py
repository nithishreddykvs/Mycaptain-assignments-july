file_name = input("Input the file name: ")
file_name_splitup = file_name.split(".")
extension = file_name_splitup[-1]
if extension == "py":
    print("The extension of the file is : python")
elif extension == "c":
    print("The extension of the file is  c language")
elif extension == "java":
    print("The extension of the file is java language")
else:
    print("Invalid extension")