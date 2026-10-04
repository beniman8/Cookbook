wining_combinations = [
    '123',
    '456',
    '789',
    '147',
    '258',
    '369',
    '159',
    '357'
]


def check_number(player_moves):

    for combination in wining_combinations:

        if all(number in player_moves for number in combination):
            return True

    return False