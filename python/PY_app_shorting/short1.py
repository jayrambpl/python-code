class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_info(self, name):
        filtered_data = [item for item in self.data if item[0] == name]
        if not filtered_data:
            return "Name not found in the data."
        sorted_data = sorted(filtered_data, key=lambda x: (x[1], x[2]))
        return sorted_data[0]

def main():
    sample_data = [
        ("Log4j changes include the following:", 1, 1),
        ("add-auth-operator", 1, 2),
        ("address-lookup", 2, 5),
        ("admin-control", 1, 8),
        ("asap-credit-authorization", 1, 9),
        ("asap-dataloader", 2, 3),
        ("asap-navigation-bar", 1, 6),
        ("asap-rates", 2, 4),
        ("asap-rental-agreement", 2, 7),
        ("asap-security", 1, 6),
        ("asap-thermal-printer", 2, 4)
    ]

    analyzer = DataAnalyzer(sample_data)

    inputs = [
        "address-lookup",
        "admin-control",
        "asap-credit-authorization",
        "asap-dataloader"
    ]

    for input_name in inputs:
        result = analyzer.get_info(input_name)
        print(f"{input_name}: {result[0]} \t {result[1]} \t {result[2]}")

if __name__ == "__main__":
    main()
