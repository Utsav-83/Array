import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    # initialize array with at least 11 elements so index 10 is valid
    score = [None] * 11
    score[10] = sys.argv[1]
else:
    score = [1, 2, 3, 9, 7, 10, 5]

sum_of_elements = sum(score)
print("Sum of elements:", sum_of_elements)
avg_of_elements = sum_of_elements / len(score)
print("Average of elements:", avg_of_elements)
