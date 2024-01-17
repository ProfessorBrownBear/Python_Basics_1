Below are examples of various control structures and loops in Python, including accessing elements 
from a list (array) in each case. Note that Python does not have a built-in `switch-case` structure like 
some other languages, but we can simulate similar functionality using a dictionary or if-elif-else statements.

### 1. If-Then (If-Else) Example

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")
else:
    print("Apple is not in the list")
```

### 2. Simulating Switch-Case Using Dictionary

Python doesn't have a native switch-case construct. Here's how you can simulate it using a dictionary:

```python
def handle_apple():
    return "Handling an apple"

def handle_banana():
    return "Handling a banana"

def handle_default():
    return "Handling unknown fruit"

fruit_handler = {
    "apple": handle_apple,
    "banana": handle_banana
}

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    handler = fruit_handler.get(fruit, handle_default)
    print(handler())
```

### 3. For Loop Example

Iterating over a list using a for loop:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### 4. While Loop Example

Using a while loop to iterate over a list:

```python
fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

### Explanation:

- **If-Then (If-Else)**: This is used for conditional execution. The example checks if "apple" is in 
the list `fruits` and prints a message accordingly.
  
- **Simulating Switch-Case**: Python lacks a native switch-case statement, but you can mimic this 
functionality using a dictionary. This example maps fruit names to functions and calls the appropriate
function based on the fruit in the list.

- **For Loop**: This is used to iterate over each element in the list `fruits`. It's the most common 
way to loop through a list in Python.

- **While Loop**: This loop continues as long as the condition (`i < len(fruits)`) is true. It's used to 
iterate through the list elements by index.

These examples demonstrate basic ways to control the flow of a Python program and interact with lists. 
The simulated switch-case is less common but shows how Python's flexibility allows for creative solutions to certain problems.
