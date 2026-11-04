college_attendance = {
    "Mathematics": 82,
    "Physics": 68,
    "Basic Electrical Engineering": 78,
    "Programming in Python": 90,
    "Engineering Graphics": 72
}
print("🎒 --- B.Tech Attendance & Bunk Planner --- \n")
required_percentage = 75

for subject , percentage in college_attendance.items():
    print(f"📚 Subject: {subject}")
    print(f"📊 Current Attendance: {percentage}%")

    if percentage >= required_percentage:
         print("✅ Status: Safe! You meet the 75% criteria.")
         print("💡 Advice: You can safely afford to miss the next lecture if needed.\n")
    else:
        print("🚨 Status: Low Attendance Alert!")
        classes_needed = required_percentage - percentage
        print(f"⚠️ Advice: DO NOT BUNK! You need to attend upcoming classes to bridge the {classes_needed}% gap.\n")

print("------------------------------------------")
print("🎯 Pro-Tip: Keep your streak high in both coding and college attendance!")