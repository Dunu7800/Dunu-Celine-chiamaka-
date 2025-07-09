# NAME: DUNU CELINE CHIAMAKA
# REG NO: 2024934009
# DEPT: SOFTWARE ENGINEERING
# COURSE CODE: COS102

# Pseudocode:
# START
# FUNCTION get_grade(score)
#     IF score >= 70 AND score <= 100 THEN
#         RETURN "A"
#     ELSE IF score >= 60 AND score < 70 THEN
#         RETURN "B"
#     ...
# END FUNCTION
# GET score from user
# CALL get_grade(score)
# PRINT grade



def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score <= 39:
        return "F"
    else:
        return "Invalid score"

#  I used try statement so that the code won't crash
try:
    score_input = float(input("Enter your assignment score (0 - 100): "))
    grade = get_grade(score_input)
    print(f"Your grade is: {grade}")
except ValueError:
    print("Please enter a valid integer score.")
