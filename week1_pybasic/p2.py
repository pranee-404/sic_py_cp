'''accept the average score from the student and give her the results as follows:
0 to 69 - fail
70 to 84 - second class
85 to 95 - first class
96 to 100 - excellent'''
avg_score = int(input('Enter the student average score:'))
if avg_score >= 0 and avg_score <= 69:
    print('Result is Fail')
elif avg_score >= 70 and avg_score <= 84:
    print('Result is Second class')
elif avg_score >= 85 and avg_score <= 95:
    print('Result is First class')
elif avg_score >= 96 and avg_score <= 100:
    print('Result is Excellent')
else:
    print('Invalid Average Score')