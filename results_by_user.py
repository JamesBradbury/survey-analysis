"""
Some filters to analyse results by user.
"""
import csv
from typing import Dict

from analysis import get_matching_rows, read_file, create_filter_combinations, remove_several_strings

file_rows = read_file(file_path="data/202001322_input.csv")


def truncate_answers(filter_dict: Dict) -> str:
    output_list = []
    for k, v in filter_dict.items():
        if len(v) > 1:
            raise ValueError("More than one answer found!", v)
        output_list.append(f"Q:{k} A:{v[0][:10]}")

    return ", ".join(output_list)


response_info = {
    "Are you responding on behalf of yourself or a group?": ["A group"],
    "Which of these best describes you currently?": [
        "I am an occasional cyclist",
        "A am a regular cyclist (once a week or more)",
        "I am not a cyclist and I do not wish to start cycling",
        "I don't currently cycle but I would like to cycle more or start cycling",
    ],
}

schemes = {
    "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support the cycling scheme on Monkton Hill in Chippenham?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support the cycling scheme on Brown Street and Exeter Street in Salisbury?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support the cycling scheme on the A361 Hilperton Road in Trowbridge?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support the cycling scheme on the B3108 between Winsley and Bradford on Avon?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support proposals to make the scheme on the A420 in Chippenham permanent and extend the scheme?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support proposals for the scheme on Lowden Hill in Chippenham?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support proposals for the scheme on Downton Road in Salisbury?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support proposals for the scheme that links Hilperton to Melksham via Semington?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
    "Do you support proposals for the Easton Lane cycle link between Chippenham and Corsham?": [
        "Yes", "No", "I am not interested in this scheme",
    ],
}

text_to_remove = [
    "Do you support proposals ",
    "Do you support the cycling scheme on ",
    "Are you responding on behalf of yourself or a "
]

questions = {}
responder_filters_dict = create_filter_combinations(questions_and_answers=response_info)

print("responder_filters_dict combinations: ", len(responder_filters_dict))

responder_rows = []

for filter_name, filter_rule in responder_filters_dict.items():
    responder_rows.extend(get_matching_rows(input_rows=file_rows, filters=filter_rule))
    print(f"matches={len(responder_rows)} / {len(file_rows)}\n")

output_rows = []

for scheme_q, scheme_a_list in schemes.items():
    questions = {scheme_q: scheme_a_list}
    scheme_filters_dict = create_filter_combinations(questions_and_answers=questions)
    output_dict = dict()
    output_dict["Schemes"] = remove_several_strings(target=scheme_q, remove_list=text_to_remove)

    for filter_name, filter_rule in scheme_filters_dict.items():
        matching_rows = get_matching_rows(input_rows=responder_rows, filters=filter_rule)
        answer_text = filter_rule[0][scheme_q][0][:10]
        output_dict[answer_text] = len(matching_rows)
    output_rows.append(output_dict)

with open("results_group_would_like_to_cycle.csv", "w") as csv_out:
    dw = csv.DictWriter(csv_out, delimiter=",", fieldnames=output_rows[0].keys())
    dw.writeheader()
    dw.writerows(output_rows)
