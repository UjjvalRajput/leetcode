class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        stack = []
        for operation in operations:
            if operation not in "DC+": # if operation is a number
                record.append(int(operation))
            elif operation in "D":
                previous_entry = record[-1]
                double_prev = previous_entry * 2
                record.append(double_prev)
            elif operation in "C":
                record.pop()
            else: # +
                first = record[-1]
                second = record[-2]
                total = first + second
                record.append(total)
        return sum(record)


