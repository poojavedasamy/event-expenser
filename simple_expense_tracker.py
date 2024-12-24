transactions_log = []
def record_transaction():
    entry_type = input("Enter type of transaction (e.g., Food, Rent): ")
    entry_amount = float(input("Enter the amount for the transaction: "))
    transactions_log.append({"type": entry_type, "amount": entry_amount})
    print("Transaction has been recorded!")

def display_transaction_history():
    if not transactions_log:
        print("No transactions recorded yet.")
        return
    print("\nTransaction History:")
    for idx, entry in enumerate(transactions_log, start=1):
        print(f"{idx}. {entry['type']} - ${entry['amount']:.2f}")
    print()

def total_spending():
    total_spent = sum(entry["amount"] for entry in transactions_log)
    print(f"Total amount spent: ${total_spent:.2f}")

def main_interface():
    while True:
        print("\nTransaction Manager")
        print("1. Record a Transaction")
        print("2. View Transaction History")
        print("3. Calculate Total Spending")
        print("4. Exit")
        user_selection = input("Select an option: ")
        
        if user_selection == "1":
            record_transaction()
        elif user_selection == "2":
            display_transaction_history()
        elif user_selection == "3":
            total_spending()
        elif user_selection == "4":
            print("Thank you for using the Transaction Manager!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main_interface()
