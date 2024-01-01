def find_common_participants(participants_1, participants_2, separator = ","):
    list_1 = list(set(participants_1.split(separator)).intersection(list(participants_2.split(separator))))
    list_1.sort()
    return list_1

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
