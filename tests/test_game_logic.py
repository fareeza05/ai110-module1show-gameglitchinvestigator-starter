import sys
import os
import pytest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

# Test cases for get_range_for_difficulty
def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)  # Default case

# Test cases for parse_guess
@pytest.mark.parametrize(
    "raw_input, expected_result",
    [
        ("10", (True, 10, None)),  # Valid integer input
        ("10.5", (True, 10, None)),  # Valid float input, converted to int
        ("", (False, None, "Enter a guess.")),  # Empty input
        (None, (False, None, "Enter a guess.")),  # None input
        ("abc", (False, None, "That is not a number.")),  # Invalid input
    ],
)
def test_parse_guess(raw_input, expected_result):
    assert parse_guess(raw_input) == expected_result

# Test cases for check_guess
@pytest.mark.parametrize(
    "guess, secret, expected_outcome",
    [
        (10, 10, ("Win", "🎉 Correct!")),  # Correct guess
        (15, 10, ("Too High", "📉 Go LOWER!")),  # Guess too high
        (5, 10, ("Too Low", "📈 Go HIGHER!")),  # Guess too low
    ],
)
def test_check_guess(guess, secret, expected_outcome):
    assert check_guess(guess, secret) == expected_outcome

# Test cases for update_score
@pytest.mark.parametrize(
    "current_score, outcome, attempt_number, expected_score",
    [
        (0, "Win", 0, 100),  # Win on first attempt
        (0, "Win", 9, 10),  # Minimum score for a win
        (50, "Too High", 2, 55),  # Too High on even attempt (+5 points)
        (50, "Too High", 3, 45),  # Too High on odd attempt (-5 points)
        (50, "Too Low", 3, 45),  # Too Low (-5 points)
    ],
)
def test_update_score(current_score, outcome, attempt_number, expected_score):
    assert update_score(current_score, outcome, attempt_number) == expected_score

def test_winning_guess():
    result, _ = check_guess(50, 50)  # Unpack the tuple
    assert result == "Win"

def test_guess_too_high():
    result, _ = check_guess(60, 50)  # Unpack the tuple
    assert result == "Too High"

def test_guess_too_low():
    result, _ = check_guess(40, 50)  # Unpack the tuple
    assert result == "Too Low"
