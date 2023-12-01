class Repetition:
    def __init__(self, pattern):
        self.pattern = pattern
        # still working on how to implement the pattern
        # this data structure will end up storing the indices from
        # the signal
        self.last_full_index = 0
        self.signal_indices = []
        self.complete = False

    def __str__(self):
        rep_str = ""
        for i in range(len(self.signal_indices)):
            rep_str += str(self.signal_indices) + " "
        return f"[{rep_str}]"

    def append_symbol(self, symbol, signal_index) -> bool:
        """
        This method returns true if the symbol appended is valid, else false
        If the symbol is valid this method will also store it in this object.
        :param symbol: either a 1 or 0 from the signal
        :return: true if can append else false
        """
        if self.is_complete():
            return False
#        print(f"{self.last_full_index}\n")
        if symbol == self.pattern[self.last_full_index]:
            # the symbol is a valid addition, update index and return True
            self.signal_indices.append(signal_index + 1)
            self.last_full_index += 1
            return True
        else:
            return False

    def is_complete(self) -> bool:
        if self.complete or self.last_full_index == len(self.pattern):
            self.complete = True
            return True
        else:
            return False

    def get_current_index(self) -> int:
        return self.last_full_index























