a=int(input("Enter the obtained marks in matric = "))
b=int(input("Enter the total marks of matric = "))
c=int(input("Enter the obtained marks in first year = "))
d=int(input("Enter the total marks of first year = "))
e=int(input("Enter the obtained marks in Ecat = "))
f=int(input("Enter the total marks of Ecat = "))

per_matric=(a/b)*25
per_firstyear=(c/d)*45
per_ecat=(e/f)*30
total=per_ecat+per_firstyear+per_matric
print("Your Aggregate becomes = ",total)