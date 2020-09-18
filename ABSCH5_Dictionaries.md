## Automate The Boring Things! CH3 Dictionaries

#### Dictionaries vs Lists

* Dictionaries are unordered, this means you can't refer by index like Lists
* Since they are unordered, You can't slice them like Lists

#### keys(), Values(), and items() methods
```python
ex_dict = {"color": 'red','age': '22', 'name': 'Brando'}

items = ex_dict.items()
values = ex_dict.values()
keys = ex_dict.keys()
```
These values are not returned as true lists so they can't be modified but they can be used in a for loop
```python
ex_dict = {"color": 'red','age': '22', 'name': 'Brando'}
items = ex_dict.items()  # dict_type([blah,blah,blah])
print(type(items))
print(items)
arr = []
for i in ex_dict.items():
    arr.append(i)

print(arr[0][1]) # red
```

#### Checking whether a Key or Value exists in a Dictionary
```python
ex_dict = {"color": 'red','age': '22', 'name': 'Brando'}
'name' in ex_dict  # True
'name' in ex_dict.keys()  # True
'Brando' in ex_dict.values()  # True
```
Searching in a dictionary only finds keys, not values.
#### The get() Method
checks and "gets" the value in a dictionary, if the key is missing then a **KeyError** will occuer
```python
ex_dict = {"color": 'red','age': '22', 'name': 'Brando'}

print(f"{ex_dict.get('name')} is {ex_dict.get('age')}, and he's {ex_dict.get('color')} because of his sunburn.")
# Brandon is 22, and hes red because of his sunburn.
```
##### setdefault() Method
If and only if a key-value is non-existent. Use  **setdefault()** to set a new key-value pair in a dictionary
```python
ex_dict = {"color": 'red','age': '22',}
ex_dict.setdefault('name', 'Brando')
print(f"{ex_dict.get('name')} is {ex_dict.get('age')}, and he's {ex_dict.get('color')} because of his sunburn.")
# Brandon is 22, and hes red because of his sunburn.
```
#### Using Data structures to Model Real-World Things
We can use a hashmap to chart grid locations like the positions of a *Chess Board*. A Tic Tac Toe Hash is a simplified
chess board so our first example with that.
