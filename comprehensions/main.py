
## Group Members
# Brian Oyollo
# Fred Monjugu
# Elvis Njoroge
# Caesar Augustine


# task 1: List Comprehension – Student Grades
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]

# Use a list comprehension to filter all the scores above 60 and store them in a new list called passed
passed  = [score for score in scores if score > 60]
# print(passed)

# Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.
pass_fail_list = ["Fail" if score < 50 else "Pass" for score in scores]
# print(pass_fail_list)

# task 2: Dictionary Comprehension – Student Report
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]

# Create a dictionary using comprehension that pairs each student with their mark.
students_score = {name:score for name,score in zip(students, marks)}
# print(students_score)

# Create a second dictionary that stores only students who scored more than 70
students_passed = {name:score for name,score in zip(students, marks) if score > 70}
# print(students_passed)

# Create a third dictionary that maps each student to "Pass" or "Fail" (threshold: 50).
pass_fail_dict = {name:"Fail" if score < 50 else "Pass" for name,score in zip(students, marks)} 
# print(pass_fail_dict)


# Bonus Challenge (for advanced learners)
# Given a sentence:
# sentence = "Data science is fun and insightful"
# Write a dictionary comprehension that maps each word to its length.

sentence = "Data science is fun and insightful"
word_len = {word:len(word) for word in sentence.split(" ")}
# print(word_len)