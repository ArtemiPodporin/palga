#11
def calculate_net_salary(gross_salary, tax_rate):
    net_salary = gross_salary * (100 - tax_rate) / 100
    return net_salary

def print_net_salaries(names, salaries, tax_rate):
    for i in range(len(names)):
        net_salary = calculate_net_salary(salaries[i], tax_rate)
        print(f"{names[i]}: netopalk = {net_salary}")

#19
def lowest_salary(palgad, inimesed):
    """Find the index of the person with the lowest salary."""
    min_salary = min(palgad)
    min_index = palgad.index(min_salary)
    min_person = inimesed[min_index]
    return min_index, min_person