from analysis import create_filter_combinations


test_data = {
    "cheese": ["Yes", "No", "Unknown"],
    "ham": ["Yes", "No"],
    "eggs": ["Yes", "No"],
    "spam": ["Yes", "No", "Unknown"],
}


def test_create_filter_combinations():
    # Exploratory test, no assertions yet.
    result = create_filter_combinations(questions_and_answers=test_data)
    for k, v in result.items():
        print(k, v)
