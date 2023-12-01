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
        return f"[{self.root} {self.left} {self.right}]"

    def append_symbol(self, symbol, signal_index) -> bool:
        """
        This method returns true if the symbol appended is valid, else false
        If the symbol is valid this method will also store it in this object.
        :param symbol: either a 1 or 0 from the signal
        :return: true if can append else false
        """
        if self.complete:
            return False
        if symbol == self.pattern[self.last_full_index]:
            # the symbol is a valid addition, update index and return True
            self.signal_indices[self.last_full_index] = signal_index
            self.last_full_index += 1
        else:
            return False

    def is_complete(self) -> bool:
        if self.complete:
            return True
        else:
            return False

    def get_current_index(self) -> int:
        return self.last_full_index























