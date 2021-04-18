while True: 
    def calcLogic():
        num1 = float( input('Please Insert Number1: '))
        num2 = float( input('Please Insert Number2: '))
        operation = input('What would you like to do?( *, +, /, -,^,mod ): ')

        if operation == '+':
            print(num1 + num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '/':
            print(num1 / num2)
        elif operation == '^':
            print(num1 ** num2)
        elif operation == 'mod':
            print(num1 % num2)
        else:
            print('Choose between *, +, /, -,^,mod')
            calcLogic()

        yesNo = input('Would you like to use calculator service? ').lower()

        if yesNo == 'yes': 
            print('Calculator service in use')
            calcLogic()

        elif yesNo == 'no':
            quit()

