def check_sequence_type(eut_list):
    for element in eut_list:
        if element not in [0, 1]:
            return False
    return True


def changes_leading_by_0(eut_list):
    count = 0
    current = 0
    if eut_list[current] != 0:
        count += 1
        eut_list[current] = 0
    for number in eut_list:
        nxt = current + 1
        if nxt < len(eut_list) and number == eut_list[nxt]:
            count += 1
            eut_list[nxt] = 1 - number
        current = nxt
    return count, eut_list


def changes_leading_by_1(eut_list):
    count = 0
    current = 0
    if eut_list[current] != 1:
        count += 1
        eut_list[current] = 1
    for number in eut_list:
        nxt = current + 1
        if nxt < len(eut_list) and number == eut_list[nxt]:
            count += 1
            eut_list[nxt] = 1 - number
        current = nxt
    return count, eut_list


def minimum_quantity_of_changes(eut):
    if not check_sequence_type(eut):
        return 'please put a sequence of of coin flips with 0,1 elements'
    if len(eut) == 0:
        return 'please put a non empty sequence as input'
    if len(eut) == 1:
        return 0, eut
    eut_reverse = [i for i in eut]
    count1, list1 = changes_leading_by_0(eut)
    count2, list2 = changes_leading_by_1(eut_reverse)
    result = count1, list1
    if count2 < count1:
        result = count2, list2
    return result
