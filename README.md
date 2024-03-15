 Python-Week-1
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

_Strings:_
There are numerous tools to analyse and construct strings, and slicing is one of the most useful tools.
Slicing is taking a portion of a string and returning it. 

_Byte:_
For bytes, it is done as ones and zeros, when computers store information.
Bytes is used for streaming files or transmitting texts without knowing the encoding.

_Lists:_
In this topic, we will dive deep into the methods of python.
append() method is a method used to add an item to the end of a list.
Eg, when we have a list called "myList" with the values containing 1,2,3,4, we can append the value of 5. 
We do this by typing myList.append(5), and it will print the myList.
We use the insert() method if we want to insert an item at a specific position in that list.
Eg, if we want to insert the value 10 at position 3 in myList, it will be myList.insert(3,10). It will print a new list in that specified position.
These are the two ways to remove items from a list: 
- remove(): removes an item based on its value, not its index. Eg, if we want to remove the integer 5 from myList, we type myList.remove(5) and it prints myList.
- pop(): removes and returns the items at the end of the list. Eg, if we write myList.pop() and then print myList, it will remove the last item of myList.
- cpoy(): to make a copy of a list so that the changes of the one list do not affect the other.Eg, we have a list with values from 1 to 5 and we want a copy of it, we will type b = a.copy(). It will return a copy of that specified list, which is 'a' in this case, thus printing out values from 1 to 5.
When we assign a list to a variable, the variable stores a reference not a copy of the list. Meaning, we need to modify the list through one variable hencefourth changes will show in other variable that reference the same list.

_Tuples and Sets:_
We will explain more of sets and tuples in this section.
*Sets*
As mentioned before, sets are defined by using curly brackets, like this {'a','b','c'}
However, we can also define it by passing an iterable object in the constructor of the set class. We use it like this: mySet = set(('a','b','c'))
We can create a list with some duplicates and de-deuplicate it by converting it to set and back again.
Eg, thisSet = {'b', 'c', 'c'} 
mySet = list(set(thisSet))
print(mySet)
The above code will print {'b','c'}, meaning myList passed its list to mySet and did not print the duplicates.
To determine how many items a set has or the length of the set, we use the len() function. 
Eg, mySet = {'b','c','c'}
    print(len(mySet))  it will print the integer 3, and this is because there are three items in the list/set.
We cannot access elements in a set using an index or slicing index. But, we can add elements to a set by using "add()" function and remove by using "discard" function.

*Tuples*
As mentioned before, tuples use parathesis insead of square brackets.
So, tuples are indexed, that being said, the first item has index[0], the second item has index[1], etc,
Tuples have a defined order, the oder does not change. We cannot change tuples, meaning we cannot add, change, or remove items once the tuple has been created. 
They allow duplicates since tuples are indexed, and can have items with the same value.


_Control Flow:_
We have spoken about control flows, however, we will dive deep into them.
This topic is important for writing most programs.
In other programming languages there is switch statement. This statement analyses a series of values and runs the code instructions that correspond to the first true value.
However, in python, there "replacements" for switch cases and they are:

- Switch case using Dictionary mapping:

- Using an If-else: Is used to determine whether a specific statment or block of statements. So, the block of statements will be performed or not, that is, whether a block of statements will be executed if a specific condition is true or not.
- Using a class: we are using a class to create a switch method
