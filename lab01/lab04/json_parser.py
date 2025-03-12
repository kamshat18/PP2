import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    print("{:<50} {:<20} {:<10} {:<10}".format(
        interface["dn"], interface.get("descr", "inherit"), interface["speed"], interface["mtu"]
    ))
