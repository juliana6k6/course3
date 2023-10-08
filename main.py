from src.utils import get_all_operations, filter_operations
filename_ = "operations.json"

all_operations = get_all_operations(filename_)
print(filter_operations(all_operations))
