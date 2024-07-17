#___________ Case Statements in PY__________________--

x=4
match x:
    case 0:
        print("x is Zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print("x, is not 90")
    case _ :
        print(x)