import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if args.type == "annuity":
    if args.payment and args.periods and args.interest:
        nominal_interest = (1 / 12) * (args.interest / 100)
        loan_principal = (args.payment
                          / ((nominal_interest * math.pow(1 + nominal_interest, args.periods))
                             / (math.pow(1 + nominal_interest, args.periods) - 1)))

        print(f"Your loan principal = {math.floor(loan_principal)}!")
        print(f"Overpayment = {math.ceil(args.periods * args.payment - loan_principal)}")
    elif args.principal and args.payment and args.interest:
        nominal_interest = (1 / 12) * (args.interest / 100)
        payment_count = math.ceil(math.log(args.payment / (args.payment - nominal_interest * args.principal)
                                           , 1 + nominal_interest))
        months = payment_count % 12
        years = payment_count // 12

        if years and months:
            print(f"It will take {years} {'year' if years == 1 else 'years'}"
                  , f"and {months} {'month' if months == 1 else 'months'} to repay this loan!")
        elif years:
            print(f"It will take {years} {'year' if years == 1 else 'years'} to repay this loan!")
        else:
            print(f"It will take {months} {'month' if months == 1 else 'months'} to repay this loan!")
        print(f"Overpayment = {math.floor(args.payment * (months + (years * 12)) - args.principal)}")
    elif args.principal and args.periods and args.interest:
        nominal_interest = (1 / 12) * (args.interest / 100)
        annuity_payment = (args.principal
                           * ((nominal_interest * math.pow(1 + nominal_interest, args.periods))
                              / (math.pow(1 + nominal_interest, args.periods) - 1)))

        print(f"Your monthly payment = {math.ceil(annuity_payment)}!")
        print(f"Overpayment = {int(math.ceil(annuity_payment)* args.periods - args.principal)}")
    else:
        print("Incorrect parameters")
elif args.type == "diff" and args.principal and args.periods and args.interest and not args.payment:
    nominal_interest = (1 / 12) * (args.interest / 100)
    running_sum = 0
    for m in range(1, args.periods + 1):
        differentiated_payment = (args.principal / args.periods) + nominal_interest \
                                 * (args.principal - ((args.principal * (m - 1)) / args.periods))
        running_sum += math.ceil(differentiated_payment)

        print(f"Month {m}: payment is {math.ceil(differentiated_payment)}")

    print(f"\nOverpayment = {int(running_sum - args.principal)}")
else:
    print("Incorrect parameters")
