from collections import Counter

orders = {
    "An":["Cà phê", "Trà sữa", "Bánh ngọt"],
    "Bình":["Trà đào", "Cà phê", "Cà phê"],
    "Chi":["Sinh tố", "Bánh ngọt"],
    "Dũng":["Cà phê", "Trà sữa", "Trà sữa"]
} 
item= set()
for items in orders.values():
    item.update(items)

print("Các món quán bán ra:",item)

unique_count = {name: len(set(items)) for name, items in orders.items()}
print("Số món khác nhau:",unique_count)

item_to_customers = {}
for customer, items in orders.items():
    for item in set(items):
        item_to_customers.setdefault(item, set()).add(customer)
poular_count = {item: len(customers) for item, customers in item_to_customers.items()}
max_count = max(poular_count.values())
most_popular = [item for item, count in poular_count.items() if count == max_count]
print("Món phổ biến nhất:", most_popular, "(", max_count, "khách hàng)")