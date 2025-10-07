def checkFunction(ans):
    sols = int(input('Enter your Answer: '))
    if sols == ans:
                print('\n\n')
                print('                Correct Answer!')
    else:
                print('\n')
                print('xxxxxxxxxxx Incorrect answer! xxxxxxxxxx')
    
def main():
    fullOperators=[]
    firstOperand = []
    secondOperand = []
    correctAnswer = []
    while True:
        print('\n\n\n')
        print("********* FISRT FOUR pre-school *********")
        print('\n')
        print('*--------------------------------------*')
        print("*              Math Buddy              *")
        print('*--------------------------------------*')
        print('\n')
        print('Operations: +  -  x  / ')
        print('\n')
        print('1. Enter Problems')
        print('2. EXIT')
        print('\n')
        choice = input('      Enter choice (1/2): ')

        if choice == '1': 
            
            ops = input("Enter Operator [+  -  x  /] : ")
            
            fullOperators.append(ops)
        
            if ops == '+':
                try:
                    firstNumber = input("Enter Augend: ")
                    secondNumber = input("Enter Addend: ")
                    ans = int(firstNumber) + int(secondNumber)
                    checkFunction(ans)
                except ValueError:
                     print('\n')
                     print('---------------------------')
                     print("Error: Enter INTEGERS only.")
                     print('---------------------------')
                     continue

            elif ops == '-':
                try:
                    firstNumber = input("Enter Minuend: ")
                    secondNumber = input("Enter Subtrahend: ")
                    ans = int(firstNumber) - int(secondNumber)
                    checkFunction(ans)
                    
                except ValueError:
                     print('\n')
                     print('---------------------------')
                     print("Error: Enter INTEGERS only.")
                     print('---------------------------')
                     continue
                

            elif ops == 'x' or ops == 'X' or ops == '*' :
                try:
                    firstNumber = int(input("Enter Multiplier: "))
                    secondNumber = int(input("Enter Multiplicand: "))
                    ans = firstNumber * secondNumber
                    checkFunction(ans)
                except ValueError:
                     print('\n')
                     print('---------------------------')
                     print("Error: Enter INTEGERS only.")
                     print('---------------------------')
                     continue

            elif ops == '/':
                try:
                     
                    firstNumber = int(input("Enter Dividend: "))
                    secondNumber = int(input("Enter Divisor: "))
                    if secondNumber == 0:
                            print('\n')
                            print("----------------------------------------------------",end='')
                            print("\nxxx ERROR: You can't divide a number by zero. xxx")
                            print("----------------------------------------------------",end='')
                            continue
                    else:
                            ans = firstNumber / secondNumber
                            checkFunction(ans)
                except ValueError:
                     print('\n')
                     print('---------------------------')
                     print("Error: Enter INTEGERS only.")
                     print('---------------------------')
                     continue
              
                
            else:
                print('\n')
                print('--------------------')
                print("INVALID OPERATOR :( ")
                print('--------------------')
                continue
            
            firstOperand.append(firstNumber)
            secondOperand.append(secondNumber)
            correctAnswer.append(ans)
            print('\n\n')
           
            
            totalSums = int(len(fullOperators))
            
            
            print('\n', end='')
            for i in firstOperand:
                print(f"{i:>5}",end="     ")
            print('\n',end='')
            for i, j in zip(fullOperators, secondOperand):
                print(f"{i}{j:>4}",end="     ")
            print('\n',end='')
            
            i = 0
            for i in range(totalSums):
                print("-----", end="     ")
            print('\n',end='')
                
            
            for i in correctAnswer:
                print(f"{i:>5}",end= "     " )
            

        elif choice == '2':
            print('\n')
            print('           --------------------')
            print('           Exiting the program!         ')
            print('           --------------------')
            print('      Thank you for using Math Buddy!')
            print('\n')
            
            break
        else:
             print('\n')
             print('---------------------------')
             print('      INVALID ENTRY :(     ')
             print('---------------------------')
            
         
    
main() # <- 

