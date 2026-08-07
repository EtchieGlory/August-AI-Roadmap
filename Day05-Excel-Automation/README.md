# Day 5 - Excel Grade Automation

A Python automation tool that reads student scores from an Excel
spreadsheet, automatically assigns grades, handles invalid or missing
scores, formats the workbook, and creates a grade summary.

## Features

-   Read existing `.xlsx` files
-   Process student scores automatically
-   Assign grades:
    -   `A` --- 70 and above
    -   `B` --- 50--69
    -   `F` --- below 50
-   Handle missing or non-numeric scores as `N/A`
-   Add a Grade column automatically
-   Create a Summary worksheet
-   Count the number of A, B, and F grades
-   Bold worksheet headers
-   Adjust column widths
-   Save the processed workbook to an output folder

## Project Structure

``` text
Day05-Excel-Automation/
├── main.py
├── README.md
├── requirements.txt
├── files/
│   └── students.xlsx
└── output/
    └── graded_students.xlsx
```

## Requirements

-   Python 3
-   openpyxl

Install the dependency with:

``` bash
pip install openpyxl
```

Or install from `requirements.txt`:

``` bash
pip install -r requirements.txt
```

## Input Format

The input Excel file should contain student names in column A and scores
in column B.

Example:

  Name      Score
  ------- -------
  John         85
  Mary         42
  Peter        73
  David        61

The program starts processing from row 2 because row 1 is treated as the
header.

## How It Works

1.  Loads `files/students.xlsx`.
2.  Accesses the active worksheet.
3.  Creates a `Grade` column.
4.  Checks each student's score.
5.  Assigns the appropriate grade.
6.  Marks missing or invalid scores as `N/A`.
7.  Creates a `Summary` worksheet.
8.  Counts A, B, and F grades.
9.  Formats the headers and adjusts column widths.
10. Saves the result as `output/graded_students.xlsx`.

## Example Output

The Students sheet will contain:

  Name      Score Grade
  ------- ------- -------
  John         85 A
  Mary         42 F
  Peter        73 A
  David        61 B

The Summary sheet will contain:

  Grade     Number of Students
  ------- --------------------
  A                          2
  B                          1
  F                          1

## What I Learned

This project helped me practice:

-   Python file paths
-   Importing third-party libraries
-   `openpyxl`
-   `Workbook`
-   `load_workbook`
-   Worksheets and cells
-   `.value`
-   `iter_rows()`
-   `max_row`
-   Dynamic Excel cell references
-   `isinstance()`
-   Loops and conditional statements
-   Creating worksheets
-   Basic Excel formatting
-   Automating repetitive data-processing tasks

## Future Improvements

Possible features for a future version:

-   Support multiple input files
-   Add more grading systems
-   Calculate class averages
-   Find the highest and lowest scores
-   Add Excel formulas
-   Add charts
-   Apply more advanced formatting
-   Generate PDF reports
-   Add a command-line menu
-   Validate score ranges such as 0--100

## Project Status

**Day 5 of 30-Day AI Automation Roadmap --- Complete ✅**

This project is part of a progressive roadmap focused on building
practical Python automation skills before moving into AI-powered
applications.


## 👨‍💻 Author

**Etchie Glory Edonyabo**

Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.

Building one practical Python project every day throughout the **August AI Automation Roadmap**.