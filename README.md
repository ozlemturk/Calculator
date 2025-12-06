# 🧮 Tkinter Calculator
A fully functional calculator application built with Python's Tkinter library.  
Designed as a beginner-friendly yet clean and structured GUI project, this calculator replicates
the core behavior of modern digital calculators.

This project demonstrates:
- GUI layout with Tkinter
- Handling user input events
- Evaluating mathematical expressions
- Error handling and UI feedback
- Clean code structure using OOP principles

---

## 🚀 Features

### ✔ Basic Arithmetic
Supports all essential operations:
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)

### ✔ Additional Calculator Functions
- Percentage (%)
- Toggle sign (+/-)
- Decimal point support (.)
- Clear (CE)
- Equal (=)

### ✔ Dynamic Expression Display
- Small top text shows the ongoing input expression
- Large bottom text displays the computed result

### ✔ Error Handling
The calculator prevents:
- Division by zero  
- Output overflow (very long numbers)  
- Invalid expressions  

It provides clear visual error messages such as:
- `"ERROR"`
- `"Zero Division ERROR!"`

---

## 🏗 Architecture & Code Structure

The project is organized using a single class:

### **`Calculator` class**
Handles:
- Window initialization  
- UI construction (buttons, labels)  
- Expression management  
- All calculator logic and evaluation  

### Important Methods
| Method | Purpose |
|--------|---------|
| `create_buttons()` | Generates and places all calculator buttons using Tkinter's grid layout |
| `button_digit(d)` | Appends a pressed digit to the expression |
| `button_operator(op)` | Appends an operator (e.g., +, -, /) |
| `toggle_sign()` | Wraps the current expression to toggle its sign |
| `calculate()` | Safely evaluates the mathematical expression and prints result |
| `clear()` | Clears both input and result fields |

The UI automatically scales using configurable `ipadx`, `ipady`, and `columnspan` settings.

---

## 🖼 UI Preview (Example Layout)
<img width="348" height="351" alt="Ekran Resmi 2025-12-06 22 39 00" src="https://github.com/user-attachments/assets/b1a2d21c-3e6d-4930-ab7d-3c0090063799" />
<img width="348" height="345" alt="Ekran Resmi 2025-12-06 22 39 31" src="https://github.com/user-attachments/assets/d6396f24-eff3-4295-9d18-8b41f57931f4" />

