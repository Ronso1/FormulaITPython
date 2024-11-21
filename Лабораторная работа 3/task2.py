def find_common_participants(list_of_guests_first, list_of_guests_second, divide=','):
    first_quests = list_of_guests_first.split(divide)
    second_quests = list_of_guests_second.split(divide)

    general_quests = list(set(first_quests).intersection(second_quests))
    general_quests.sort()
    return general_quests

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:", participants)