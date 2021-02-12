from analysis import match_this_row
from tests.test_data.four_rows import test_rows


def test_regular_cyclist_found_in_row_which_has_it():
    row_filters = [
        {
            "Which of these best describes you currently?":
                [
                    "A am a regular cyclist (once a week or more)"
                ]
        }
    ]
    assert match_this_row(row=test_rows[1], filters=row_filters) is True


def test_regular_cyclist_not_found_when_row_does_not_have_it():
    row_filters = [
        {
            "Which of these best describes you currently?":
                [
                    "A am a regular cyclist (once a week or more)"
                ]
        }
    ]
    assert match_this_row(row=test_rows[0], filters=row_filters) is False


def test_multiple_filter_conditions():
    row_filters = [
        {
            "Which of these best describes you currently?":
                [
                    "A am a regular cyclist (once a week or more)"
                ],
            "Do you support proposals for the scheme on Lowden Hill in Chippenham?": ["No"],
            "How old are you?": ["35-44"]
        }
    ]
    assert match_this_row(row=test_rows[0], filters=row_filters) is False
    assert match_this_row(row=test_rows[1], filters=row_filters) is False
    assert match_this_row(row=test_rows[2], filters=row_filters) is False
    assert match_this_row(row=test_rows[3], filters=row_filters) is True
