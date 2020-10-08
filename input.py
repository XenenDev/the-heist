from time import sleep as wait

def ask(message = "", allowedAnswers = ["yes", "no", "n", "y"], falseInputResponce = "input not understood"):
    answer = input(message).lower().strip()

    if answer in allowedAnswers:
        return answer
    else:
        print(falseInputResponce)

def choice(choices, prompt = "",falseInputResponce = "input not understood"):
    i = 0

    for choice in choices:
        i += 1
        print(f"{str(i)}) {choice}")

    answer = input(prompt).lower().strip()

    if len(choices) >= int(answer) > 0:
        return int(answer)
    else:
        print(falseInputResponce)

def slowType(value, delay=0.1):
    for i in range(len(value)):
        wait(delay)
        print(value[i], end="")
    print("")
