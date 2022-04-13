from sales_person import SalesPerson


def sales_sort(sales_person):
    return sales_person[2]


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        text = open(file_name, "r").read()
        text = text.split("\n")
        for line in text:
            line_text = line.split(",")
            person = (SalesPerson(int(line_text[0]), line_text[1]))
            for sale in line_text[2:]:
                person.enter_sale(float(sale))
            self.sales_people.append(person)

    def quota_report(self, quota):
        list_qr = []
        for person in self.sales_people:
            part = [person.get_id(), person.get_name(), person.total_sales(), person.met_quota(quota)]
            list_qr.append(part)
        return list_qr

    def top_seller(self):
        list_qr = []
        for person in self.sales_people:
            part = [person.get_id(), person.get_name(), person.total_sales()]
            list_qr.append(part)
        list_qr.sort(key=sales_sort, reverse=True)
        top_sellers = []
        count = 0
        while True:
            top_sellers.append(list_qr[count])
            if list_qr[count][2] == list_qr[count + 1][2]:
                count += 1
            else:
                break
        return top_sellers

    def individual_sales(self, e_id):
        index = 0
        for person in self.sales_people:
            if person.get_id() == e_id:
                return person
            else:
                index += 1

    def sales_frequencies(self):
        frequencies = {}
        list_of_sales = []
        for person in self.sales_people:
            sales = person.get_sales()
            for sale in sales:
                list_of_sales.append(sale)
        for sale in list_of_sales:
            frequencies[sale] = frequencies.get(sale, 0) + 1

        return frequencies





