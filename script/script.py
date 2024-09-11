import json

JSON_DATA_FILE_PATH = "../data/student_audit_data_with_fake_names.json"
RESULTS_FILE_PATH = "../results/results.txt"

with open(JSON_DATA_FILE_PATH, "r") as json_file:
    student_data = json.load(json_file)

# Print the total number of students
print(f"Total number of students: {len(student_data)}")

# Initialize dictionaries to count the occurrences of "N" for each course and track student names
course_counts = {}
students_needing_courses = {}

# Iterate through each student's data
for student in student_data:
    # Debug statement to print the student_active status
    print(f"Student: {student.get('student_name', 'Unknown')}, Active: {student.get('student_active')}")

    # Check if the student is active
    if student.get("student_active") != "Y":
        continue
    
    student_name = student.get("student_name", "Unknown")
    print(f"Processing student: {student_name}")  # Debug statement
    
    # Find the key that starts with "concentration_in"
    concentration_key = next((key for key in student if key.startswith("concentration_in")), None)
    if concentration_key:
        concentration = student[concentration_key]
        for course, status in concentration.items():
            if status == "N":
                if course not in course_counts:
                    course_counts[course] = 0
                    students_needing_courses[course] = []
                course_counts[course] += 1
                students_needing_courses[course].append(student_name)
                print(f"Student {student_name} needs to take {course}")  # Debug statement

# Write the results to a text file
with open(RESULTS_FILE_PATH, "w") as results_file:
    # Write individual student needs
    for course, count in course_counts.items():
        if count == 1:
            results_file.write(f"1 student needs to take {course}: {students_needing_courses[course][0]}\n")
        else:
            results_file.write(f"{count} students need to take {course}: {', '.join(students_needing_courses[course])}\n")
    
    # Write the summary of courses needed by the most students
    results_file.write("\nCourses needed by the most students:\n")
    sorted_courses = sorted(course_counts.items(), key=lambda item: item[1], reverse=True)
    for course, count in sorted_courses:
        if count == 1:
            results_file.write(f"1 student needs to take {course}\n")
        else:
            results_file.write(f"{count} students need to take {course}\n")

print(f"Results have been written to {RESULTS_FILE_PATH}")