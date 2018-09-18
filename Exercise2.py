number1 = int (input (" Enter a number 1"))
number2 = int (input (" Enter a number 2"))

result = (number1/number2)

roundDownresult = int(result)

if number1 % number2 != 0:

    if result > 0:

        print( int (roundDownresult + 1) )

    else:

        print(int(roundDownresult - 1))


else:

    print(roundDownresult)







