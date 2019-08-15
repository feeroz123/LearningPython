# This program calculates the total tax based on the States in US. Assume Federal Tax of 10%.


def get_tax(income, state):
    """
    This method calculates the tax applied based on Income and State values passed.
    :param income: Income amount
    :param state: State code in USA
    :return: Total Tax amount
    """

    # Assuming Federal Tax Rate of 10%
    fed_tax = 0.1

    if state == "SFO":
        state_tax = 0.2
    elif state == "NYC":
        state_tax = 0.25
    elif state == "OKL":
        state_tax = 0.15
    else:
        state_tax = 0.3
        print(f"\n** Default State Tax Rate applied: {state_tax * 100}% **")

    fed_tax_amount = income * fed_tax
    state_tax_amount = income * state_tax
    net_income = income - fed_tax_amount - state_tax_amount

    print("Net Income for Income {} and State {} is: {}".format(income, state, net_income))


get_tax(10000, "SFO")
get_tax(10000, "NYC")
get_tax(20000, "WAS")


