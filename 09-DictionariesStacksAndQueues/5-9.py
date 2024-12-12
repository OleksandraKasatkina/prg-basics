# Read the province data
province_file = "province.csv"
vehicle_file = "vehicle.txt"

# Create a dictionary to map letters to provinces
province_mapping = {}
with open(province_file, 'r') as pf:
    next(pf)  # Skip the header
    for line in pf:
        letter, name = line.strip().split(',')
        province_mapping[letter] = name

# Create a dictionary to count vehicles from each province
vehicle_counts = {province: 0 for province in province_mapping.values()}

# Read the vehicle data and count vehicles per province
with open(vehicle_file, 'r') as vf:
    for line in vf:
        registration = line.strip()
        province_letter = registration[0]  # The first letter of the registration number
        if province_letter in province_mapping:
            province_name = province_mapping[province_letter]
            vehicle_counts[province_name] += 1

# Print the results
for province, count in vehicle_counts.items():
    print(f"{province}: {count}")