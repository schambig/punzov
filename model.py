'''
Compilor Data Model
AST = (Abstract Syntax Tree) This is a program representation through data structures.

var my_var = 6
var my_var2 = 9

my_var + my_var2

EXPR
STATEMENT
'''

class BinaryOperation:
    def __init__(self, operation, left_side, right_side):
        self.operation = operation
        self.left_side = left_side
        self.right_side = right_side

    def evaluate(self):
        if self.operation == '+':
            return self.left_side + self.right_side
        elif self.operation == '-':
            return self.left_side - self.right_side
        elif self.operation == '*':
            return self.left_side * self.right_side
        elif self.operation == '/':
            if self.right_side == 0:
                raise Exception('Can\'t divide by zero.')
            return self.left_side / self.right_side
        elif self.operation == '=':
            self.left_side.variable_value = self.right_side
            return self.right_side
        else:
            raise ValueError("Invalid operation")    

class VariableName:
    def __init__(self, variable_name):
        self.variable_name = variable_name
        self.variable_value = None

# Declaring
my_var1 = VariableName('my_var1')
my_var2 = VariableName('my_var2')

# Assigning
BinaryOperation('=', my_var1, 6).evaluate()
BinaryOperation('=', my_var2, 9).evaluate()

# Performing Operations
addtion = BinaryOperation('+', my_var1.variable_value, my_var2.variable_value).evaluate()
print(addtion)

subtraction = BinaryOperation('-', my_var1.variable_value, my_var2.variable_value).evaluate()
print(subtraction)

division = BinaryOperation('/', my_var1.variable_value, my_var2.variable_value).evaluate()
print(division)