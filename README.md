# 🛠️ Learning Git Through Python Projects

This repository contains three beginner-to-intermediate Python projects built to **practice Git workflows**, including branching, merging, and maintaining clean commits—all while applying core programming concepts like file handling, OOP, and modularization.

Each project is self-contained inside its own folder and uses **JSON** for simple local data persistence. The overall goal is to build real-world CLI apps while learning proper version control practices.

---

## 📦 Included Projects

### 1. 📚 Bookstore Inventory Manager

A Python CLI tool for managing books in a bookstore. Supports adding, viewing, searching, and updating stock levels of books.

> 📁 Folder: `bookstore/`

Key Concepts:
- JSON file storage
- Custom `Book` class
- Input validation
- `math.ceil` for rounding prices
- Modular structure (`book.py`, `inventory.py`, `main.py`)

---

### 2. 🧾 Personal Budget Tracker

Track and categorize your daily expenses. View summaries grouped by category with totals automatically calculated.

> 📁 Folder: `budget_tracker/`

Key Concepts:
- `datetime` for working with dates
- Exception handling for user inputs
- Categorized summaries using `collections.defaultdict`
- JSON persistence
- Input loop and dynamic date parsing

---

### 3. 🧑‍🎓 Student Record Manager

A CLI tool for managing academic records of students. Supports multiple subjects, calculates averages and grades, and handles data updates and deletion.

> 📁 Folder: `student_record_manager/`

Key Concepts:
- Average & grade calculation
- Nested dictionaries for subjects/scores
- Error handling and input validation
- JSON for persistence
- CRUD operations via menu-driven CLI

---

## 🎯 Purpose of This Repository

This repository is designed to help you:

- Practice **Git version control** using real features:
  - `git branch`
  - `git checkout -b`
  - `git merge`
  - `git commit`, `add`, `push`, etc.

- Build working command-line tools in **Python**
- Improve understanding of:
  - File I/O
  - Classes and objects
  - Modular programming
  - Exception handling

---

## 🔧 Getting Started

Each project has its own `README.md` with detailed instructions on how to run and use the application. No external libraries are required — just **Python 3.6+**.

You can run any project using:

```bash
cd project_folder
python main.py
```
## Recommended Workflow for Practicing Git

* For each feature or fix:

#### Create a new branch
`git checkout -b feature-xyz`

#### Work on your code

#### Stage and commit
```
git add .
git commit -m "Add feature xyz"
```

#### Merge when ready
```
git checkout main
git merge feature-xyz
```