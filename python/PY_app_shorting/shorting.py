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
        ("Log4j changes include the following:", "Components", 1),
        ("add-auth-operator", "Components", 2),
        ("address-lookup", "App", 5),
        ("admin-control", "Components", 8),
        ("asap-credit-authorization", "Components", 9),
        ("asap-dataloader", "App", 3),
        ("asap-navigation-bar", "Components", 6),
        ("asap-rates", "App", 4),
        ("asap-rental-agreement", "App", 7),
        ("asap-security", "Components", 6),
        ("asap-thermal-printer", "App", 4)
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
