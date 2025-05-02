from pathlib import Path

PARENT_DIR = Path(__file__).parent

def get_bin(x: int, fill: int = 8) -> str:
    return bin(x)[2:].zfill(fill)

def flatten(lst: list[list[str]]) -> list[str]:
    flattened = []
    for elem in lst:
        flattened.extend(elem)
    return flattened

def main() -> None:
    with open(PARENT_DIR / 'fw1.rl') as fl:
        _data = flatten([line[1:].split()[:2] for line in fl if line.strip()])
    data = [ipr.split('.') for ipr in _data]
    data = [ipr[:-1] + ipr[-1].split('/') for ipr in data]
    data = [tuple(map(int, ipr)) for ipr in data]

    with open(PARENT_DIR / 'fw1.rl.processed', 'w') as fl:
        for original, processed in zip(_data, data):
            to_replace = processed[-1]
            bin_str = ''.join((get_bin(processed[i]))  for i in range(len(processed) - 1))
            bin_str = bin_str[:len(bin_str) - to_replace] + '*' * to_replace
            print(f"{original.ljust(19)} : {bin_str}", file=fl)
if __name__ == "__main__":
    main()
