parlay_list = []

def is_positive(num):
    return num > 0

def parlay_calculator(bet_info):
    subset_recursion(0, 1, bet_info, [], [])
    return parlay_list

def subset_recursion(main_index, carry_over_score, bet_info, team_list, result_list):
    if main_index < len(bet_info):
        for i in range (3):
            previous_score = carry_over_score
            temp_num = int(bet_info[main_index]['odds'][i])
            if (is_positive(temp_num)):
                temp_parlay_score = float((100.0 + temp_num) / 100.0)
            else:
                temp_parlay_score = float((100.0 + abs(temp_num)) / abs(temp_num))
            team_list.append(bet_info[main_index]['teams'][i])
            result_list.append(bet_info[main_index]['result'][i])
            carry_over_score = carry_over_score * temp_parlay_score
            subset_recursion(main_index + 1, carry_over_score, bet_info, team_list, result_list)
            del team_list[-1]
            del result_list[-1]
            carry_over_score = previous_score
    else:
        temp_parlay_list_item = {}
        temp_parlay_list_item['teams'] = team_list
        temp_parlay_list_item['result'] = result_list
        temp_parlay_list_item['score'] = round(carry_over_score - 1, 2)
        print(temp_parlay_list_item)
        parlay_list.append(temp_parlay_list_item)

