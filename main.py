from analysis import get_matching_rows, read_file

file_rows = read_file(file_path="data/202001322_input.csv")

print("### file_rows:")
for r in file_rows[:4]:
    print(r)

t1q1_filter = [
    {"Which of these best describes you currently?":
         ["A am a regular cyclist (once a week or more)"]}
]

t1q1_rows = get_matching_rows(input_rows=file_rows, filters=t1q1_filter)
print("t1q1 count:", len(t1q1_rows))
