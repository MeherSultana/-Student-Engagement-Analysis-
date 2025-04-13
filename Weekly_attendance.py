import pandas as pd
import matplotlib.pyplot as plt
import os 

# Load the datasets
students = pd.read_csv("Data /students.csv")
attendance = pd.read_csv("Data /attendance.csv", parse_dates=['date'])
assignments = pd.read_csv("Data /assignments.csv", parse_dates=['due_date'])
participation = pd.read_csv("Data /participation.csv")

# Display head of each dataset
students.head(), attendance.head(), assignments.head(), participation.head()

# Calculate weekly attendance rate
attendance['week'] = attendance['date'].dt.isocalendar().week
weekly_attendance = attendance.groupby(['student_id', 'week'])['present'].mean().reset_index()

# Plot average weekly attendance rate across all students
avg_weekly_attendance = weekly_attendance.groupby('week')['present'].mean()

os.makedirs("images", exist_ok=True)

plt.figure(figsize=(8, 5))
avg_weekly_attendance.plot(marker='o')
plt.title("Average Weekly Attendance Rate")
plt.xlabel("Week Number")
plt.ylabel("Attendance Rate")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/avg_weekly_attendance_plot.png", bbox_inches='tight')
plt.show()

# Plot average score by assignment type
avg_scores = assignments.groupby('assignment_type')['score'].mean().sort_values()

avg_scores.plot(kind='barh', color='skyblue')
plt.title("Average Score by Assignment Type")
plt.xlabel("Score")
plt.tight_layout()
plt.savefig("images/avg_scores_plot.png", bbox_inches='tight')
plt.show()

# Plot participation trends
weekly_participation = participation.groupby('week')[['posts_made', 'resources_viewed']].mean()

weekly_participation.plot(marker='o')
plt.title("Average Weekly Participation")
plt.xlabel("Week")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/attendance_plot.png", bbox_inches='tight')
plt.show()



