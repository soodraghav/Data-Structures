{\rtf1\ansi\ansicpg1252\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Reverse Strings:\
In this first exercise, the goal is to write a function that takes a string as\
input and then returns the reversed string. For example, if the input is the\
string "water", then the output should be "retaw".\
While you're working on the function and trying to figure out how to\
manipulate the string, it may help to use the print statement so you can\
see the effects of whatever you're trying.\
"""\
\
\
def string_reverser(our_string):\
    """\
    Reverse the input string\
    Args:\
       our_string(string): String to be reversed\
    Returns:\
       string: The reversed string\
    Time complexity:\
        for-loop: O(n)\
        Total: O(n)\
    Space complexity:\
        our_string: O(n)\
        rev_string: O(n)\
        Total: O(n+n) => O(n)\
    """\
\
    # TODO: Write your solution here\
    \
    reverse = ""\
    \
    for letter in our_string:\
        #print(letter)\
        reverse = letter + reverse\
        \
        \
    return reverse\
\
def string_reverser_pythonicway(our_string):\
    """\
    Time complexity:\
        string reverse: O(n)\
        Total: O(n)\
    Space complexity:\
        rev_string: O(n)\
        Total: O(n)\
    """\
    rev = our_string[::-1]\
    \
    return rev\
\
\
# Test Cases\
print('Reverse a string - The old fashonied way:')\
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")\
print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==\
                 string_reverser('Practicing string manipulation!'))\
      else "Fail")\
print("Pass" if ('3432 :si edoc esuoh ehT' ==\
                 string_reverser('The house code is: 2343')) else "Fail")\
\
print('Reverse a string - The Python Way:')\
print("Pass" if ('retaw' == string_reverser_pythonicway('water')) else "Fail")\
print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==\
                 string_reverser_pythonicway('Practicing '\
                                             'string manipulation!'))\
      else "Fail")\
print("Pass" if ('3432 :si edoc esuoh ehT' ==\
                 string_reverser_pythonicway('The house code '\
                                             'is: 2343')) else "Fail")}