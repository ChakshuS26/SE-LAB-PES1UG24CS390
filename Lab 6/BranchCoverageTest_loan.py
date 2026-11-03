
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


def test_score_below_minimum():
    with pytest.raises(ValueError):
        credit_band(200)


def test_score_above_maximum():
    with pytest.raises(ValueError):
        credit_band(950)


def test_excellent_branch():
    assert credit_band(800) == "excellent"


def test_good_branch():
    assert credit_band(700) == "good"


def test_fair_branch():
    assert credit_band(600) == "fair"


def test_poor_branch():
    assert credit_band(400) == "poor"


def test_unknown_employment_branch():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_age_below_limit():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_limit():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_age_within_limit():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_salaried_low_income():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_self_employed_low_income():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_sufficient_income():
    assert is_eligible(30, 50000, "self_employed", 800) is True


def test_poor_credit_rejected():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_good_credit_accepted():
    assert is_eligible(30, 50000, "salaried", 700) is True


def test_excellent_interest_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_interest_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_other_interest_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_self_employed_rate():
    assert interest_rate(600, "self_employed", False) == 14


def test_collateral_rate():
    assert interest_rate(600, "salaried", True) == 11


def test_no_collateral_rate():
    assert interest_rate(600, "salaried", False) == 13
