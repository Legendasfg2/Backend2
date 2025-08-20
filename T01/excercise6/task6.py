import json
import sys


def merge_sorted(list1, list2):
    """Сливает два отсортированных по 'year' списка фильмов"""
    i = j = 0
    merged = []
    while i < len(list1) and j < len(list2):
        if not isinstance(list1[i], dict) or not isinstance(list2[j], dict):
            return None
        if "year" not in list1[i] or "year" not in list2[j]:
            return None
        if not isinstance(list1[i]["year"], int) or not isinstance(
            list2[j]["year"], int
        ):
            return None
        if list1[i]["year"] <= list2[j]["year"]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("Incorrect input")
        return

    if not isinstance(data, dict) or "list1" not in data or "list2" not in data:
        print("Incorrect input")
        return

    list1, list2 = data["list1"], data["list2"]
    if not isinstance(list1, list) or not isinstance(list2, list):
        print("Incorrect input")
        return

    merged = merge_sorted(list1, list2)
    if merged is None:
        print("Incorrect input")
        return

    result = {"list0": merged}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
