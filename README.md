![image](https://github.com/Vaish22/Treasure_Island/assets/66295767/e1e66974-d3b1-424a-842f-4bdb1be1db2f)
How can you use the else statement with if in Python programming?

The ‘else’ statement is used with the ‘if’ statement in Python to execute a different block of code when the condition is false.
 Here is an example:

if the condition is true:
    statement present inside the if block
else:
    statement present inside the else block
If the condition is true, the statement present inside the if block will be executed. If the condition is false, the statement present inside the else block will be executed.

What is an elif statement in Python, and how it differs from if and else?

‘Elif’ stands for ‘else if’ and is used in Python programming to test multiple conditions. It is written following an if statement in Python to check an alternative condition if the first condition is false. The code block under the elif statement will be executed only if its condition is true.

What is the syntax of an if statement in Python?
The syntax for an if statement in Python is:

if condition1:
    statement to execute if condition1 is true
elif condition2:
    statement to execute if condition2 is true
else:
    statement to execute if both conditions are false
Here, 

If condition 1 is true, the statement present inside the if block will be executed. 
If condition 1 is false, then the elif condition will be checked. 
If the elif condition is true, the statement present inside the elif block will be executed. 
If both conditions are false, the statement present inside the else block will be executed.
How can you use multiple if statements in Python?
Multiple elif statements can be used in Python by nesting them inside one another. 

For example:

if condition1:
    statement to execute if condition1 is true
elif condition2:
    statement to execute if condition2 is true
elif condition3:
    statement to execute if condition3 is true
else:
    statement to execute if all conditions are false
Here,

 If condition 1 is true, the statement present inside the if block will be executed. If condition 1 is false, then the elif condition 2 will be checked. 
If condition 2 is true, the statement present inside the elif block will be executed. 
Similarly, if condition 3 is true, the statement present inside the elif block will be executed. 
If all conditions are false, the statement present inside the else block will be executed.
