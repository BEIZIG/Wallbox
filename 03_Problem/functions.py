def changes(eut_list):
    count = 0
    current = 0
    for number in eut_list:
        nxt = current + 1
        if nxt < len(eut_list) and number == eut_list[nxt]:
            count += 1
            eut_list[nxt] = 1 - number
        current = nxt
    return count, eut_list


def minimum_quantity_of_changes(eut):
    eut_reverse = [i for i in eut]
    eut_reverse.reverse()
    count1, list1 = changes(eut)
    count2, list2 = changes(eut_reverse)
    result = count1
    if count2 < count1:
        result = count2
    return result




