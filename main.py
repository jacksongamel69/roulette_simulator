import random
import csv
import matplotlib.pyplot as plt
import sys  # If you're doing command-line args


from roulette import Roulette
from strategies import (
    martingale,
    flat_betting,
    reverse_martingale,
    d_alembert,
    fibonacci
)
from analysis import analyze_results

def display_menu():
    """Display the strategy options and get user selection."""
    print("🎰 Jackson's Roulette Strategy Simulator 🎰\n")
    print("Choose a strategy:")
    print("1. Martingale          - Double initial bet amount after each loss")
    print("2. Flat Betting        - Same bet amount every time, win or lose.")
    print("3. Reverse Martingale  - Double initial bet size after each win")
    print("4. D'Alembert          - Increase bet by initial bet amount after loss, decrease bet size after win")
    print("5. Fibonacci           - Use Fibonacci sequence on losses: Increase your bet by adding the previous two bet amounts after each loss, and if you win, you move back two places in the sequence")
    print("6. Compare Strategies  - Compare all strategies with 1,000 spins")
    print("7. Exit                - Exit the program")
    choice = input("\nEnter the number of your strategy: ")
    return choice

def get_user_input():
    """Get input from the user for bankroll, starting bet, and max spins."""
    try:
        bankroll = float(input("Enter starting bankroll: $"))
        starting_bet = float(input("Enter your starting bet: $"))
        spins = int(input("Enter the maximum number of spins: "))
        return bankroll, starting_bet, spins
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")
        return get_user_input()  # Prompt again on invalid input


def compare_strategies_auto(trials=100, spins=100, bankroll=500, starting_bet=1):
    strategies = [
        ("Martingale", martingale),
        ("Flat Betting", flat_betting),
        ("Reverse Martingale", reverse_martingale),
        ("D'Alembert", d_alembert),
        ("Fibonacci", fibonacci)
    ]
    
    # To store final bankrolls per trial
    trial_results = {name: [] for name, _ in strategies}

    for trial in range(trials):
        for name, strategy in strategies:
            _, history = strategy(Roulette(), bankroll, starting_bet, spins)
            trial_results[name].append(history[-1])  # Final bankroll after `spins`

    # Compute averages after every 5 trials
    averaged_results = {name: [] for name in trial_results}
    trial_points = list(range(5, trials + 1, 5))  # [5, 10, ..., 100]

    for name in trial_results:
        for i in trial_points:
            avg = sum(trial_results[name][:i]) / i
            averaged_results[name].append(avg)

    # Save to CSV
    with open('strategy_comparison_by_trial.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['Trial'] + [name for name, _ in strategies]
        writer.writerow(header)
        for i, trial in enumerate(trial_points):
            row = [trial] + [averaged_results[name][i] for name, _ in strategies]
            writer.writerow(row)

    # Plot the graph
    for name in averaged_results:
        plt.plot(trial_points, averaged_results[name], label=name)

    plt.title("Strategy Comparison Over Trials")
    plt.xlabel("Number of Trials")
    plt.ylabel("Average Final Balance")
    plt.legend()
    plt.grid(True)
    plt.savefig("strategy_comparison_by_trial.png")
    plt.clf()





def compare_strategies(bankroll, starting_bet, spins):
    strategies = [
        ("Martingale", martingale),
        ("Flat Betting", flat_betting),
        ("Reverse Martingale", reverse_martingale),
        ("D'Alembert", d_alembert),
        ("Fibonacci", fibonacci)
    ]

    results = []
    history_data = {}

    for name, strategy in strategies:
        print(f"Running {name} Strategy...")
        _, history = strategy(Roulette(), bankroll, starting_bet, spins)
        history_data[name] = history
        final_balance = history[-1]
        total_change = final_balance - bankroll
        percentage_change = (total_change / bankroll) * 100
        results.append((name, final_balance, total_change, percentage_change))

    # Save data to CSV
    with open('compare_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Spin'] + [name for name, _ in strategies]
        writer.writerow(header)

        for i in range(spins):
            row = [i + 1]
            for name, _ in strategies:
                value = history_data[name][i] if i < len(history_data[name]) else ''
                row.append(value)
            writer.writerow(row)

    # Plot the data
    for name in history_data:
        plt.plot(range(1, len(history_data[name]) + 1), history_data[name], label=name)

    plt.xlabel('Spin Number')
    plt.ylabel('Bankroll')
    plt.title('Strategy Comparison Over Spins')
    plt.legend()
    plt.grid(True)
    plt.savefig('strategy_comparison.png')
    plt.close()

    # Print result summary
    results.sort(key=lambda x: x[2], reverse=True)
    print("\nStrategy Comparison (Sorted by Total Gain/Loss):\n")
    for name, final_balance, total_change, percentage_change in results:
        print(f"{name}: Final Balance = ${final_balance:.2f}, Total Gain/Loss = ${total_change:.2f} ({percentage_change:.2f}%)")

    print(f"\nThe best strategy was {results[0][0]} with the highest gain/loss.")

def main():
    while True:
        choice = display_menu()

        if choice == "7":  # If the user selected "Exit"
            break  # This will exit the loop and terminate the program
        elif choice == "6":
            # Compare all strategies with 1,000 spins
            bankroll, starting_bet, spins = get_user_input()
            compare_strategies(bankroll, starting_bet, spins)
        else:
            # Existing strategy code
            if choice == "1":
                strategy = martingale
            elif choice == "2":
                strategy = flat_betting
            elif choice == "3":
                strategy = reverse_martingale
            elif choice == "4":
                strategy = d_alembert
            elif choice == "5":
                strategy = fibonacci
            else:
                print("❌ Invalid choice. Please try again.")
                continue  # Return to the menu if choice is invalid

            # Get user input for bankroll, starting bet, and max spins
            bankroll, starting_bet, spins = get_user_input()

            print(f"\nRunning {strategy.__name__.replace('_', ' ').title()} Strategy...\n")

            final_balance, history = strategy(Roulette(), bankroll, starting_bet, spins)
            print(f"Final balance: ${final_balance:.2f}")
            print(f"Bets history: {history}")

            # Analyzing the results
            analyze_results(history)

            # Ask if the user wants to run another simulation
            again = input("\nWould you like to run another simulation? (y/n): ")
            if again.lower() != 'y':
                print("Thank you for using the Roulette Strategy Simulator!")
                break

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "auto":
        print(f"sys.argv: {sys.argv}")
        try:
            num_trials = int(sys.argv[2])
        except ValueError:
            print("Invalid number format for trials. Usage: python3 main.py auto 100")
            sys.exit(1)

        print(f"Running automatic comparison for {num_trials} trials of 100 spins each...")
        compare_strategies_auto(trials=num_trials, spins=100, bankroll=500, starting_bet=1)
    else:
        main()

