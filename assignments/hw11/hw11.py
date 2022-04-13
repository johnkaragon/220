from sales_person import SalesPerson
from sales_force import SalesForce


def print_person(person):
    print(person.get_id())
    print(person.get_name())
    print(person.get_sales())
    print("\n")


def print_force(force):
    for person in force.get_force():
        print(person.get_id())
        print(person.get_name())
        print(person.get_sales())
        print("\n")



"""
sales_p1 = SalesPerson(12974367, "John Aragon")
print_person(sales_p1)

sales_p1.enter_sale(12.97)
sales_p1.set_name("Adam Swidzinski")
print_person(sales_p1)

sales_p1.enter_sale(15.18)
sales_p1.enter_sale(54.97)
sales_p1.enter_sale(213.75)
sales_p1.enter_sale(93.29)
print(sales_p1.total_sales())

print(sales_p1.met_quota(400.00))

sales_p2 = SalesPerson(12974368, "John Aragon")
print_person(sales_p2)
sales_p2.enter_sale(67.43)
sales_p2.enter_sale(98.37)
sales_p2.enter_sale(138.62)
sales_p2.enter_sale(95.08)

print()
print_person(sales_p2)
print(sales_p2.total_sales())
sales_p1.enter_sale(9.34)
print(sales_p1.total_sales())

print()
print(sales_p1.compare_to(sales_p2))
print()
print(sales_p1.__str__())

"""

microsoft_sales = SalesForce()
microsoft_sales.add_data("people.txt")
#print_force(microsoft_sales)
print(microsoft_sales.quota_report(400.00))
print(microsoft_sales.top_seller())
p_list = microsoft_sales.get_force()
print(p_list)
print(microsoft_sales.individual_sales(1267236))
print(microsoft_sales.sales_frequencies())
