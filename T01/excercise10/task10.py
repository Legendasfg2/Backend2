def main():
    import sys

    try:
        N, total_time = map(int, input().split())
        machines = []
        for _ in range(N):
            year, cost, time = map(int, input().split())
            machines.append((year, cost, time))
    except:
        print("Incorrect input")
        return

    # группируем по году выпуска
    from collections import defaultdict

    year_dict = defaultdict(list)
    for year, cost, time in machines:
        year_dict[year].append((cost, time))

    min_total_cost = None

    # проверяем все годы
    for year, machine_list in year_dict.items():
        L = len(machine_list)
        for i in range(L):
            for j in range(i + 1, L):
                cost1, time1 = machine_list[i]
                cost2, time2 = machine_list[j]
                if time1 + time2 == total_time:
                    total_cost = cost1 + cost2
                    if min_total_cost is None or total_cost < min_total_cost:
                        min_total_cost = total_cost

    if min_total_cost is not None:
        print(min_total_cost)
    else:
        print("Incorrect input")


if __name__ == "__main__":
    main()
