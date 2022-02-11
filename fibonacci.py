
def isfib(value):

    val1 = 0

    val2 = 1

    while True:

        if val2 <= value:

            if val2 == value:

                return True

            else:

                tempval = val2

                val2 += val1
                val1 = tempval
        else:

            return False

n= int(input("Enter number:"))

number=n

fibonacci=isfib(number)

if (fibonacci):

    print("true")

elif n==0:

    print("true")

else:

    print("false")