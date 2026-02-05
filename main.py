import csv

print('Welcome to Expense Tracker')

name = input('Enter your name: ')
print('Hello', name)

while True:
    # amount validation loop
    while True:
        try:
            amount = float(input("Enter expense amount: "))
        
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("please enter a valid number (example: 25 or 25.5).")
            continue
        
    category = input('Enter expense category: ')

    print('Expense saved!')
    print('Amount:', amount)
    print('Category:', category)


    with open('expenses.csv', 'a', newline='')as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])
    
    print('Saved to expenses.csv')
    
    again = input('Add another expenses? (y/n): ')
    if again != 'y':
        break