# NumPy Basics – Exam & Interview Notes

## What is NumPy?

**NumPy (Numerical Python)** is a fundamental Python library used for **numerical computing**. It provides fast, memory‑efficient **N-dimensional arrays (ndarray)** and tools for performing mathematical operations on them.

---

## Why NumPy is Important

* Faster than Python lists (written in C)
* Uses less memory
* Supports vectorized operations
* Foundation for Pandas, SciPy, Scikit‑learn, TensorFlow

---

## Installation

```bash
pip install numpy
```

```python
import numpy as np
```

---

## NumPy Array (ndarray)

* Homogeneous (same data type)
* Fixed size
* Supports multi‑dimensional data

### Creating Arrays

```python
np.array([1, 2, 3])
np.zeros((2, 3))
np.ones((3, 3))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

---

## Array Attributes (Very Important for Exams)

```python
a = np.array([[1, 2], [3, 4]])
```

| Attribute | Meaning              |
| --------- | -------------------- |
| `a.ndim`  | Number of dimensions |
| `a.shape` | Rows & columns       |
| `a.size`  | Total elements       |
| `a.dtype` | Data type            |

---

## Array Indexing & Slicing

```python
a = np.array([10, 20, 30, 40])
a[0]        # 10
a[1:3]      # [20 30]
```

2D slicing:

```python
b = np.array([[1,2,3],[4,5,6]])
b[0, 1]     # 2
```

---

## Reshaping Arrays

```python
a = np.arange(6)
a.reshape(2, 3)
```

Other useful methods:

```python
a.flatten()
a.ravel()
```

---

## Mathematical Operations (Vectorization)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b
a * b
np.sqrt(a)
np.sum(a)
np.mean(a)
```

---

## Broadcasting

Allows operations on arrays of different shapes

```python
a = np.array([1, 2, 3])
a + 10
```

---

## Comparison & Boolean Masking

```python
a = np.array([10, 20, 30])
a > 15

a[a > 15]
```

---

## Random Module

```python
np.random.rand(3, 3)
np.random.randint(1, 10, size=5)
np.random.seed(42)
```

---

## Copy vs View (Very Important Interview Question)

```python
a = np.array([1, 2, 3])
b = a.view()
c = a.copy()
```

* **View** → shares memory
* **Copy** → new memory

---

## NumPy vs Python List

| NumPy      | List          |
| ---------- | ------------- |
| Faster     | Slower        |
| Fixed type | Mixed types   |
| Vectorized | Loop required |

---

## Common Exam / Interview Questions

### 1. What is NumPy?

Library for numerical computing using arrays.

### 2. What is ndarray?

N‑dimensional homogeneous array.

### 3. Why NumPy is faster than lists?

Uses C‑level operations & contiguous memory.

### 4. Difference between `reshape()` and `resize()`?

* `reshape()` → returns new view
* `resize()` → changes original array

### 5. What is broadcasting?

Applying operations on arrays with different shapes.

### 6. Difference between `flatten()` and `ravel()`?

* `flatten()` → copy
* `ravel()` → view

### 7. How to check shape and datatype?

```python
a.shape
a.dtype
```

### 8. What is vectorization?

Performing operations without loops.

---

## One‑Line Revision

> NumPy is the backbone of data analysis & machine learning in Python.

---

## Next Topics to Study

* NumPy linear algebra (`linalg`)
* Statistical functions
* File handling (`loadtxt`, `savetxt`)
* NumPy with Pandas

---

**Prepared for Exams & Interviews**
