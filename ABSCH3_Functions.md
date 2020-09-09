## Automate The Boring Things! CH3 Functions

### Define, Call, Pass, Argument, Parameter

A value being passed to a function is a called an *Argument*<br>
Variables that have arguments assigned to them are *Parameters*
```python
def sayHi(name):
    print(f"Hi, {name}")

sayHi('Victor')
```
In this case <span style="blue">*Victor*</span> is the <span style="blue">*argument*</span> and <span style="green">*name*</span>
is the <span style="green">*parameter*</span>

### Local and Global

* Local Variables can't be used in the Global Scope
* Local Scopes Cant use Variables from other Local Scopes
* Global Variables can be read from a Local Scope

### Mastery Questions
Why are functions Advantageous in programing?<br>
* *Reduces duplicate code, making it shorter, thus easier to read and update*

What's the difference between a **function** and **function call**?
* Function: you define what the function will do when it is called upon (cake recipe)
* Function Call: this is the actual operation that was defined in the function (the tasty cake)

What's a **Return Value**? Can a return value be a part of an expression?
* It is the value that a function call evaluates to.
* Like any value a return value can also be used in an expression.

If a function does not have a return statement, what is the return value of a call to that function?
* With no return it would return as `None` (which is a sort of null data-type)

How do you prevent a program from crashing?
* One method is to use is to place the line of code in a `try` clause

What goes in the `try`clause? What goes in the `Except` clause?
* Code that could cause an issue: `try`
* Code that executes if an error does occur: `except`

