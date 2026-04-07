class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, ctg):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {ctg.name}")
            ctg.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        bill = self.name.center(30, '*') + '\n'
        for i in self.ledger:
            desc = i['description'][:23].ljust(23)
            amt = f"{i['amount']:.2f}".rjust(7)
            bill += f"{desc}{amt}\n"
        bill += f"Total: {self.get_balance():.2f}"
        return bill

# --- outside class ---
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    expense = []
    for category in categories:
        spent = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
        expense.append(spent)
    
    # for category in categories:
    #     spent = 0
    #     for i in category.ledger:
    #         if i['amount']<0:
    #             spent += abs(i['amount'])
    #     expense.append(spent)
    
    total_expense = sum(expense)

    percentage = [int((s / total_expense) * 100 // 10) * 10 if total_expense > 0 else 0 for s in expense]
    # percentage = []
    # for spent_amount in expense:
    #     if total_expense > 0:
    #         percentage.append(int((spent_amount / total_expense) * 100 // 10) * 10)
    #     else:
    #         percentage.append(0)

    for y in range(100, -1, -10):
        chart +=f'{str(y).rjust(3)}| '
        for p in percentage:
            chart += "o  " if p >= y else "   "
        chart += "\n"

    chart += "    "+"-"*(len(categories)*3+1)+"\n"
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))