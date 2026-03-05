import random


def generate_secret_number(low=1, high=100):
    return random.randint(low, high)


def parse_guess(user_input):
    try:
        return int(user_input)
    except ValueError:
        return None


def check_guess(guess, secret):
    # FIXME: guess comparison bug (argument order + outputs)
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


def generate_hint(secret, guess):
    # FIXME: bug in hint logic
    if guess < secret:
        return "Try a higher number."
    elif guess > secret:
        return "Try a lower number."
    else:
        return "You got it!"