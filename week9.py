# =============================================================
#  Week 9 – FNB App Academy · Final Project 🎓
#  A full CLI Task Manager combining everything learned
#  across all 9 weeks: structure, logic, data, functions, UX
# =============================================================

from datetime import datetime

print("=" * 60)
print("  🎓 Week 9 – FNB App Academy · FINAL PROJECT")
print("  📝 Task Manager — Full Python Backend CLI App")
print("=" * 60)


# --------------------------------------------------
# DATA STORE
# --------------------------------------------------
tasks = []
task_counter = 0

PRIORITIES = {"1": "🔴 High", "2": "🟡 Medium", "3": "🟢 Low"}
STATUSES   = ["Pending", "In Progress", "Completed"]


# --------------------------------------------------
# CORE FUNCTIONS
# --------------------------------------------------

def add_task(title, description="", priority="2", due_date=""):
    global task_counter
    task_counter += 1
    task = {
        "id":          task_counter,
        "title":       title,
        "description": description,
        "priority":    PRIORITIES.get(priority, "🟡 Medium"),
        "status":      "Pending",
        "due_date":    due_date,
        "created_at":  datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tags":        []
    }
    tasks.append(task)
    return task

def get_task_by_id(tid):
    return next((t for t in tasks if t["id"] == tid), None)

def update_status(tid, status):
    task = get_task_by_id(tid)
    if task and status in STATUSES:
        task["status"] = status
        return True
    return False

def delete_task(tid):
    global tasks
    before = len(tasks)
    tasks = [t for t in tasks if t["id"] != tid]
    return len(tasks) < before

def add_tag(tid, tag):
    task = get_task_by_id(tid)
    if task and tag not in task["tags"]:
        task["tags"].append(tag)
        return True
    return False

def filter_by_status(status):
    return [t for t in tasks if t["status"] == status]

def filter_by_priority(priority_label):
    return [t for t in tasks if priority_label in t["priority"]]

def search_tasks(keyword):
    kw = keyword.lower()
    return [t for t in tasks if kw in t["title"].lower() or kw in t["description"].lower()]

def get_stats():
    total = len(tasks)
    if total == 0:
        return {"total": 0}
    by_status   = {s: len([t for t in tasks if t["status"] == s]) for s in STATUSES}
    by_priority = {p: len([t for t in tasks if p in t["priority"]]) for p in ["High", "Medium", "Low"]}
    completion  = round((by_status["Completed"] / total) * 100, 1) if total else 0
    return {
        "total":       total,
        "by_status":   by_status,
        "by_priority": by_priority,
        "completion":  f"{completion}%"
    }


# --------------------------------------------------
# DISPLAY HELPERS
# --------------------------------------------------

def display_tasks(task_list, heading="Tasks"):
    print(f"\n  📋 {heading} ({len(task_list)} found)")
    if not task_list:
        print("    No tasks to display.")
        return
    print("  " + "-" * 68)
    print(f"  {'ID':<4} {'Title':<22} {'Priority':<14} {'Status':<14} {'Due'}")
    print("  " + "-" * 68)
    for t in task_list:
        due = t["due_date"] if t["due_date"] else "—"
        print(f"  {t['id']:<4} {t['title'][:21]:<22} {t['priority']:<14} {t['status']:<14} {due}")

def display_task_detail(tid):
    task = get_task_by_id(tid)
    if not task:
        print(f"  ❌ Task #{tid} not found.")
        return
    print(f"\n  🗂️  Task Detail – #{task['id']}")
    print("  " + "-" * 40)
    for k, v in task.items():
        print(f"    {k:<12}: {v}")


# --------------------------------------------------
# CLI MENU
# --------------------------------------------------

def show_menu():
    print("""
  ┌─────────────────────────────────┐
  │       📝 TASK MANAGER MENU      │
  ├─────────────────────────────────┤
  │  1. View all tasks              │
  │  2. Add a new task              │
  │  3. Update task status          │
  │  4. Add tag to task             │
  │  5. Delete a task               │
  │  6. Search tasks                │
  │  7. Filter by status            │
  │  8. Filter by priority          │
  │  9. View task detail            │
  │  10. View statistics            │
  │  0. Exit                        │
  └─────────────────────────────────┘""")

def run_app():
    # Pre-load demo tasks
    add_task("Build HTML Page",       "Create basic page structure",  "3", "2024-01-10")
    add_task("Style with CSS",        "Apply fonts, colors, layout",  "2", "2024-01-17")
    add_task("Pine City Zoo App",     "SDLC project – zoo website",   "2", "2024-01-24")
    add_task("JavaScript Intro",      "Learn DOM and events",         "2", "2024-01-31")
    add_task("Build Calculator",      "JS calculator – all ops",      "1", "2024-02-07")
    add_task("Contact Book + API",    "Fetch from JSONPlaceholder",   "1", "2024-02-14")
    add_task("Python Intro",          "Variables, loops, functions",  "2", "2024-02-21")
    add_task("Python Data Structures","Lists, dicts, tuples, sets",   "2", "2024-02-28")
    add_task("Final Project",         "Tie everything together 🎓",   "1", "2024-03-07")

    # Auto-update some statuses for demo
    for i in range(1, 9):
        update_status(i, "Completed")
    update_status(9, "In Progress")
    add_tag(9, "Python")
    add_tag(9, "FinalProject")

    while True:
        show_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            display_tasks(tasks, "All Tasks")

        elif choice == "2":
            print("\n  ➕ Add New Task")
            title = input("    Title       : ").strip()
            if not title:
                print("    Title cannot be empty.")
                continue
            desc  = input("    Description : ").strip()
            print("    Priority: 1=High, 2=Medium, 3=Low")
            pri   = input("    Priority    : ").strip() or "2"
            due   = input("    Due Date (YYYY-MM-DD or blank): ").strip()
            t = add_task(title, desc, pri, due)
            print(f"    ✅ Task #{t['id']} '{t['title']}' added.")

        elif choice == "3":
            display_tasks(tasks)
            try:
                tid = int(input("\n    Task ID to update: ").strip())
                print(f"    Statuses: {', '.join(STATUSES)}")
                new_status = input("    New status: ").strip()
                if update_status(tid, new_status):
                    print(f"    ✅ Task #{tid} updated to '{new_status}'.")
                else:
                    print("    ❌ Invalid ID or status.")
            except ValueError:
                print("    ❌ Please enter a valid number.")

        elif choice == "4":
            try:
                tid = int(input("    Task ID to tag: ").strip())
                tag = input("    Tag name: ").strip()
                if add_tag(tid, tag):
                    print(f"    ✅ Tag '{tag}' added to task #{tid}.")
                else:
                    print("    ❌ Could not add tag.")
            except ValueError:
                print("    ❌ Please enter a valid number.")

        elif choice == "5":
            try:
                tid = int(input("    Task ID to delete: ").strip())
                if delete_task(tid):
                    print(f"    ✅ Task #{tid} deleted.")
                else:
                    print("    ❌ Task not found.")
            except ValueError:
                print("    ❌ Please enter a valid number.")

        elif choice == "6":
            kw = input("    Search keyword: ").strip()
            display_tasks(search_tasks(kw), f"Results for '{kw}'")

        elif choice == "7":
            print(f"    Statuses: {', '.join(STATUSES)}")
            s = input("    Filter by status: ").strip()
            display_tasks(filter_by_status(s), f"Status: {s}")

        elif choice == "8":
            print("    Priorities: High, Medium, Low")
            p = input("    Filter by priority: ").strip().title()
            display_tasks(filter_by_priority(p), f"Priority: {p}")

        elif choice == "9":
            try:
                tid = int(input("    Task ID: ").strip())
                display_task_detail(tid)
            except ValueError:
                print("    ❌ Please enter a valid number.")

        elif choice == "10":
            stats = get_stats()
            print("\n  📊 Statistics")
            print("  " + "-" * 30)
            print(f"    Total tasks    : {stats['total']}")
            print(f"    Completion rate: {stats.get('completion', '—')}")
            print("    By Status:")
            for s, c in stats.get("by_status", {}).items():
                print(f"      {s:<14}: {c}")
            print("    By Priority:")
            for p, c in stats.get("by_priority", {}).items():
                print(f"      {p:<14}: {c}")

        elif choice == "0":
            print("\n  🎓 Thanks for using Task Manager!")
            print("  FNB App Academy – Week 9 Complete. You made it! 🚀")
            print("=" * 60)
            break

        else:
            print("    ⚠️  Invalid choice. Please try again.")


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    run_app()
