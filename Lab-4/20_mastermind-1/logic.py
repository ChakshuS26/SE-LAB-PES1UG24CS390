def feedback(code, guess):
    # First, count exact matches.
    # Exact matches are resolved before partial matches.
    exact = 0
    remaining_code = []

    for code_symbol, guess_symbol in zip(code, guess):
        if code_symbol == guess_symbol:
            exact += 1
        else:
            remaining_code.append(code_symbol)

    # Then count partial matches.
    # Each code occurrence can be used at most once.
    partial = 0

    for guess_symbol in guess:
        if guess_symbol in remaining_code:
            partial += 1
            remaining_code.remove(guess_symbol)

    return exact, partial