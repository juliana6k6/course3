from src.utils import (get_all_operations, filter_operations,
                       sort_operations_five)
from src.utils2 import encode_cards, format_date, encode_score
filename_ = "operations.json"


def main():
    all_operations = get_all_operations(filename_)
    filtered_operations = filter_operations(all_operations)
    sorted_operations_five = sort_operations_five(filtered_operations)
    for operation in sorted_operations_five:
        date_ISO = operation["date"]
        date = format_date(date_ISO)
        description_operation = operation["description"]
        counts = []
        counts_new = []
        if "from" in operation:
            initial_count = operation["from"]
            counts.append(initial_count)
        else:
            initial_count = "НЕТ ДАННЫХ"
            counts_new.append(initial_count)
        final_count = operation["to"]
        counts.append(final_count)
        for count in counts:
            count_info = count.split()
            if count_info[0].lower() == "счёт":
                score_form = encode_score(count_info[1])
            else:
                score_form = encode_cards(count_info[-1])
            score = count_info[0] + " " + score_form
            score_split = " ".join(score)
            counts_new.append(score)
        initial_count_new = counts_new[0]
        final_count_new = counts_new[1]
        sum_operation = operation["operationAmount"]["amount"]
        currency_operation = operation["operationAmount"]["currency"]["name"]
        print(f"""{date} {description_operation}
{initial_count_new} > {final_count_new}
{sum_operation} {currency_operation}
_______________________________________________""")


main()
