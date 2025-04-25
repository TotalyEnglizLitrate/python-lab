from random import randint

def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    
    l_subarray = lst[:len(lst) // 2]
    r_subarray = lst[len(lst) // 2:]

    print("Split:", l_subarray, r_subarray, sep="\n")
    
    l_subarray = merge_sort(lst[:len(lst) // 2])
    r_subarray = merge_sort(lst[len(lst) // 2:])

    sorted_lst = []
    i = j = to_append = 0
    while (i < len(l_subarray)) and (j < len(r_subarray)):
        if l_subarray[i] < r_subarray[j]:
            to_append = l_subarray[i]
            i += 1
        else:
            to_append = r_subarray[j]
            j += 1
        sorted_lst.append(to_append)

    while i < len(l_subarray):
        sorted_lst.append(l_subarray[i])
        i += 1
    

    while j < len(r_subarray):
        sorted_lst.append(r_subarray[j])
        j += 1

    print("Merge:", sorted_lst)
    return sorted_lst


if __name__ == "__main__":
    lst = [randint(0, 1000) for _ in range(30)]
    print(lst)
    print(merge_sort(lst))