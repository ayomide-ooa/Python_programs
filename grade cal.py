#Grade Calculator program
print("Enter your scores for the subject below to know your grade\n")

#get the subject scores
math, eng, sci = float(input("Mathematics : ")), float(input("English Language: ")), float(input("Science : "))

#get the average score
getAverage = (math+eng+sci)//3
print("Average Score: \t", getAverage , "\n")

#check the average score to know grade
if getAverage > 100:
    print("Each scores input should not be more than 100")
elif getAverage >= 90:
    print("Grade A")
elif getAverage >= 80:
      print("Grade B")
elif getAverage >= 70:
       print(" Grade C")
elif getAverage >= 60:
      print(" Grade D")
elif getAverage < 60:
    print("Grade F")
else:
     print("Please enter a valid input")