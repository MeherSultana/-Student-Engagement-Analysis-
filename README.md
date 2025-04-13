# Student-Engagement-Analysis
# 📊 Student Engagement Analysis This notebook demonstrates how to analyze student engagement using attendance, assignment, and participation data.

🔹 Load the Data:
Imported CSV files containing student attendance, assignment scores, and weekly participation logs using pandas.

🔹 Clean and Prepare the Data:
Parsed dates, handled missing values, and added useful features like week numbers extracted from attendance dates.

🔹 Analyze Weekly Attendance:
Grouped attendance records by student and ISO calendar week, then calculated each student's weekly attendance rate. Aggregated this further to find the average attendance trend across all students per week.

🔹 Analyze Assignment Scores:
Grouped assignment scores by type (e.g., Homework, Quiz, Project) to compute average performance and highlight strengths or areas needing support.

🔹 Analyze Participation Trends:
Averaged weekly posts_made and resources_viewed per student, and plotted trends over time to evaluate student engagement across weeks.

🔹 Visualize the Data:
Used matplotlib to generate insightful plots showing:

Weekly attendance rates

Average assignment scores by type

Participation trends over time

🔹 Save Plots for Documentation:
All plots were saved using plt.savefig() to the /images folder 