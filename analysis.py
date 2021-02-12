import csv
from typing import Dict, List, Any


def display_possible_answers(all_answers: Dict) -> None:
    # Display the all the questions, with all the possible answers.
    for question, set_of_answers in all_answers.items():
        print(f'"{question}"')
        for answer in set_of_answers:
            print(f' - "{answer}"')


def collate_totals(totals: Dict[str, Dict[str, int]], question: str, answer: str) -> Dict:
    # If we haven't seen this question yet, add it.
    if question not in totals:
        totals[question] = dict()
    # If we haven't seen this answer for this question yet, add it.
    elif answer not in totals[question]:
        totals[question][answer] = 1
    else:
        # If we have seen this answer for this question, count another one.
        totals[question][answer] += 1

    return totals


def match_this_row(row: Dict[str, Any], filters: List) -> bool:
    """
    Go through all filters checking that the question is there and the answer matches
    what we're looking for. If not, return False.
    """
    for filter_dict in filters:
        for question, answers_set in filter_dict.items():
            if question not in row or row[question] not in answers_set:
                return False

    return True


def get_matching_rows(input_rows: List, filters: List) -> List:
    """
    Gets the rows which match all the filters. If a question is not listed in filters, any answer can match.
    :param input_rows: Rows to search for matches
    :param filters: Conditions (questions and answers)
    :return: matching_rows
    """
    matching_rows = []
    for row in input_rows:
        if not match_this_row(row, filters):
            continue
        matching_rows.append(row)

    return matching_rows


def read_file(file_path: str):
    all_raw_rows = []
    all_question_totals = dict()
    possible_responses_per_field = dict()
    with open(file_path) as input_csv:
        csv_reader = csv.DictReader(input_csv, delimiter=",")

        for row_dict in csv_reader:
            all_raw_rows.append(row_dict)
            for question, answer in row_dict.items():
                # First, get all the possible responses for all the questions,
                # so we have something to refer to.
                if question not in possible_responses_per_field:
                    possible_responses_per_field[question] = set()
                else:
                    possible_responses_per_field[question].add(answer)
                collate_totals(
                    totals=all_question_totals,
                    question=question,
                    answer=answer
                )

    print(all_question_totals)
    display_possible_answers(all_answers=possible_responses_per_field)

    return all_raw_rows
