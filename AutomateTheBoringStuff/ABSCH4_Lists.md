## Automate The Boring Things! CH4 Functions
#### Topics To Know
1. Getting Individual Values in a List with Indexes
2. Negative Indexes
3. Getting Sub-lists and Slices
4. Changing Values in a List with Indexes
5. List Concatenation and List Replication 
6. Removing Values from Lists using del
7. Mutable and Immutable Data Types
```python
array = ["Cat","Dog","Rat", "Giraffe"]
Dog = array[1]  # 1
Rat = array[-2]  # 2
sublist1 = array[0:-1]  # Cat Dog Rat  # 3
slice1 = array[:2]   # Cat Dog  # 3
array2 = array * 2  # "Cat","Dog","Rat", "Giraffe","Cat","Dog","Rat", "Giraffe"  # Replication
concatenation = [1, 2, 3] + ['A', 'B', 'C']  # [1, 2, 3, A, B, C]
del array[1]  # array = ["Cat", "Rat", "Giraffe"]  # 6
```
allmycats.py
```python
catNames = [] 
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input() 
if name == '':
    break
catNames = catNames + [name] # list concatenation
print('The cat names are:') 
for name in catNames:
    print(' ' + name)
```
```python
list("hello")  # ['h', 'e', 'l', 'l', 'o']
```
#### Pass by value
* variable assignments pass by value
```python
a = 40
b = a
b = 2
print(f"{a} and {b}") #  40 and 2
```

#### Pass by by Reference
* Lists will pass by reference
```python
a = [1,2,3]
b = a
a[0] = "a"
print(a)  # [a,2,3]
print(b)  # [a,2,3]
```

#### Mastery Questions
1. What does this expression evaluate to?
```python
ans = int("3"*2) / 11  # ans = 3  string value evaluates to 33
```
