student_scores = input("Input a list of students scores ").split(" ")

max = 0

for i in student_scores:
    if(int(i) > max):
        max = int(i)

print(f"The highest score in the class is: {max}")