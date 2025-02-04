---
theme: ./theme.json
author: Samuel Dostál
date: YYYY-MM-DD
paging: (%d/%d)
---

# Optimized Coding Environment for AOC
- Not how to solve problems
- How to solve them faster
- Assumes familiarity with AOC problem structure
<br>
&nbsp;&nbsp;**Presentation**
- *Choosing a language*
- *Algorithms*
- *Input parsing*
- *Tools*

---

# Choosing a language
- Balance **Familiarity** and **Efficiency**
<br>
- ~~Language performance~~
<br>
- String manipulation
- Memory management
- Concise syntax

---

# Choosing a language - [string comparison]
## Python
```python
a = "aaa"
b = "bbb"
print(a != b)
```

## C / C++
```c++
char* a = "aaa";
char* b = "bbb";
printf("%d", strcmp(a, b) != 0);
```

---

# Choosing a language - [string addition]
## Python
```python
a = "aaa"
b = "bbb"
print(a + b)
```

## Rust
```rust
let a = "aaa";
let b = "bbb";

let result = format!("{}{}", a, b);
println!("{}", result);
```
---

# Choosing a language - [memory management]
## Python
```python
arr = [1, 2, 3]
```

## C / C++
```c
int* arr = malloc(3 * sizeof(int));

arr[0] = 1;
arr[1] = 2;
arr[2] = 3;

free(arr);
```

---
# Choosing a language - [verbose syntax]
## Java
```java
public class Main {
    public static int xor(int a, int b) {
        return a ^ b;
    }

    public static void main(String[] args) {
        System.out.println(xor(1, 2));
    }
}
```

---
# Choosing a language
- Python, JavaScript, Go, Ruby, Kotlin = 😙🤌

---

# Be Prepared
- Templates & Common Algorithms
<br>
- Template file - `template.py`
- Common algorithms file - `common.py`

## Algorithms
- Graph / Grid traversal - BFS, DFS, Dijkstra - `18.py`
- Sorting algorithms, Binary search
- Dynamic programming (recursion)
- Regular expressions - `03.py`

---

# Grid traversal tip

```python
S##
###
##E

pos = (0, 0)
end = (2, 2)

```

---

# Grid traversal tip

```python
S##
###
##E

list_2d = ["S##", "###", "##E"]

pos = (0, 0)
end = (2, 2)

while pos != end:
    # look in all directions
    # ERROR: Index out of bounds [0, -1] = needs boundary check
```

---

# Grid traversal tip

```python
S##
###
##E

default_dict = { (0, 0) = "S", (0, 1) = "#", ... , (2, 2) = "E" }
default_dict.default = "X"

pos = (0, 0)
end = (2, 2)

while pos != end:
    # look in all directions
    # if neighbor is not 'X' = valid tile
```

---

# Automatization and Tooling
- regex101.com
- Advent of Code CLIs - `aocdl` / `aoc-cli`

## Bash
`aocdl -wait -output -force 01/input.txt`
