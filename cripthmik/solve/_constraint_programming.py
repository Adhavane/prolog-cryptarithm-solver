from typing import List, Set

from ..utils import Cryptarithm
from ._generate_and_test import GenerateAndTest
from ._prolog import Rule


class ConstraintProgramming(GenerateAndTest):
    """A solver that uses Constraint Programming to solve cryptarithms.
    
    Attributes:
        rules: A list of rules that are used to solve the cryptarithm.
        
    Methods:
        _all_digits: Generates rules for all the digits in the cryptarithm.
        _all_diff: Generates a rule that ensures all the digits are different.
        _diff: Generates a rule that ensures a digit is different from a value.
        _test: Generates a rule that tests the cryptarithm.
        
    Example:
        >>> from cripthmik.solve import ConstraintProgramming
        >>> solver = ConstraintProgramming()
        >>> cryptarithm = Cryptarithm("SEND + MORE = MONEY")
        >>> for solution in solver.solve(cryptarithm):
        ...     print(solution)
    """

    _rules: List[Rule] = [":- use_module(library(clpfd))"]

    def __init__(self):
        super().__init__()

    def _all_digits(self, letters: Set[str]) -> Set[Rule]:
        return {f"{letter} in 0..9" for letter in letters}

    def _all_diff(self, letters: Set[str]) -> Rule:
        return f"all_different([{','.join(letters)}])"

    def _diff(self, letter: str, value: int) -> Rule:
        return f"{letter} #\\= {value}"

    def _test(self, cryptarithm: Cryptarithm) -> Rule:
        return super()._test(cryptarithm).replace("=:=", "#=")
