sample_data = [
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

# Sort the sample data by type first, then by order
sorted_data = sorted(sample_data, key=lambda x: (x[1], x[2]))

# Print the sorted data
print("Name\t\tType\tOrder")
for entry in sorted_data:
    print(f"{entry[0]}\t{entry[1]}\t{entry[2]}")
