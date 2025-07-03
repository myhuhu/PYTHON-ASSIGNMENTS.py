#program to check if person is eligible to vote
age = int(input("Enter your age"))
countries= input("Enter your Country (Kenya, Uganda, Tanzania:" )
East_Africa_Nationality= ["Kenya", "Uganda", "Tanzania"]
if(age >= 18 and East_Africa_Nationality=="yes"):
     print("You vote")
else:
     print("Not eligible to vote")
