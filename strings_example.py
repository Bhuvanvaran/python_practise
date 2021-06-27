# Strings are sequence of characters either it can be in single quotes or doube quotes
def single_quote():
    single_quoted_string = 'hello'
    print(single_quoted_string)


# Example for printing string in double quotes with singel quotes in it
def double_quote():
    double_quoted_string = "I'm the world"
    print(double_quoted_string)


# Example for printing stirng in new line
def new_line():
    new_line_string = "Hello I'm a new learner \nThanks \nBhuvan"
    print(new_line_string)


# Example for inbuilt len method in java we use to take strings using string.lenght() but here it is straight forward
def lenght_of_the_string():
    lenght_of_the_strin = "Hello "
    print(len(lenght_of_the_strin))


# String indexing
def positive_indexing():
    mystring = "Hello World"
    print(mystring[0])


# Negative indexing
def negative_indexing():
    mystring = "Hello world"
    print(mystring[-1])


# Slicing string and retieving it's substring
# slicing from starting
def start_substring():
    mystring = "abcdefgh"
    print(mystring[:3])  # prints first 3 character not including 'd'
# slicing from backwards, slice from the given character
def backward_sbstring():
    mystring = "abcdefgh"
    print(mystring[3:])

# specific string slicing
def specific_string():
    mystring = "abcdefgh"
    print(mystring[3:6])
#step sizing the string
#example of :: syntax, this syntax simply prints entire charecters in the string
def step_size():
    mystring="abcdefgh"
    print(mystring[::])
#Example of jump sizing
def jump_characters():
    mystring="abcdefgh"
    print(mystring[::2])
#Example of jump sizing with slicing
def jump_slice():
    mystring = "abcdefgh"
    print(mystring[0:4:2])
#example
def examplea():
    mystring = "tinker"
    print(mystring[1:4])

#String functions
def string_functions():
    mystring = "Hello World"
    print("Print string in Upper case: " + mystring.upper())
    print("Printing string in lower case: " + mystring.lower())
    print(mystring.index('e'))
    print(mystring.capitalize())
    print(mystring.casefold())
    print(mystring.endswith('d'))
    print(mystring.split())
#Formating Strings
def format_string():
    mystrings="Bhuvan has knowledge on {} {}"
    print(mystrings.format('java','python'))
def format_string2():
    str='Bhuvan'
    mystrings = "The Length of the string is {length}"
    print(mystrings.format(length=len(str)))
def f_string_method():
    str = 'Bhuvan'
    mystrings = f"The Length of the string is {len(str)}"
    print(mystrings)
#padding strings left and right padding
def right_allignment():
    mystring = "Bhuvan"
    print('{:>10}'.format(mystring)) #insert > next to :
def allign_with_underscore():
    mystring = 'Bhuvan'
    print('{:_>10}'.format(mystring)) #insert _> next to :
def allign_center():
    mystring = 'Bhuvan'
    print('{:^10}'.format(mystring)) #inset ^ next to :
#Truncate the string using format
def truncate_string():
    mystring = 'HelloThere'
    print('{:.5}'.format(mystring)) #insert . next to :
#Truncating and padding
def truncate_and_padding():
    mystring = 'HelloThere'
    print('{:10.5}'.format(mystring))
if __name__ == '__main__':
    # single_quote()
    # double_quote()
    # new_line()
    # lenght_of_the_string()
    # positive_indexing()
    # negative_indexing()
    #start_substring()
    #backward_sbstring()
    #specific_string()
    #step_size()
    #jump_characters()
    #jump_slice()
    #examplea()
    #string_functions()
    format_string2()
    f_string_method()
    right_allignment()
    allign_with_underscore()
    allign_center()
    truncate_string()
    truncate_and_padding()
