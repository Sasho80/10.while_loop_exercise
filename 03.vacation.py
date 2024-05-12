money_need_tour = float(input())
money_hand = float(input())
total_counter_days = 0
leave_money = 0
consecutive_days_counter = 0

while money_hand < money_need_tour and consecutive_days_counter < 5:
    type_action = input()
    amount = float(input())
    if type_action == "spend":
        leave_money = money_hand - amount
        consecutive_days_counter += 1
        if leave_money > 0:
            money_hand = leave_money
            leave_money = 0
        elif leave_money < 0:
            leave_money = 0
            money_hand = 0
    elif type_action == "save":
        consecutive_days_counter = 0
        leave_money = money_hand + amount
        money_hand = leave_money
        leave_money = 0
    total_counter_days += 1
if money_hand >= money_need_tour:
    print(f"You saved the money for {total_counter_days} days.")
elif consecutive_days_counter == 5:
    print(f"You can't save the money.")
    print(total_counter_days)
