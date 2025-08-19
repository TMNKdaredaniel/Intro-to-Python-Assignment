# README

## Overview

This Python script demonstrates basic list operations such as creating a list, appending elements, inserting elements at a specific position, extending the list with another list, removing elements, sorting, and finding the index of an element.

## Code Explanation

1. **Creating the list**  
   An empty list named `my_list` is created:
   ```python
   my_list = []
   ```

2. **Appending elements**  
   Elements `10`, `20`, `30`, and `40` are appended to the list using the `append()` method:
   ```python
   my_list.append(10)
   my_list.append(20)
   my_list.append(30)
   my_list.append(40)
   ```

3. **Inserting an element**  
   The value `15` is inserted at the second position (index 1) in the list using the `insert()` method:
   ```python
   my_list.insert(1, 15)
   ```

4. **Extending the list**  
   The list is extended by adding multiple elements `[50,ing the `extend()` method:
   ```python
   my_list.extend([50, 60, 70])
   ```

5. **Removing the last element**  
   The last element of the list is removed using the `pop()` method:
   ```python
   my_list.pop()
   ```

6. **Sorting the list**  
   The list is sorted in ascending order using the `sort()` method:
   ```python
   my_list.sort()
   ```

7. **Finding the index of an element**  
   The index of the value `30` in the list is found and stored in the variable `index_of_30`. It is then printed to the console:
   ```python
   index_of_30 = my_list.index(30)
   print(my_list.index(30))
   ```

## Result

After running the script, the final sorted list will be:

```
[10, 15, 20, 30, 40, 50, 60]
```

The printed output will be:

```
3
```

which is the index of the value `30` in the sorted list.

## Requirements

- Python 3.x

## How to run

Save the script in a `.py` file and run it using Python interpreter:

```bash
python script_name.py
```

Replace `script_name.py` with the actual filename.
