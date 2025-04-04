from pathlib import Path
from re import compile

def get_bin(n: int, fill: int) -> str:
    return bin(n)[2:].zfill(fill)

def binary_prefix_range(r):
    fill = 16
    bin_strs = set((get_bin(x, fill) for x in r))
    suffix = ""
    while True:
        for i in bin_strs.copy():
            if not i:
                break
            _i = int(i, base=2)
            if _i & 1:
                if (pred_i := get_bin(_i - 1, fill - len(suffix))) in bin_strs:
                    bin_strs.remove(i)
                    bin_strs.remove(pred_i)
                    to_add = list(i)
                    to_add[-1] = "*"
                    bin_strs.add("".join(to_add))

        
        if all(x.endswith("*") for x in bin_strs):
            bin_strs = {x[:-1] for x in bin_strs}
            suffix += "*"
        else:
            break

    return sorted((x +  suffix for x in bin_strs))


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
    print(len(binary_prefix_range(range(1, 65534))))