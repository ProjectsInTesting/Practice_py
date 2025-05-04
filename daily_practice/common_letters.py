
def common_letter() :

    str1 = input("Enter your first String: ").lower()
    str2 = input("enter your second string: ").lower()

    # remove duplicate from string
    string1 = set(str1)
    string2 = set(str2)
    # print(string1)  to check before continue the code
    # print(string2)
    comm_let = string1 & string2
    if comm_let:
        print(f"{comm_let} : Common Letter")
    else:
        print("No Common letter")

common_letter()



