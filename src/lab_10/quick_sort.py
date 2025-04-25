from random import randint

def quick_sort(lst: list[int], pivot=-1) -> list[int]:
    if len(lst) == 1:
        return lst
    pivot = pivot % len(lst)
    l_subarray = []
    r_subarray = []
    for i in lst:
        if i > lst[pivot]:
            r_subarray.append(i)
        else:
            l_subarray.append(i)
    
    if not (r_subarray and l_subarray):
        return quick_sort(lst, pivot=(pivot - 1) % len(lst))
    print(f"{pivot=}; {l_subarray}, {r_subarray}")
    return quick_sort(l_subarray) + quick_sort(r_subarray)

if __name__ == "__main__":
    lst = [randint(0, 1000) for _ in range(30)]
    print(lst)
    print(quick_sort(lst))