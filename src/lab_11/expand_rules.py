from itertools import product
from functools import cache
from pathlib import Path
from typing import Optional, Self

PARENT_DIR = Path(__file__).parent

class BinaryPrefixString:
    def __init__(self, x: int, suffix: Optional[int] = None) -> None:
        self.value = x
        self.suffix = suffix or 0

    def __str__(self) -> str:
        return bin(self.value)[2:].zfill(16 - self.suffix) + "*" * self.suffix

    __repr__ = __str__
    
    def __hash__(self) -> int:
        return (self.value << (len(bin(self.suffix)) - 2)) + self.suffix

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

    
    return sorted((str(x) for x in bin_strs))

def get_bin(x: int, fill: int = 8) -> str:
    return bin(x)[2:].zfill(fill)

def get_lpm(lpm: str) -> str:
    ip, dont_care = lpm.split('/')
    dont_care = int(dont_care)
    return ''.join(get_bin(int(x)) for x in ip.split('.'))[:32 - dont_care] + '*' * dont_care


def main():
    with open(PARENT_DIR / 'fw1.rl') as fl:
        rules = fl.readlines()

    with open(PARENT_DIR / 'fw1.rl.processed', 'w') as fl:
        for rule in rules:
            print(rule, file=fl)
            tmp_r = rule[1:].split()
            tern_rule = []
            base_ternary_rule = f"{get_lpm(tmp_r[0])} {get_lpm(tmp_r[1])} "
            ipr_1 = binary_prefix_range(range(int(tmp_r[2]), int(tmp_r[4]) + 1))
            ipr_2 = binary_prefix_range(range(int(tmp_r[5]), int(tmp_r[7]) + 1))

            print(f"Total ternary rule expansions: {len(ipr_1) * len(ipr_2)}", file=fl)
            for _tern_rule in product(ipr_1, ipr_2):
                tern_rule.append(base_ternary_rule + " ".join(_tern_rule))
            
            print(*tern_rule, '\n', sep='\n', file=fl)


if __name__ == "__main__":
    main()