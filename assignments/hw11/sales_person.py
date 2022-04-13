class SalesPerson:
    def __init__(self, employee_id, name):
        self.name = name
        self.employee_id = employee_id
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc += sale
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        other_sales = other.total_sales()
        if self.total_sales() > other_sales:
            return 1
        if self.total_sales() == other_sales:
            return 0
        return -1

    def __str__(self):
        message = str(self.employee_id) + "-" + str(self.name) + ": " + str(self.total_sales())
        return message
