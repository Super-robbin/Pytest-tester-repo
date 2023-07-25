class Present():
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception('A contents has already been wrapped.')
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception('No contents have been wrapped')
        return self.contents
    
    # We can't test both because they would conflict with each other,
    # therefore if we test the wrap(), if self.content = None it will fail,
    # because the EXCEPTION is ONLY raised if self.content = None

    # Note: if we change self.content = 90, hence the EXCEPTION is met,
    # (in this case the condition is self.content IS NOT None),
    # it means that the test will PASS, otherwise the test will FAIL.
    
