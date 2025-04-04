from functools import cache
from pathlib import Path
from typing import Optional, Self

class BinaryPrefixString:
    def __init__(self, x: int, suffix: Optional[int] = None) -> None:
        self.value = x
        self.suffix = suffix or 0

    def __str__(self) -> str:
        return bin(self.value)[2:].zfill(16 - self.suffix) + "*" * self.suffix

    def __repr__(self):
        return "\"" + str(self) + "\""
    
    def __hash__(self) -> int:
        return self.value << len(str(self.suffix)) + self.suffix

    def __eq__(self, other: Self):
        if not isinstance(other, BinaryPrefixString):
            return False
        return self.value == other.value and self.suffix == other.suffix
    


@cache # Cache the results of the function so as to not to recompute them
def binary_prefix_range(r: range) -> list[str]:
    bin_strs = set(BinaryPrefixString(x) for x in r)
    while True:
        changed = False
        for i in bin_strs.copy():
            if i.value & 1 and BinaryPrefixString(i.value - 1, i.suffix) in bin_strs:
                changed = True
                bin_strs.remove(i)
                bin_strs.remove(BinaryPrefixString(i.value - 1, i.suffix))
                
                # add back the combined binary prefix string after removing the
                # two strings being combined
                bin_strs.add(BinaryPrefixString(i.value >> 1, i.suffix + 1))

        if not changed:
            break

    
    return sorted(bin_strs, key=lambda x: str(x))


def main():
    # example: fw1.rl, ensure it is placed in same directory as this script
    with open(Path(__file__).parent / "fw1.rl") as in_fl:
        data = [x.split(":") for x in in_fl.readlines()]

    out_data = []
    for line in data:
        tmp = [x.split() for x in line]
        out_data.append(range(
            int(tmp[0][2]), int(tmp[1][0]) + 1
            ))

    # output the ranges and their corresponding binary prefix strings to a file
    # example: fw1.rl.processed
    with open(Path(__file__).parent / "fw1.rl.processed", "w") as out_fl:
        for rng in out_data:
            out_fl.write(f"{rng.start} : {rng.stop - 1} - ")
            out_fl.write(str(binary_prefix_range(rng)))
            out_fl.write("\n")

if __name__ == "__main__":
    main()