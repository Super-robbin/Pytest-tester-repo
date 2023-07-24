class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = 'Be grateful for: '
        formatted += ', '.join(self.gratitudes)
        return formatted
    
    # We create a list, append multiple arguments (i.e. Makers, Food, Water)
    # Then, we format the list, we use ', '.join() to combine the list of arguments,
    # divided by ', ' (comma and whitespace) to return the final string.