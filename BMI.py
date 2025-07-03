#program to calculate body mass index
weight = float(input("Enter weight in kilogram"))
height = float(input("Enter height in meters"))

BMI = weight/height**2
print(f"BMI is {BMI:.2f}")
if(BMI<18.5):
  print("Underweight")
elif(18.5<=BMI<24.9):
  print("Normal")
elif(25<=BMI<29.9):
  print("Overweight")
else:
  print("OBESITY!!")
