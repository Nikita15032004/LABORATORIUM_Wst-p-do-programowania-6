#zad 7
#----------------------------------------------------------------
from datetime import datetime

last_lab_date = datetime(2024, 11, 19)
exam_date = datetime(2024, 12, 17)

current_date = datetime.now()
days_since_last_lab = (current_date - last_lab_date).days
days_until_exam = (exam_date - current_date).days

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

print(f"Days since the last laboratory: {days_since_last_lab} days")
print(f"Days until the exam: {days_until_exam} days ({month_names[exam_date.month]})")

