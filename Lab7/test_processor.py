
import pytest
from hypothesis import given, strategies as st

from processor import (
    credit_band,
    is_eligible,
    interest_rate
)


# ==========================================
# FUNCTION 1: CREDIT BAND FUZZ TESTS
# ==========================================

@given(st.booleans())
def test_credit_band_rejects_boolean_scores(score):
    with pytest.raises((TypeError, ValueError)):
        credit_band(score)


@given(
    st.floats(
        min_value=300.01,
        max_value=899.99,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_credit_band_rejects_decimal_scores(score):
    with pytest.raises((TypeError, ValueError)):
        credit_band(score)


@given(st.integers(min_value=300, max_value=900))
def test_credit_band_valid_scores(score):
    assert credit_band(score) in [
        "excellent",
        "good",
        "fair",
        "poor"
    ]


# ==========================================
# FUNCTION 2: LOAN ELIGIBILITY FUZZ TESTS
# ==========================================

@given(st.booleans())
def test_is_eligible_rejects_boolean_age(age):
    with pytest.raises((TypeError, ValueError)):
        is_eligible(age, 50000, "salaried", 750)


@given(st.booleans())
def test_is_eligible_rejects_boolean_income(income):
    with pytest.raises((TypeError, ValueError)):
        is_eligible(25, income, "salaried", 750)


@given(
    st.sampled_from([
        "intern",
        "unemployed",
        "contractor",
        ""
    ])
)
def test_is_eligible_rejects_unknown_employment(employment):
    with pytest.raises(ValueError):
        is_eligible(25, 50000, employment, 750)


@given(
    st.integers(min_value=21, max_value=60),
    st.integers(min_value=25000, max_value=100000),
    st.integers(min_value=650, max_value=900)
)
def test_is_eligible_valid_inputs(age, income, score):
    result = is_eligible(
        age, income, "salaried", score
    )
    assert isinstance(result, bool)


# ==========================================
# FUNCTION 3: INTEREST RATE FUZZ TESTS
# ==========================================

@given(
    st.sampled_from([
        "intern",
        "unemployed",
        "contractor",
        ""
    ])
)
def test_interest_rate_rejects_unknown_employment(employment):
    with pytest.raises(ValueError):
        interest_rate(750, employment, True)


@given(
    st.sampled_from([
        None,
        "yes",
        1,
        0
    ])
)
def test_interest_rate_rejects_invalid_collateral(collateral):
    with pytest.raises((TypeError, ValueError)):
        interest_rate(750, "salaried", collateral)


@given(st.booleans())
def test_interest_rate_valid_inputs(collateral):
    result = interest_rate(
        750, "salaried", collateral
    )
    assert isinstance(result, (int, float))
