# Grade Generator Calculator
This is a two-part project where I built an interactive Python application that calculates a student's final grade by prompting the user for assignment details, and a Bash script that archives the generated CSV files with timestamps.

---

## Overview
Automation for the management of grades on two levels:
* Grade Generator (Python) - For the computation of weighted grades as well as GPAs, and pass and fail states
* Organizer (Bash) - Performs the archiving of CSVs with timestamps and logging

---

## Features
Grade Generator (__grade-generator.py__)
* Interactive input with validation (grades 0-100, categories FA/SA, positive weights).
* Weighted grades, final grade and GPA (5.0 scale) computed.
* Pass/Fail determination (requires ≥50% in BOTH categories)
* Resubmission recommendations for failing students.
* Export data to CSV.

Organizer (organizer.sh)
* Timestamps and renames CSV files (grades.csv → grades-20251112-143025.csv)
* Moves files to archive/ directory
* Logs all actions and file contents to organizer.log.

---

## __How It Works__
```
Weighted Grade = (Grade / 100) × Weight
Final Grade = Total FA + Total SA
GPA = (Final Grade / 100) × 5.0
```

Pass/Fail Logic: Student must score ≥50% in BOTH FA and SA categories.

Example:
```
FA: 17.0/20.0 (Need 10.0) 
SA: 40.0/50.0 (Need 25.0) 
Status: PASS | GPA: 2.85
```

---

## Archival Process
```
grades.csv → [timestamp] → grades-20251112-143025.csv → archive/
                         → [log] → organizer.log
```

---

## __File Structure__
```
Lab1-YOUR_USERNAME/
├── grade-generator.py    # Python calculator
├── organizer.sh          # Bash archival script
├── README.md             # Documentation
├── grades.csv            # Generated grade data
├── organizer.log         # Archival log
└── archive/              # Archived CSV files
```

---

## __Troubleshooting__
| Issue | Solution |
|-------|----------|
| Permission denied | chmod +x organizer.sh |
| Python not found | Use python3 instead of python |
| No CSV files found | Run grade-generator.py first |

---

## Author
Raphael Mumo Musau - African Leadership University

GitHub: raphaelmstudios

Course: Introduction to Python Programming and Databases

---

## Requirements
* Python 3.8+
* Bash 4.0+
* OS: Linux/macOS/WSL (Windows)
