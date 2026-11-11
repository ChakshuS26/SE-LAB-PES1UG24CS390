
import math


MIN_INCOME = {
    "salaried": 25000,
    "self_employed": 40000
}


def credit_band(score):
    # Reject Boolean and non-integer credit scores
    if isinstance(score, bool) or not isinstance(score, int):
        raise TypeError("Credit score must be an integer")

    # Validate credit score range
    if score < 300 or score > 900:
        raise ValueError("Credit score must be between 300 and 900")

    if score >= 750:
        return "excellent"
    elif score >= 650:
        return "good"
    elif score >= 550:
        return "fair"

    return "poor"


def is_eligible(age, income, employment, score):
    # Validate age
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("Age must be an integer")

    # Validate income
    if isinstance(income, bool) or not isinstance(income, (int, float)):
        raise TypeError("Income must be a number")

    if not math.isfinite(income):
        raise ValueError("Income must be finite")

    if income < 0:
        raise ValueError("Income cannot be negative")

    # Validate employment type
    if not isinstance(employment, str):
        raise TypeError("Employment must be a string")

    if employment not in MIN_INCOME:
        raise ValueError("Unknown employment type")

    # Validate credit score
    band = credit_band(score)

    # Check eligibility conditions
    if age < 21 or age > 60:
        return False

    if income < MIN_INCOME[employment]:
        return False

    if band == "poor":
        return False

    return True


def interest_rate(score, employment, has_collateral):
    # Validate employment type
    if not isinstance(employment, str):
        raise TypeError("Employment must be a string")

    if employment not in MIN_INCOME:
        raise ValueError("Unknown employment type")

    # Validate collateral value
    if not isinstance(has_collateral, bool):
        raise TypeError("Collateral must be True or False")

    # Validate credit score and determine credit band
    band = credit_band(score)

    # Calculate base interest rate
    if band == "excellent":
        rate = 8
    elif band == "good":
        rate = 10
    else:
        rate = 13

    # Additional interest for self-employed applicants
    if employment == "self_employed":
        rate += 1

    # Discount for collateral
    if has_collateral:
        rate -= 2

    return rate


if __name__ == "__main__":
    print("===== LOAN ELIGIBILITY APPLICATION =====")

    score = 780
    age = 25
    income = 50000
    employment = "salaried"
    collateral = True

    print("Credit Score:", score)
    print("Credit Band:", credit_band(score))

    print(
        "Loan Eligible:",
        is_eligible(age, income, employment, score)
    )

    print(
        "Interest Rate:",
        interest_rate(score, employment, collateral),
        "%"
    )
