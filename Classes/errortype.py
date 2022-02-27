from os import path
class ErrorType:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.image = self.getImage()

    def getImage(self):
        file = f'assets/{self.name}.png'
        if path.exists(file):
            return file
        else:
            return None


errors = set([ErrorType('AssertionError', 'Raised when the assert statement fails.'),
              ErrorType(
    'AttributeError', 'Raised on the attribute assignment or reference fails.'),
    ErrorType(
    'EOFError', 'Raised when the input() function hits the end-of-file condition.'),
    ErrorType('FloatingPointError',
              'Raised when a floating point operation fails.'),
    ErrorType(
    'GeneratorExit', 'Raised when a generators close() method is called.'),
    ErrorType(
    'ImportError', 'Raised when the imported module is not found.'),
    ErrorType(
    'IndexError', 'Raised when the index of a sequence is out of range.'),
    ErrorType(
    'KeyError', 'Raised when a key is not found in a dictionary.'),
    ErrorType(
    'KeyboardInterrupt', 'Raised when the user hits the interrupt key(Ctrl+c or delete).'),
    ErrorType(
    'MemoryError', 'Raised when an operation runs out of memory.'),
    ErrorType(
    'NameError', 'Raised when a variable is not found in the local or global scope.'),
    ErrorType('NotImplementedError',
              'Raised by abstract methods.'),
    ErrorType(
    'OSError', 'Raised when a system operation causes a system-related error.'),
    ErrorType(
    'OverflowError', 'Raised when the result of an arithmetic operation is too large to be represented.'),
    ErrorType(
    'ReferenceError', 'Raised when a weak reference proxy is used to access a garbage collected referent.'),
    ErrorType(
    'RuntimeError', 'Raised when an error does not fall under any other category.'),
    ErrorType('StopIteration', 'Raised by the next() function to indicate that there is no further item to be returned by the iterator.'), ErrorType(
    'SyntaxError', 'Raised by the parser when a syntax error is encountered.'),
    ErrorType('IndentationError',
              'Raised when there is an incorrect indentation.'),
    ErrorType(
    'TabError', 'Raised when the indentation consists of inconsistent tabs and spaces.'),
    ErrorType(
    'SystemError', 'Raised when the interpreter detects internal error.'),
    ErrorType('SystemExit',
              'Raised by the sys.exit() function.'),
    ErrorType(
    'TypeError', 'Raised when a function or operation is applied to an object of an incorrect type.'),
    ErrorType(
    'UnboundLocalError', 'Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.'),
    ErrorType(
    'UnicodeError', 'Raised when a Unicode-related encoding or decoding error occurs.'),
    ErrorType(
    'UnicodeEncodeError', 'Raised when a Unicode-related error occurs during encoding.'),
    ErrorType(
    'UnicodeDecodeError', 'Raised when a Unicode-related error occurs during decoding.'),
    ErrorType(
    'UnicodeTranslateError', 'Raised when a Unicode-related error occurs during translation.'),
    ErrorType(
    'ValueError', 'Raised when a function gets an argument of correct type but improper value.'),
    ErrorType('ZeroDivisionError', 'Raised when the second operand of a division or module operation is zero.')])
