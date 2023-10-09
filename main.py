from src.utils import get_all_operations, filter_operations, sort_operations_five
from src.utils2 import encode_cards
filename_ = "operations.json"

all_operations = get_all_operations(filename_)
filtered_operations = filter_operations(all_operations)
sorted_operations_five = sort_operations_five(filtered_operations)
sorted_operations_five.reverse()
print(encode_cards("1234567812345678"))
