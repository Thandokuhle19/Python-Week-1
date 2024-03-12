# Python-Week-1
_Variable and Types:_
Variable -Basic unit of a program, assigned a value. 
Equal sign (=) is used as an assignment operator.
Variable names include upper and lower cases, including underscores, and usually begin with lowercases. It cannot begin with a number
There are several types of variable in python and they are: - Integers >> whole numbers (floats: decimal numbers), complex numbers(used                                                               for complex mathematical calculations), 
                                                            - Strings (collections of characters),
                                                            - Booleans (true or false values)
The plus sign (+) is used to join characters, when working in strings, but it does not add strings or numbers. 

_Data Structures:_
Data Structures - allow for storage of a list of values in a single 
One of the first data structure we will learn is a list. They contain a data type, which includes a list within a list.
Length of a list is determined by using length function [which is len()]. Eg, myList = ["apple","banana","cherry"]
                                                                              x = len(myList) >> this will print out what is inside the list, in order.
Set is similar to a lit, but differs in such that it contains unique elements and is declared by the use of curly braces. Eg, thisset = {"apple", "banana", "cherry"}
print(thisset) >> this will print out whatever is inside the "thisset", in no particular order

In a list, the order of your elements is important, unlike a set.
Tuples cannot but modified once they have been declared. This means that they are unchangeable, we cannot add or remove items after the tuple has been created. 
Tuples use round brackets. Eg, thistuple = ("apple","banana","cherry") 
                           print(thistuple)

 _Operators:_
Operators: instructions that perform operations on variable and values. Familiar type operator is the arithmetic, used for mathematical calculations.
Example of arithmetic operator are addition(+) for adding numbers together, multiplication(*) for mulitplying numbers together, exponents(**) raises a number to a specified power, division(/) returns a floating-point value, even if the result is a whole number.
Modulus operator is specific to programming and gives the remainder after division. Eg, 20 % 6, the remainder will be 2, meaning it will return two. 
The addition operator for strings join, or combine two strings together, only working with two strings. Eg, 'string 1' + 'string 2', will show an output of 'string 1 string 2'.
Whereas with multiplication operator, repeats a string a certain number of times, working with either a string or a number. Eg, string1*2, will show an output of string1string1.
"And", "or", and "not" operate on boolean values. "And" returns true if both operators are true, "or" returns if at least one is true. "Not" denies the boolean.
Membership operators: - "in" and "not in" >> check if value is present or not. "In" to check if number or string is present in a list or string.

_Control Flow:_
There are three types of control flow in programming: 
    -If statement: Allows you to produce a block of code if that condition is met. 
    - Else statement: Produces a block of code is that condition is false. 
                   Example of an if and else statement: 
                   a = 2 
                   b = 5
                   if a < b:
                      print("a is smaller than b")   >> if the condition is met, it will produce the statement that is true.
                   else:
                       print("a is greater than b")  >> if the condition is false, it will produce the false statement.

A for loop is used to constantly repeat a list or any repeatable item. Eg, fruits = ["apple","banana","grapes"]
                                                                        for x in range (1,3):
                                                                            print(fruits[x])
A while loop keeps looping or keeps repeating until a cerain condition is false. You need to make sure that the condition in the loop becomes false, if not, it will loop forever.

_Functions:_
Function takes inputs and produces outputs.
Defined by using "def" keyword, followed by the function name and arguments in parenthesis. 
Eg, def my_function:
        print("Hello from function")
    my_function()
Function body is indented and contains code that performs the desired operation on the inputs, and the keyword "return" is used to specify the output.
Functions can only take one argument, and may or may not return a value.

_Classes and Objects:_
Classes help label and organise related collections. They are link object constructors, or a "blueprint" for creating objects.
For example, we can create a class called dog, which has multiple functions and attributes, such as legs, a name, and bark.
To define a class, we use an uppercase letter for the class name, we then define all functions and attributes inside the class definition.
We begin by creating a special function called initialization, or "init" function.



