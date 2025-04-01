# Compare Two Lists.

def compare_lists(list1, list2):
    return {
        "same_length": len(list1) == len(list2),
        "same_sum": sum(list1) == sum(list2),
        "common_values": set(list1) & set(list2)
    }

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))
result = compare_lists(list1, list2)
print("Same length:", result["same_length"])
print("Same sum:", result["same_sum"])
print("Common values:", result["common_values"])