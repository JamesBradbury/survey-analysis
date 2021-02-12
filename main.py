import csv

# First, get all the possible responses for all the questions,
# so we have something to refer to.
possible_responses_per_field = dict()
all_question_totals = dict()


def display_possible_answers():
    # Display the all the questions, with all the possible answers.
    for question, set_of_answers in possible_responses_per_field.items():
        print(f"Question: {question}")
        for answer in set_of_answers:
            print(f" - {answer}")


def collate_totals(question: str, answer: str):
    # If we haven't seen this question yet, add it.
    if question not in all_question_totals:
        all_question_totals[question] = {}
    # If we haven't seen this answer for this question yet, add it.
    elif answer not in all_question_totals[question]:
        all_question_totals[question][answer] = 1
    else:
        # If we have seen this answer for this question, count another one.
        all_question_totals[question][answer] += 1


def read_file():
    with open("data/202001322_input.csv") as input_csv:
        csv_reader = csv.DictReader(input_csv, delimiter=",")

        for row_dict in csv_reader:
            for question, answer in row_dict.items():
                if question not in possible_responses_per_field:
                    possible_responses_per_field[question] = set()
                else:
                    possible_responses_per_field[question].add(answer)
                collate_totals(question=question, answer=answer)


read_file()

display_possible_answers()

print(all_question_totals)
