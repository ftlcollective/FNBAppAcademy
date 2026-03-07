# =============================================================
#  Week 7 – FNB App Academy · Introduction to Python 🐍
#  Topics: Variables, Data Types, Conditionals, Loops, Functions
# =============================================================

print("=" * 50)
print("  🐍 Week 7 – Introduction to Python")
print("  FNB App Academy")
print("=" * 50)


# --------------------------------------------------
# 1. VARIABLES & DATA TYPES
# --------------------------------------------------
print("\n📦 1. Variables & Data Types")

name = "FNB App Academy"       # str
year = 2024                    # int
price = 99.99                  # float
is_enrolled = True             # bool

print(f"  Name     : {name}")
print(f"  Year     : {year}")
print(f"  Price    : R{price}")
print(f"  Enrolled : {is_enrolled}")
print(f"  Types    : {type(name).__name__}, {type(year).__name__}, {type(price).__name__}, {type(is_enrolled).__name__}")


# --------------------------------------------------
# 2. STRING OPERATIONS
# --------------------------------------------------
print("\n🔤 2. String Operations")

greeting = "hello, world"
print(f"  Original  : {greeting}")
print(f"  Upper     : {greeting.upper()}")
print(f"  Title     : {greeting.title()}")
print(f"  Length    : {len(greeting)}")
print(f"  Replace   : {greeting.replace('world', 'Python')}")


# --------------------------------------------------
# 3. CONDITIONALS
# --------------------------------------------------
print("\n🔀 3. Conditionals")

def check_grade(score):
    if score >= 80:
        return "🏆 Distinction"
    elif score >= 70:
        return "✅ Merit"
    elif score >= 50:
        return "📘 Pass"
    else:
        return "❌ Fail"

scores = [92, 75, 55, 30]
for s in scores:
    print(f"  Score {s}: {check_grade(s)}")


# --------------------------------------------------
# 4. LOOPS
# --------------------------------------------------
print("\n🔁 4. Loops")

print("  For loop – counting 1 to 5:")
for i in range(1, 6):
    print(f"    {i}", end=" ")
print()

print("  While loop – countdown:")
n = 5
while n > 0:
    print(f"    {n}...", end=" ")
    n -= 1
print("🚀 Liftoff!")


# --------------------------------------------------
# 5. FUNCTIONS
# --------------------------------------------------
print("\n⚙️  5. Functions")

def greet_student(student_name, week=7):
    """Greet a student and tell them which week they're on."""
    return f"Welcome, {student_name}! You're on Week {week} of the FNB App Academy."

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def is_even(num):
    """Return True if a number is even."""
    return num % 2 == 0

print(f"  {greet_student('Lebo')}")
print(f"  {greet_student('Thabo', week=9)}")
print(f"  25°C = {celsius_to_fahrenheit(25)}°F")
print(f"  Is 8 even? {is_even(8)}")
print(f"  Is 7 even? {is_even(7)}")


# --------------------------------------------------
# 6. BUILDING A SIMPLE CLI INTERACTION
# --------------------------------------------------
print("\n💬 6. Simple CLI App – Name Greeter")

def run_greeter():
    user = input("  Enter your name: ").strip()
    if not user:
        print("  No name entered. Hello, Stranger!")
    else:
        print(f"  Hello, {user.title()}! Welcome to Python 🐍")
        print(f"  Your name has {len(user)} characters.")

run_greeter()

print("\n" + "=" * 50)
print("  ✅ Week 7 complete! Python basics covered.")
print("=" * 50)
