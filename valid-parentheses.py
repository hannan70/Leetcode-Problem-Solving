
def isValid(s):

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            print("okay")
        else:
            print("not okay")


s = "()"
isValid(s)
