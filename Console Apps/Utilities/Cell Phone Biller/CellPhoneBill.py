from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')


def bill_ingredients(family_member):
    ''' Cell Phone Plan Rates Subtotal '''
    number_of_lines = 5
    line_one = 65
    line_two = 45
    additional_lines = 25
    prorated_charges = 4.17
    unlimited_basic_phone_plan = (prorated_charges + line_one + line_two + (
        additional_lines * (number_of_lines - 2))) / (number_of_lines)
    # print("Equally Divided Plan:", locale.currency(unlimited_basic_phone_plan, grouping=True))

    ''' Autopayment & Other Discounts '''
    discounts = 0
    autopay = True
    autopay_plan_discount = 5
    if autopay:
        discounts += autopay_plan_discount
    else:
        print("You can save by autopaying")

    if family_member == "Gavin":
        sprint_perks_discount = 5
        discounts += sprint_perks_discount
    elif family_member == "Hayden":
        line_on_us_three_unlimited_service_plan = 20
        prorated_charges = 3.33 + 0.83
        discounts += line_on_us_three_unlimited_service_plan + prorated_charges
    # if not discounts == 0:
    #     print("Discounts:", locale.currency(discounts, grouping=True))

    ''' Plans & Services Subtotal '''
    plans_and_services = unlimited_basic_phone_plan - discounts
    print("Plans & Services:", locale.currency(
        plans_and_services, grouping=True))

    ''' Hayden's Phone Payoff '''
    equipment = 0
    samsung_a11_lease = True
    if date.today() < date(2022, 12, 25) and samsung_a11_lease:
        if family_member == "Mama" or family_member == "Ellie" or family_member == "Blair":
            equipment += 7.50 / 3  # Hayden's Cell Phone
    if not equipment == 0:
        print("Equipment:", locale.currency(equipment, grouping=True))

    ''' Sprint Complete & Sprint Premium Services Subtotal '''
    sprint_complete = 0
    sprint_premium_services = 0
    protection_plan_for_Hayden = True
    if protection_plan_for_Hayden:
        if not family_member == "Hayden" and not family_member == "Ian":
            # Hayden's Protection Plan
            sprint_complete += ((1.5 + 9) / (number_of_lines - 1))
    if family_member == "Blair" or family_member == "Ian":
        sprint_complete += 19
    elif family_member == "Ellie":
        sprint_complete += 15
    elif family_member == "Gavin":
        sprint_complete -= 2.53
    if not sprint_complete == 0:
        print("Sprint Complete:", locale.currency(
            sprint_complete, grouping=True))
    if family_member == "Blair":
        sprint_premium_services += 9.99
    if not sprint_premium_services == 0:
        print("Sprint Premium Services:", locale.currency(
            sprint_premium_services, grouping=True))

    ''' Surcharges Subtotal '''
    surcharges = 0
    if not family_member == "Hayden":
        administrative_charge = 15
        federal_universal_service_access = 1.77
        kentucky_state_gross_receipts_surcharge = 0.53
        regulatory_charge = 5.94
        surcharges += (administrative_charge + federal_universal_service_access +
                       kentucky_state_gross_receipts_surcharge + regulatory_charge) / (number_of_lines - 1)
    if not surcharges == 0:
        print("Surcharges:", locale.currency(surcharges, grouping=True))

    ''' Government Taxes & Fees Subtotal '''
    government_taxes_and_fees = 0
    if not family_member == "Hayden":
        emergency_tax = 3.5
        lifeline_fee = 0.35
        sales_tax = 2.6
        trs_tap = 0.15
        government_taxes_and_fees += (emergency_tax + lifeline_fee +
                                      sales_tax + trs_tap) / (number_of_lines - 1)
    if not government_taxes_and_fees == 0:
        print("Government Taxes & Fees:", locale.currency(
            government_taxes_and_fees, grouping=True))

    ''' Totals Due '''
    due = sprint_premium_services
    if not family_member == "Hayden":
        due += plans_and_services + sprint_complete + \
            surcharges + government_taxes_and_fees
    if not family_member == "Hayden" or not family_member == "Gavin":
        due += equipment
    return locale.currency(due, grouping=True)


def bill(family_member):
    ''' Billing Function '''
    if family_member:
        print("Total Due: ", bill_ingredients(family_member))


def main():
    ''' Family Members to Be Billed '''
    print('\n', date.today().strftime("%A, %B %d, %Y"), '\n')
    family_members = ["Hayden", "Gavin", "Mama", "Ellie", "Blair"]
    for family_member in family_members:
        print(family_member)
        bill(family_member)
        print('\n')


main()