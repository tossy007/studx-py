# 🎓 Student Management System (Python CLI)

A simple command-line based Student Management System built in Python.  
Designed to help manage student records — adding, updating, deleting, and viewing student data — all stored in a JSON file for persistence.

Built during my freshman year as part of my journey to master Python 🙇‍♂
====================================================================================================
## 📌 Features

- Add new students with auto-generated unique IDs
- Update student name or age
- Delete student records
- View all student data
- Save and load data using JSON
===================================================================================================
## 🧠 Tech Stack

- Python 3.x
- JSON for persistent storage
- CLI (Command Line Interface)
===================================================================================================

## 🚀 How to Run

1. *Launch the script* and follow the menu prompts to manage student records.

### 🧾 How It Works

1. *Add Students*  
   - After adding a student, the system generates a unique *4-digit code*.  
   - This code is important — you’ll need it to retrieve, update, or delete that student’s data.

2. *Update Records*  
   - You can edit the name or age of any student — just make sure you have their 4-digit code.

3. *Delete Records*  
   - Want to remove a student? You can — but you’ll need their code to do it.

4. *Automatic Saving*  
   - All data is saved automatically behind the scenes using JSON.  
   - No need to worry about losing your progress — it’s handled for you.

---

### 🛠 Future Plans

I’m still learning and growing — so I plan to polish this project over time.  
Better menus, search features, maybe even a GUI someday.  
For now, this is my humble start .

## 📁 File Structure


student_management/
├── student_management.py   # Main Python script
├── Student.json            # Auto-generated data file
└── README.md               # Project documentation

## 🙇 Why I Built This🙇‍♂ 

I wanted to understand how real programs handle data — not just syntax.  
This project helped me learn:
- How to use dictionaries effectively
- How to persist data across sessions
- How to structure CLI-based programs
- How to think like a developer

---

## 💬 Final Note

This is a beginner-level project, but it means a lot to me.  
If you’re learning Python too — feel free to fork, improve, or explore.  
Let’s keep building, keep learning, and stay consistent 💪