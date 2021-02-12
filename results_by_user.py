"""
Some filters to analyse results by user.
"""
from typing import Dict, List

from analysis import get_matching_rows, read_file

file_rows = read_file(file_path="data/202001322_input.csv")

all_filters_dict = {
    "ind_t1_r1c1": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["A am a regular cyclist (once a week or more)"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": ["Yes"]
        }
    ],
    "ind_t1_r1c2": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["A am a regular cyclist (once a week or more)"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": ["No"]
        }
    ],
    "ind_t1_r1c3": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["A am a regular cyclist (once a week or more)"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": [
                "I am not interested in this scheme"
            ]
        }
    ],
    "ind_t1_r1c4": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["I am an occasional cyclist"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": ["Yes"]
        }
    ],
    "ind_t1_r1c5": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["I am an occasional cyclist"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": ["No"]
        }
    ],
    "ind_t1_r1c6": [
        {
            "Are you responding on behalf of yourself or a group?": ["Myself"],
            "Which of these best describes you currently?": ["I am an occasional cyclist"],
            "Do you support the cycling scheme on the A420 Bristol Road in Chippenham?": [
                "I am not interested in this scheme"
            ]
        }
    ],

}

for filter_name, filter_rules in all_filters_dict.items():
    matching_rows = get_matching_rows(input_rows=file_rows, filters=filter_rules)
    print(f"Filter {filter_name}, matches={len(matching_rows)}")
