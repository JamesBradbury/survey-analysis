import csv

# First, get all the possible responses for all the questions,
# so we have something to refer to.
possible_responses_per_field = dict()

with open("data/202001322_input.csv") as input_csv:
    csv_reader = csv.DictReader(input_csv, delimiter=",")

    for row_dict in csv_reader:
        for key, value in row_dict.items():
            if key not in possible_responses_per_field:
                possible_responses_per_field[key] = set()
            else:
                possible_responses_per_field[key].add(value)

# Display the all the questions, with all the possible answers.
for question, set_of_answers in possible_responses_per_field.items():
    print(f"Question: {question}")
    for answer in set_of_answers:
        print(f" - {answer}")
