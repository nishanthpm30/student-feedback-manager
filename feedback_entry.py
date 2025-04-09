def collect_feedback():
  feedback = {}
  num_students = int(input("Enter the number of students providing feedback: "))

  for i in range(1, num_students + 1):
    student_name = input(f"Enter the name of student {i}: ")
    comment = input(f"Enter feedback for {student_name}: ")
    feedback[student_name] = comment

  print("\n--- Feedback Collected ---")
  for name, comment in feedback.items():
    print(f"{name}: {comment}")

if name == "main":
  collect_feedback()
