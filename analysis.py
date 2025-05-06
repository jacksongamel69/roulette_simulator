import matplotlib.pyplot as plt

def analyze_results(history_or_balance, starting_bankroll=None):
    # Case 1: Called with history (list of bankrolls)
    if isinstance(history_or_balance, list):
        history = history_or_balance
        print(f"Final bankroll: ${history[-1]:.2f}")
        print(f"Total change: ${history[-1] - history[0]:.2f}")
        print(f"Total spins: {len(history)}")

        plt.plot(history)
        plt.title("Bankroll Over Time")
        plt.xlabel("Spin Number")
        plt.ylabel("Bankroll ($)")
        plt.grid(True)
        plt.savefig("results.png")
        plt.close()
        print("Plot saved as 'results.png'")

    # Case 2: Called with final_balance and starting_bankroll
    else:
        final_balance = history_or_balance
        profit = final_balance - starting_bankroll
        print(f"\n💰 Summary: You started with ${starting_bankroll:.2f} and ended with ${final_balance:.2f}.")
        if profit > 0:
            print(f"📈 Profit: ${profit:.2f}")
        elif profit < 0:
            print(f"📉 Loss: ${-profit:.2f}")
        else:
            print("⚖️ You broke even.")



