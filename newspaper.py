from itertools import combinations

def find_combinations(budget, newspapers):

    combinations_list = []
    for i in range(1, len(newspapers)+1):
        comb = combinations(newspapers, i)
        combinations_list.extend(comb)

    valid_combinations = []
    for comb in combinations_list:
        total_cost = 0
        for newspaper in comb:
            total_cost += newspapers[newspaper]

        if total_cost <= budget:
            valid_combinations.append(comb)

    return valid_combinations

newspapers = {
    "TOI": 26,
    "Hindu": 20.5,
    "ET": 34,
    "BM": 10.5,
    "HT": 18
}


print(find_combinations(40, newspapers))

