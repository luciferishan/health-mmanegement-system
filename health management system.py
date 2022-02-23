import datetime
def gettime():
  return datetime.datetime.now()
while(True):

    uinp = input('''what you want to do : log or retrive
     for exit press : 0 \n''')
    if uinp == "log":
        ask = input("you want to log exercise or diet\n ")
        if ask == "diet":
            value = input("what did you eat")
            fun = open("harsh.txt", "a")
            fun.write(str(gettime()) + ":  " + value)
            print("successfully written")
            fun.close()
        elif ask == "exercise":
            value = input("which exercise have you done")
            fun = open("harsh.txt", "a")
            fun.write(str(gettime()) + "%I"+":  " + value)
            print("successfully written")
            fun.close()
    elif uinp == "retrive":
        ask = input("you want to retrive diet or exercise\n")
        if ask == "diet":
            fun = open("harsh.txt", "r")
            a = fun.read()
            print(a,"\n")
            fun.close()
        elif ask == "exercise":
            fun = open("harsh.txt", "r")
            a = fun.read()
            print(a,"\n")
            fun.close()

    else:
        break




