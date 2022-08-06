#ERROR HANDLING

try:
    file = open("file.txt") #Opening a nonexistent file
    print("Opening file")

    a_dictionary = {"key":"value"} 
    print(a_dictionary["test"]) #Accessing a nonexistent element

except FileNotFoundError:
    file = open("file.txt", "w")
    print("Error Occured: Creating New File")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else: 
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")
    #raise TypeError("This is an error that I made up") #This will create an error no matter What


#Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)