
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


@pytest.mark.parametrize("score, expected", [
    (800, "excellent"),
    (700, "good"),
    (600, "fair"),
    (400, "poor"),
])
def test_credit_band_all_categories(score, expected):
    assert credit_band(score) == expected


@pytest.mark.parametrize("score", [200, 950])
def test_invalid_credit_scores(score):
    with pytest.raises(ValueError):
        credit_band(score)


def test_eligible_customer():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_ineligible_age():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_ineligible_income():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_poor_credit_customer():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_unknown_employment():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_interest_rate_excellent():
    assert interest_rate(800, "salaried", False) == 8


def test_interest_rate_good():
    assert interest_rate(700, "salaried", False) == 10


def test_interest_rate_fair():
    assert interest_rate(600, "salaried", False) == 13


def test_interest_rate_self_employed():
    assert interest_rate(600, "self_employed", False) == 14


def test_interest_rate_with_collateral():
    assert interest_rate(600, "salaried", True) == 11


def test_interest_rate_both_conditions():
    assert interest_rate(800, "self_employed", True) == 7
