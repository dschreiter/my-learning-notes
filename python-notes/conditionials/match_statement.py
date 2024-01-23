#  same as switch statement
#A match statement compares a value to several different conditions until one is met. True or false?

http_status = 200

match http_status:
    case 200 | 201:
        print("success")
    case 400:
        print("not found")
    case 500 | 501:
        print("server error")
    case _:
        print("unknonw")
