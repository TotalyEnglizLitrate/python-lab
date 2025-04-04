from pathlib import Path
from re import compile

def get_bin(n: int, fill = 16) -> str:
    return bin(n)[2:].zfill(fill)

def binary_prefix_range(r):
    bin_strs = [get_bin(x) for x in r]
    while True:
        old_bins = bin_strs.copy()
        for i in old_bins:
            i_stripped = i.rstrip("*")
            suffix = len(i) - len(i_stripped)
            if not i_stripped:
                break
            _i = int(i_stripped, base=2)
            if _i & 1:
                if (pred_i := get_bin(_i - 1, 16 - suffix) + "*" * suffix) in bin_strs:
                    bin_strs.remove(i)
                    bin_strs.remove(pred_i)
                    to_add = list(i_stripped)
                    to_add[-1] = "*"
                    to_add = "".join(to_add).zfill(16)
                    if to_add not in bin_strs:
                        bin_strs.append(to_add)
        
        if old_bins == bin_strs:
            break

    return sorted((x + "*" * suffix for x in bin_strs))


def main():
    with open(Path(__file__).parent / "fw1.rl") as in_fl:
        data = [x.split(":") for x in in_fl.readlines()]

    out_data = []
    for line in data:
        tmp = [x.split() for x in line]
        out_data.append(range(
            int(tmp[0][2]), int(tmp[1][0]) + 1
            ))

    with open(Path(__file__).parent / "fw1.rl.processed", "w") as out_fl:
        for rng in out_data:
            out_fl.write(f"{rng.start} : {rng.stop - 1} - ")
            out_fl.write(str(binary_prefix_range(rng)))
            out_fl.write("\n")

if __name__ == "__main__":
    # main()
    print(binary_prefix_range(range(1, 4)))