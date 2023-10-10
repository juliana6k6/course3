from src.utils import (get_all_operations, filter_operations,
                       sort_operations_five)
from src.utils2 import encode_cards, format_date, encode_score
filename_ = "operations.json"


all_operations = get_all_operations(filename_)
filtered_operations = filter_operations(all_operations)
sorted_operations_five = sort_operations_five(filtered_operations)
for operation in sorted_operations_five:
    date = format_date(operation["date"])
    description_operation = operation["description"]
    initial_count = operation["from"]
    final_count = operation["to"]
    counts = [initial_count, final_count]
    counts_new = []
    for count in counts:
        count_info = count.split()
        if count_info[0].lower() == "счёт":
            score_form = encode_score(count_info[1])
        else:
            score_form = encode_cards(count_info[1])
        score = count_info[0] + score_form
        score_split = " ".join(score)
        counts_new.append(score)
print(f""