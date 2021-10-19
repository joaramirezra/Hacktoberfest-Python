# making a marksheet

# creating function for percentage!
def percent(english, maths, chemistry, physics, biology):
    cent = ((english + chemistry + maths + physics + biology) / 500) * 100
    return cent


# Assigning variables by the user(input).
name = input("name of student: ")
F_name = input("Father name : ")
roll_no = input("roll no of student : ")
english = (int(input("obtained marks in english : ")))
maths = int(input("obtained marks in maths :"))
physics = int(input("obtained marks in physics : "))
chemistry = int(input("obtained marks in chemistry: "))
biology = int(input("obtained marks in biology : "))
marks_ob = (english + chemistry + maths + physics + biology)
print(f"obtained {marks_ob} out of 500")

perc = (percent(maths, chemistry, physics, english, biology))

pr = "%"  # assigning % to pr for concatenating with percentage!

# conditions for assigning grades!
print(str(perc) + pr)
if (perc > 90 and perc <= 100):
    print("grade: A+")
elif (perc >= 80 and perc <= 90):
    print("Grade: A")
elif (perc >= 70 and perc < 80):
    print("Grade: B")
elif (perc >= 60 and perc < 70):
    print("Grade: C")
elif (perc >= 50 and perc < 60):
    print("Grade: D")
else:
    print("Grade: F")















