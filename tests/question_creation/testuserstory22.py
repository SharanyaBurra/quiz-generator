# test_question_pools.py
# Simple tests for question_pools.py

import json
import os
from question_pools import generate_quiz_from_pools, save_template, question_pools, pool_settings


def test_quiz_length():
    """Test that the quiz has the correct total number of questions."""
    quiz = generate_quiz_from_pools(question_pools, pool_settings)
    expected_total = sum(pool_settings.values())
    assert len(quiz) == expected_total, f"Expected {expected_total} questions, got {len(quiz)}"
    print("✅ test_quiz_length passed.")


def test_questions_from_pools():
    """Test that every question in the quiz is actually from the defined pools."""
    quiz = generate_quiz_from_pools(question_pools, pool_settings)

    all_questions = []
    for qs in question_pools.values():
        all_questions.extend(qs)

    for q in quiz:
        assert q in all_questions, f"Question not found in pools: {q}"
    print("✅ test_questions_from_pools passed.")


def test_save_template():
    """Test that the template is saved as a valid JSON file."""
    filename = "quiz_template_test.json"
    save_template(pool_settings, filename)

    assert os.path.exists(filename), "Template file was not created."

    with open(filename, "r") as f:
        data = json.load(f)

    assert data == pool_settings, "Saved template content does not match pool_settings."
    print("✅ test_save_template passed.")

    # Clean up
    os.remove(filename)


if __name__ == "__main__":
    print("Running tests for question_pools.py...\n")
    test_quiz_length()
    test_questions_from_pools()
    test_save_template()
    print("\n All tests passed!")
