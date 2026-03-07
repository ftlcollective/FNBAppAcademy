# =============================================================
#  Week 8 – FNB App Academy · Python Data Structures 🏗️
#  Topics: Lists, Dictionaries, Tuples, Sets + Backend Project
# =============================================================

print("=" * 55)
print("  🏗️  Week 8 – Python Data Structures + Backend Project")
print("  FNB App Academy")
print("=" * 55)


# --------------------------------------------------
# 1. LISTS
# --------------------------------------------------
print("\n📦 1. Lists")

courses = ["HTML", "CSS", "JavaScript", "Python"]
print(f"  Courses      : {courses}")
print(f"  First        : {courses[0]}")
print(f"  Last         : {courses[-1]}")

courses.append("React")
print(f"  After append : {courses}")

courses.remove("CSS")
print(f"  After remove : {courses}")

print(f"  Sorted       : {sorted(courses)}")

squares = [x ** 2 for x in range(1, 6)]
print(f"  Squares 1–5  : {squares}")


# --------------------------------------------------
# 2. DICTIONARIES
# --------------------------------------------------
print("\n📕 2. Dictionaries")

student = {
    "name": "Lebo Mokoena",
    "age": 22,
    "phase": "Advanced",
    "week": 8,
    "languages": ["HTML", "CSS", "JavaScript", "Python"]
}

print(f"  Name     : {student['name']}")
print(f"  Phase    : {student['phase']}")
print(f"  Languages: {', '.join(student['languages'])}")

student["completed"] = True
print(f"  Keys     : {list(student.keys())}")

for key, val in student.items():
    print(f"    {key}: {val}")


# --------------------------------------------------
# 3. TUPLES
# --------------------------------------------------
print("\n🧱 3. Tuples")

coordinates = (26.2041, 28.0473)   # Johannesburg
rgb_red     = (255, 0, 0)
academy_info = ("FNB App Academy", 2024, "Johannesburg")

print(f"  Coordinates   : {coordinates}")
print(f"  RGB Red       : {rgb_red}")
print(f"  Academy       : {academy_info}")
print(f"  (Tuples are immutable — they cannot be changed after creation)")


# --------------------------------------------------
# 4. SETS
# --------------------------------------------------
print("\n🧮 4. Sets")

skills_a = {"HTML", "CSS", "JavaScript", "Python"}
skills_b = {"Python", "Django", "SQL", "HTML"}

print(f"  Set A         : {skills_a}")
print(f"  Set B         : {skills_b}")
print(f"  Union         : {skills_a | skills_b}")
print(f"  Intersection  : {skills_a & skills_b}")
print(f"  Difference    : {skills_a - skills_b}")


# --------------------------------------------------
# 5. BACKEND PROJECT: Student Registry
# --------------------------------------------------
print("\n" + "=" * 55)
print("  🏫 BACKEND PROJECT: Student Registry System")
print("=" * 55)

students_db = []

def add_student(name, age, course):
    student_id = len(students_db) + 1
    record = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "enrolled": True
    }
    students_db.append(record)
    return record

def get_all_students():
    return students_db

def find_student(name):
    results = [s for s in students_db if name.lower() in s["name"].lower()]
    return results

def remove_student(student_id):
    global students_db
    before = len(students_db)
    students_db = [s for s in students_db if s["id"] != student_id]
    return len(students_db) < before

def get_stats():
    if not students_db:
        return {}
    courses = [s["course"] for s in students_db]
    unique_courses = set(courses)
    return {
        "total_students": len(students_db),
        "unique_courses": len(unique_courses),
        "courses": list(unique_courses),
        "avg_age": round(sum(s["age"] for s in students_db) / len(students_db), 1)
    }

def display_students(students):
    if not students:
        print("  No students found.")
        return
    print(f"\n  {'ID':<4} {'Name':<20} {'Age':<6} {'Course':<20} {'Enrolled'}")
    print("  " + "-" * 58)
    for s in students:
        print(f"  {s['id']:<4} {s['name']:<20} {s['age']:<6} {s['course']:<20} {'✅' if s['enrolled'] else '❌'}")


# Seed data
print("\n  📥 Adding students...")
add_student("Lebo Mokoena",   22, "Full Stack Web Development")
add_student("Thabo Dlamini",  24, "Python Backend Development")
add_student("Nomsa Khumalo",  20, "Full Stack Web Development")
add_student("Sipho Ndlovu",   26, "Data Science with Python")
add_student("Ayanda Zulu",    21, "Python Backend Development")

# Display all
print("\n  📋 All Students:")
display_students(get_all_students())

# Search
print("\n  🔎 Search for 'Lebo':")
display_students(find_student("Lebo"))

# Stats
print("\n  📊 Registry Statistics:")
stats = get_stats()
for k, v in stats.items():
    print(f"    {k}: {v}")

# Remove
print("\n  🗑️  Removing student with ID 3...")
removed = remove_student(3)
print(f"  Removed: {removed}")
display_students(get_all_students())

print("\n" + "=" * 55)
print("  ✅ Week 8 complete! Data structures + backend project done.")
print("=" * 55)
