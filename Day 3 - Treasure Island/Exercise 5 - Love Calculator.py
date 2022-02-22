list = ["true", "love"]

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n ")
name2 = input("What is their name?\n ")

combined = name1.lower() + name2.lower()

count = 0
first = ""
second = ""

for counter, letter in enumerate(list):
    for i in letter:
        count += combined.count(i)
    if counter == 0:
        first = str(count)
    else:
        second = str(count)
    count = 0

if first == "0":
    final = second
else:
    final = first + second

final = int(final)

if final < 10 or final > 90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif final >= 40 and final <= 50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")