#11
def calculate_salary(gross_salary, tax_rate):
    net_salary = gross_salary - (gross_salary * tax_rate / 100)
    return net_salary
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]
tax_rate = 13 
for i in range(len(palgad)):
    net_salary = calculate_salary(palgad[i], tax_rate)
    print(f"{inimesed[i]}: netopalk = {net_salary}")
    
#19   
from palgad import lowest_salary

palgad = [12, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

min_index, min_person = lowest_salary(palgad, inimesed)

print("Väikseim palk on inimesel", min_person, "indeksiga", min_index)


