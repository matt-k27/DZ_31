class GroupMaximumAmountError(Exception):
    def __init__(self, message="Group maximum amount error"):
        super().__init__()
        self.message = message