class Solution:
    def solve(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return

        # Place 1: always allowed
        numbers[index] = "1"
        self.solve(index + 1, True, numbers, result)

        # Place 0: allowed only if previous character wasn't 0
        if flag:
            numbers[index] = "0"
            self.solve(index + 1, False, numbers, result)

    def validStrings(self, n: int) -> List[str]:
        numbers = ["0"] * n
        result = []
        self.solve(0, True, numbers, result)
        return result