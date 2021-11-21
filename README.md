# cursethon
A few snippets of code I've made while coding in Python that I thought were interesting or 'cursed', per se.
The name of this repository is a portmanteau of 'cursed' and 'python', and this is a display repository showing some of the things I have made!

# Snippets

<details>
<summary> Context-based function overloading </summary>
  
<br>
Context-based function overloading is function overloading based off how the function was called syntactically. This snippet creates a `contextdispatch` decorator of which the decorator's most important argument is the regular expression for determining the syntactic context.

I'm sure this sounds a bit confusing, so let's take the following example:
```py
@contextdispatch
def print_single_digit(digit: int) -> None:
  print("print_single_digit was called!")
  print("The one's place is", digit)

# the argument in the decorator below is the regular expression for the decorator to determine the context matching
@print_single_digit.register(r"print_single_digit\(\d{2,\)")
def raise_error(number: int) -> None:
  print("print_single_digit wasn't called, raise_error was called though.")
  raise ValueError("The number you provided is not single digit!")
```
you might be thinking that this example is a bit frivolous when you can just use validation, but this is more of an example to show how this function works.

Now, let's say we do `print_single_digit(2)`, this will display the following:
```
print_single_digit was called!
The one's place is 2
```

however, if we do `print_single_digit(20)`, the context is matched with the regex for the `raise_error` function and that is dispatched to/called instead, so what happens is:
```
print_single_digit wasn't called, raise_error was called though.
ValueError: The number you provided is not single digit!
```
showing the function dispatching based on a syntactic context.

[See the source code here](https://github.com/Shom770/cursethon/blob/main/src/context_function_overloading.py)

</details>
