# BHU/23/04/09/0058

import tkinter as tk
from tkinter import Entry, Button, Label, StringVar

def calculate_cgpa():
    total_credit_units = sum(course_data.values())
    total_grade_points = 0

    for course, (credit_units) in course_data.items():
        grade = grade_vars[course].get()
        grade_point = calculate_grade_point(grade)
        total_grade_points += grade_point * credit_units

    if total_credit_units == 0:
        cgpa_var.set("N/A")
        class_var.set("N/A")
    else:
        cgpa = total_grade_points / total_credit_units
        cgpa_var.set(f"Your CGPA is: {cgpa:.2f}!")
        class_var.set(f"Your CGPA Class is: {classify_cgpa(cgpa)}!")

def calculate_grade_point(grade):
    grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'E': 1.0, 'F': 0.0}
    return grade_points.get(grade.upper(), 0.0)

def classify_cgpa(cgpa):
    cgpa_class = cgpa

    if cgpa_class >= 4.5:
        return "First Class"
    elif cgpa_class >= 3.5:
        return "Second Class Upper"
    elif cgpa_class >= 2.5:
        return "Second Class Lower"
    elif cgpa_class >= 1.5:
        return "Third Class"
    else:
        return "Fail"
