# Dictionary
student_data = dict(name="Ayush", rollno="18", branch="IoT")
print(f"data = {student_data.get('name', 'no name')}")

chai_order = {}
chai_order["type"] = "masala-chai"
chai_order["size"] = "medium"

print(f"list = {chai_order}")
print(f"type = {chai_order['type']}")

chai_order = {"type": "ginger", "size": "medium", "sugar": 2}
print(f"keys = {chai_order.keys()}")
print(chai_order.values())
print(f"items = {chai_order.items()}")

last_item = chai_order.popitem()
print(f"removed item {last_item}")
print(f"orrr = {chai_order}")
slast_item = chai_order.pop("size", None)
print(f"removed item {slast_item}")
print(f"orrr = {chai_order}")