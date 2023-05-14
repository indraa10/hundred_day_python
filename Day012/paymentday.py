from datetime import datetime, timedelta

check_payment_date = True

while check_payment_date:

    print("-------- welcome to payment day calculation------------")
    time_format = "%d-%m-%y"
    current_date = datetime.now()
    formatted_current_date_string = current_date.strftime(time_format)
    formatted_current_date_datetime = current_date.strptime(formatted_current_date_string, time_format)

    lr_date = input("today is your LR date? if Yes type 'y' else 'n' : ").lower()
    site_day = int(input("enter site day to calculate payment date: e.g 21 : "))
    site_date = timedelta(days=site_day)
    new_date = formatted_current_date_datetime + site_date
    new_date_string = new_date.strftime(time_format)
    if lr_date == 'y':
        print(f"next payment date: {new_date_string}")
    else:
        input_time = input("enter LR date in dd-mm-yy format: ")
        input_lr_date_datetime = datetime.strptime(input_time, time_format)
        new_payment_date = input_lr_date_datetime + site_date
        new_payment_date_string = new_payment_date.strftime(time_format)
        print(f"next payment date: {new_payment_date_string}")

    check_more = input("Do you want to check another payment date: if Yes type 'y' else 'n': ").lower()
    if check_more == 'n':
        break

