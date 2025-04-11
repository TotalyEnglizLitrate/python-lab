from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
from pprint import pprint
from typing import Self

PARENT_DIR: Path = Path(__file__).parent

class LinearEquation:
    def __init__(
            self,
            coefficients: tuple[Fraction],
            equals: Fraction) -> None:
        self.coefficients = coefficients
        self.equals = equals

    def __str__(self) -> str:
        eqn = []
        for var, coeff in zip(range(123 - len(self.coefficients), 123), self.coefficients):
            eqn.append(f"{coeff}{var}")
            eqn.append("+")
        eqn.append("=")
        eqn.append(self.equals)
        return " ".join(eqn)

    @classmethod
    def from_string(cls: Self, equation: str) -> Self:
        equation_list: list[str] = equation.strip().split()
        coefficients: tuple[Fraction] = tuple(map(lambda x: 1 if len(x) == Fraction(1) else Fraction(x[:-1]), equation_list[:-2:2]))

        return cls(coefficients=coefficients, equals=Fraction(equation_list[-1]))


class AugmentedEquationMatrix:
    def __init__(
            self,
            unknown_count: int,
            equations: tuple[LinearEquation],
            matrix: list[list[Fraction]]) -> None:
        self.unknown_count = unknown_count
        self.equations = equations
        self.matrix = matrix

    def __str__(self: Self) -> str:
        return str(self.matrix)

    __repr__ = __str__


    @classmethod
    def from_group(cls: Self, group: list[str]) -> Self:
        equations: tuple[LinearEquation] = tuple((LinearEquation.from_string(eq) for eq in group))
        unknown_count: int = len(group)

        if any((len(eq.coefficients) != unknown_count for eq in equations)):
            raise ValueError("All equations in a given group must contain an equal number of unknowns")
        
        matrix: list[list[int]] = []
        for eq in equations:
            matrix.append([])
            matrix[-1].extend(eq.coefficients)
            matrix[-1].append(eq.equals)

        return cls(unknown_count=unknown_count, equations=equations, matrix=matrix)

    def solve(self: Self) -> dict[str, Fraction]:
        matrix: list[list[Fraction]] = deepcopy(self.matrix)
        for idx, line in enumerate(matrix):
            leading_idx = 0

            # Make the leading entry a 1
            while not line[leading_idx]:
                leading_idx += 1
            print(line[leading_idx])
            for i in range(leading_idx, len(line)):
                line[i] = Fraction(line[i].numerator * line[leading_idx].denominator, line[i].denominator * line[leading_idx].numerator)

            # Eliminate entries above and below
            for other_idx, other_line in enumerate(matrix):
                if other_idx == idx or not other_line[leading_idx]: continue
                for i in range(len(other_line) - 1, -1, -1):
                    other_line[i] = other_line[i] - other_line[leading_idx] * line[i]
            
            pprint(matrix)
            print("\n\n\n")


def main() -> None:
    with open(PARENT_DIR / "sample_ex9.txt") as sample_fl:
        data = sample_fl.readlines();

    groups: list[list[str]] = []
    prev_line = ''
    for line in data:
        line = line.strip()
        if line:
            if not prev_line:
                groups.append([])
            groups[-1].append(line)
        
        prev_line = line

    if not groups[-1]:
        groups.pop()    
    
    matrices: list[AugmentedEquationMatrix] = [AugmentedEquationMatrix.from_group(group) for group in groups]

    matrices[0].solve()

if __name__ == "__main__":
    main()