Q.1 A school maintains a record of students' exam scores for 5 subjects in a 2D NumPy array.
    Each row represents a student, and each column represents a subject:    
    import numpy as np  # Student scores: rows = students, columns = subjects     
    scores = np.array([[85, 90, 78, 92, 88],   # Student 1   
                       [72, 75, 80, 68, 74],   # Student 2    
                       [95, 88, 92, 96, 90],   # Student 3    
                       [60, 65, 70, 58, 62],   # Student 4    
                       [88, 84, 86, 89, 87]    # Student 5 ]) 
Answer:
Code:
1.Retrieve the scores of Student 3 for all subjects:
import numpy as np
scores = np.array([
    [85, 90, 78, 92, 88],   
    [72, 75, 80, 68, 74],   
    [95, 88, 92, 96, 90],   
    [60, 65, 70, 58, 62],   
    [88, 84, 86, 89, 87]    
])
student_3_scores = scores[2, :]
print("Student 3 scores:", student_3_scores)

2.Retrieve the scores for Subject 2 (column 2) across all students:
subject_2_scores = scores[:, 1]
print("Subject 2 scores:", subject_2_scores)

3.a. Extract the scores of the first 3 students for the first 2 subjects:
first_3_students_first_2_subjects = scores[:3, :2]
print("First 3 students' first 2 subjects:", first_3_students_first_2_subjects)

b. Extract the scores of the last 2 students for the last 3 subjects:
last_2_students_last_3_subjects = scores[3:, 2:]
print("Last 2 students' last 3 subjects:", last_2_students_last_3_subjects)


4.Add 5 bonus marks to all scores:
scores_with_bonus = scores + 5
print("Scores with bonus:", scores_with_bonus)

5.Subtract 10 marks from scores of Subject 4 for all students:
scores[:, 3] -= 10
print("Scores after subtracting 10 marks from Subject 4:", scores)

6.Calculate the percentage scores of each student assuming each subject is out of 100:
percentages = (scores.sum(axis=1) / 500) * 100
print("Percentage scores of each student:", percentages)

7.Calculate the average score for each student across all subjects:
average_scores = scores.mean(axis=1)
print("Average score of each student:", average_scores)

8.Find the total marks scored by each student:
total_marks = scores.sum(axis=1)
print("Total marks scored by each student:", total_marks)

9.Identify the highest score in the entire array:
highest_score = scores.max()
print("Highest score in the entire array:", highest_score)

10.Determine the average score for each subject:
average_subject_scores = scores.mean(axis=0)
print("Average score for each subject:", average_subject_scores)

11.Find the student with the lowest average score:
lowest_avg_student = np.argmin(average_scores)
print("Student with the lowest average score:", lowest_avg_student + 1)  


Output:
Scores after subtracting 10 marks from Subject 4: [[85 90 78 82 88]
 [72 75 80 58 74]
 [95 88 92 86 90]
 [60 65 70 48 62]
 [88 84 86 79 87]].
Percentage scores of each student: [84.6 71.8 90.2 61.  84.8].
Average score of each student: [84.6 71.8 90.2 61.  84.8].
Total marks scored by each student: [423 359 451 305 424].
Highest score in the entire array: 95.
Average score for each subject: [80.  80.4 81.2 70.6 80.2].
Student with the lowest average score: 4.