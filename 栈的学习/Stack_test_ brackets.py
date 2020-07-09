from Stack import Stack

#if left brackets and right brackets is match return True
def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    for i in range (len(symbolString)):
        if symbolString[i] in "([{" :
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbolString[i]):
                    balanced = False
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{{([])}}'))

print(parChecker('{{(])'))