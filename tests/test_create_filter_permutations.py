from analysis import create_filter_combinations

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

test_data = {
    "cheese": ["Yes", "No", "Unknown"],
    "ham": ["Yes", "No"],
    "eggs": ["Yes", "No"],
    "spam": ["Yes", "No", "Unknown"],
}


def test_create_filter_combinations():
    result = create_filter_combinations(questions_and_answers=test_data)
    print(result)
