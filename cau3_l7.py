students = [
    {"sbd": "A1", "diem": 8.5},
    {"sbd": "B2", "diem": 6.0},
    {"sbd": "E3", "diem": 9.2},
    {"sbd": "D4", "diem": 5.5},
    {"sbd": "G5", "diem": 7.0},
    {"sbd": "F6", "diem": 4.8},
]

students_sorted = sorted(students, key=lambda x: x["diem"], reverse=True)

print("Danh sách sau khi sắp xếp:")
for s in students_sorted:
    print(f"SBD: {s['sbd']}, Điểm: {s['diem']}")

last_three = students_sorted[3:]

print("\n3 học sinh điểm cao nhất:")
for s in last_three:
    print(f"SBD: {s['sbd']}, Điểm: {s['diem']}")
