# 🧬 Constructor Chaining in Python Using `super()`

## 📌 Description

This Python program demonstrates **constructor chaining** using inheritance and the `super()` function.
When an object of the child class `Derived` is created:

1. Parent class constructor executes first
2. Then child class constructor executes

---

## 🚀 Features

* Demonstrates **inheritance**
* Uses `super()` to call parent constructor
* Shows constructor execution order

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Base`

Contains constructor:

```python id="u8m3pl"
def __init__(self):
```

Prints:

```python id="f2x9qa"
Inside class Base default constructor
```

---

### 2️⃣ Child Class – `Derived`

Overrides constructor:

```python id="v7k4zx"
def __init__(self):
```

Uses:

```python id="n3q8mv"
super().__init__()
```

👉 Calls constructor of parent class `Base`.

Then prints:

```python id="p6m2pt"
Inside class Derived default constructor
```

---

## 💻 Code

```python id="a4x7pl"
class Base:
    def __init__(self):
        print("Inside class Base default constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside class Derived default constructor") 

if __name__ == "__main__":
    obj = Derived()
```
---

## ▶️ Output

```id="r1m8qa"
Inside class Base default constructor
Inside class Derived default constructor
```

---

## 🧠 Key Concepts

### ✔ Constructor Chaining

When constructors are called in sequence during inheritance.

Flow:

```text id="x5q2mv"
Derived() → Base() → Derived()
```

---

### ✔ `super()` Keyword

```python id="k9m3zx"
super().__init__()
```

👉 Calls constructor of parent class.

Without this line:

* Parent constructor will NOT execute automatically.

---

## 📚 Concepts Used

* Inheritance
* Constructor overriding
* Constructor chaining
* `super()` method

---

## ⚠️ Important Difference

### Without `super()`

```python id="d7x1pt"
class Derived(Base):
    def __init__(self):
        print("Derived constructor")
```

### Output

```text id="m4q8zx"
Derived constructor
```

👉 Parent constructor is skipped.

---

### With `super()`

```python id="b2m6qa"
super().__init__()
```

👉 Parent constructor runs first.

---

## 🎯 Why `super()` is Important

Used for:

* Reusing parent initialization code
* Avoiding duplicate code
* Maintaining inheritance chain

---

## 🔧 Future Improvements

* Add parameterized constructors
* Demonstrate multilevel inheritance
* Show multiple inheritance with `super()`
* Add constructor arguments

---

## 📄 License

This project is open-source and free to use.

