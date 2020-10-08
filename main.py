from input import ask, slowType
import bank
import soldier

slowType("You have been diagnosed with a deadly disease, you only have 2 years left to live")
print("what do you want to do?")
print("1) rob a bank")
print("2) become a soldier")

answer = ask(allowedAnswers=["1", "2"])

if answer == "1":
    bank.start()
elif answer == "2":
    soldier.start()
else:
    print("input invalid")
