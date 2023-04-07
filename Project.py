#Jack Krejci
#Programming Project 6
#Data Structures and Algorithms

#Bring in the Stack Class to work with
#Exception possibility checker 
class Empty(Exception):
    pass

#Stack class
class Stack:
    # Straight forward use of adapter patter, re-use Python List
    def __init__(self):
        self._data = [] # list as underlying storage

    def is_empty(self):
        """is stack empty"""
        return len(self._data) == 0

    def len(self):
        return len(self._data)

    def top(self):
        if self.is_empty():
            raise Empty()

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()

        return self._data.pop()

    def push(self, element):
        self._data.append(element)

#Function for arithmetic expression evaluation
def eval_expression(expression, val_stack, opp_stack):
    #Walk throught the expression and identify what goes in each stack and implement counter
    total_elements = 0
    for i in expression:
        #Catch errors
        if i == "*" or i == "/":
            return "Invalid operator"
        
        if i != "+" and i != "-":
            #Do this if the stacks for num1 and num2 isn't empty
            if val_stack.is_empty() == False and opp_stack.is_empty() == False:
                opperator = opp_stack.pop()
                x = val_stack.pop()
                y = i
                #Turn x and y into integer form and evaluate
                int_x = int(x)
                int_y = int(y)
                #Do the correct opperation
                if opperator == "+":
                    answer = int_x + int_y
                    val_stack.push(answer)
                elif opperator == "-":
                    answer = int_x - int_y
                    val_stack.push(answer)

            #If this is the first number being put into val_stack then we need to simply push it in
            else:
                    val_stack.push(i)

        #If it doesn't follow the above criteria we must be working with an opperator PUSH IT  
        else:
            if opp_stack.is_empty() == False:
                #Catch multiple opperation error
                return "Multiple Opperator Error"
            else:
                opp_stack.push(i)
                
    return val_stack.top()
        

#Main Code
expression = "3+5-3+3"
val_stack = Stack()
opp_stack = Stack()
exp_ans = eval_expression(expression, val_stack, opp_stack)

#Get the answer to the equation given
print("The answer to %s:" % expression, exp_ans)
