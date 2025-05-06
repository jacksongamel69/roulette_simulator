def martingale(game, bankroll, base_bet, spins):
    bet = base_bet
    history = []

    for _ in range(spins):
        if bankroll < bet:
            break

        result = game.spin()
        win = game.is_win("red", result)

        if win:
            bankroll += bet
            bet = base_bet
        else:
            bankroll -= bet
            bet *= 2

        history.append(bankroll)
    return bankroll, history


def flat_betting(game, bankroll, base_bet, spins):
    history = []

    for _ in range(spins):
        if bankroll < base_bet:
            break

        result = game.spin()
        win = game.is_win("red", result)

        bankroll += base_bet if win else -base_bet
        history.append(bankroll)

    return bankroll, history


def reverse_martingale(game, bankroll, base_bet, spins):
    bet = base_bet
    history = []

    for _ in range(spins):
        if bankroll < bet:
            break

        result = game.spin()
        win = game.is_win("red", result)

        if win:
            bankroll += bet
            bet *= 2
        else:
            bankroll -= bet
            bet = base_bet

        history.append(bankroll)
    return bankroll, history


def d_alembert(game, bankroll, base_bet, spins):
    bet = base_bet
    history = []

    for _ in range(spins):
        if bankroll < bet:
            break

        result = game.spin()
        win = game.is_win("red", result)

        if win:
            bankroll += bet
            bet = max(base_bet, bet - base_bet)
        else:
            bankroll -= bet
            bet += base_bet

        history.append(bankroll)
    return bankroll, history


def fibonacci(game, bankroll, base_bet, spins):
    sequence = [base_bet, base_bet]
    position = 0
    history = []

    for _ in range(spins):
        if position >= len(sequence):
            sequence.append(sequence[-1] + sequence[-2])

        bet = sequence[position]
        if bankroll < bet:
            break

        result = game.spin()
        win = game.is_win("red", result)

        if win:
            bankroll += bet
            position = max(0, position - 2)
        else:
            bankroll -= bet
            position += 1

        history.append(bankroll)
    return bankroll, history

