import math
import argparse 


def calculate_differentiated_payments(principal, periods, interest):
    over_payment = 0
    nominal_interest = interest / 1200
    for i in range(1, periods + 1):
        over_payment += math.ceil((principal / periods) + nominal_interest * (principal - ((principal * (i - 1)) / periods)))
        print(f'Month {i}: payment is {math.ceil((principal / periods) + nominal_interest * (principal - ((principal * (i - 1)) / periods)))}')
    print()
    print(f'Overpayment = {over_payment - principal}')

def display_calculation_decision():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for loan principal:')
    return input()


def calculate_monthly_payments(principal, payment, interest):
    nominal_interest = interest / 1200
    periods = math.ceil(math.log((payment / (payment - (nominal_interest * principal))) , (1 + nominal_interest)))
    if (periods / 12) > 1:
        if (periods % 12) == 0:
            print(f'It will take {periods // 12} years to repay this loan!')
        else:
            print(f'It will take {periods // 12} years and {periods % 12} months to repay this loan!')
    else:
        if (periods / 12) == 1:
            print('It will take 1 year to repay this loan!')
        else:
            if (periods % 12) == 1:
                print('It will take 1 month to repay this loan!')
            else:
                print(f'It will take {periods % 12} months to repay this loan!')
    print(f'Overpayment = {payment * periods - principal}')
                

def calculate_monthly_amount(principal, periods, interest):
    nominal_interest = interest / 1200
    print(f'Your annuity payment = {math.ceil(principal * ((nominal_interest * math.pow((1 + nominal_interest), periods)) / (math.pow((1 + nominal_interest), periods) - 1)))}!')
    print(f'Overpayment = {(math.ceil(principal * ((nominal_interest * math.pow((1 + nominal_interest), periods)) / (math.pow((1 + nominal_interest), periods) - 1))) * periods) - principal}')


def calculate_loan_principal(payment, periods, interest):
    nominal_interest = interest / 1200
    print(f'Your loan principal = {math.floor(payment * ((math.pow((1 + nominal_interest), periods) - 1) / (nominal_interest * math.pow((1 + nominal_interest), periods))))}!')
    print(f'Overpayment = {(payment * periods) - (math.floor(payment * ((math.pow((1 + nominal_interest), periods) - 1) / (nominal_interest * math.pow((1 + nominal_interest), periods)))))}')

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    number_of_arguments = 0
    parser.add_argument("--type")
    parser.add_argument("--principal")
    parser.add_argument("--interest")
    parser.add_argument("--periods")
    parser.add_argument("--payment")
    args = parser.parse_args()
    if args.type is not None:
        number_of_arguments += 1
    if args.principal is not None:
        number_of_arguments += 1
    if args.interest is not None:
        number_of_arguments += 1
    if args.periods is not None:
        number_of_arguments += 1
    if args.payment is not None:
        number_of_arguments += 1
    if args.type not in ['diff', 'annuity'] or args.type is None:
        print('Incorrect parameters')
    elif args.interest is None:
        print('Incorrect parameters')
    elif args.type == 'diff' and args.payment is not None:
        print('Incorrect parameters')
    elif number_of_arguments < 4:
        print('Incorrect parameters')
    elif args.principal is not None and int(args.principal) < 0:
        print('Incorrect parameters')
    elif args.interest is not None and float(args.interest) < 0:
        print('Incorrect parameters')
    elif args.periods is not None and int(args.periods) < 0:
        print('Incorrect parameters')
    elif args.payment is not None and int(args.payment) < 0:
        print('Incorrect parameters')
    else:
        if args.type == 'diff':
            calculate_differentiated_payments(int(args.principal), int(args.periods), float(args.interest))
        else:
            if args.principal is not None and args.periods is not None:
                calculate_monthly_amount(int(args.principal), int(args.periods), float(args.interest))
            elif args.periods is not None and args.payment is not None:
                calculate_loan_principal(int(args.payment), int(args.periods), float(args.interest))
            else:
                calculate_monthly_payments(int(args.principal), int(args.payment), float(args.interest))
