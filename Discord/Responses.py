from random import choice, randint


def get_response(user_input: str)  -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well youre awfully silent'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'roll dice' in lowered:
        return f'You Rolled: {randint(1,6)}'
    else:
        return choice(['I do not understand',
                       'What are you talking about',
                       'Can you rephrase that'])