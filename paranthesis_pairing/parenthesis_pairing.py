class Text:
    """A piece of text to be analyzed.

    Attributes:
        submitted_text: Text to be inspected as string
    """

    opening_parenthesis = '('
    closing_parenthesis = ')'

    def __init__(self, submitted_text):
        """Return a new Text object."""
        self.submitted_text = submitted_text

    def count_parenthesis_pairs(self):
        """Returns count of parenthesis pairs in text.
        Does NOT take position into account.
        Returns -1 if an uneven number of brackets.
        """
        count_opening_parenthesis = self.submitted_text.count(self.opening_parenthesis)
        count_closing_parenthesis = self.submitted_text.count(self.closing_parenthesis)

        if count_opening_parenthesis == count_closing_parenthesis:
            return count_opening_parenthesis
        else:
            return -1

    def verify_parenthesis_balance(self):
        """Returns True if parenthesis balance is correct.
        Warning!!: If NONE, then technically speaking its balanced, so it passes.
        """
        if self.count_parenthesis_pairs() == -1: # Fail if uneven number
            return False

        # Fail if closer at beginning or opener at end
        location_first_opener = self.submitted_text.find(self.opening_parenthesis)
        location_first_closer = self.submitted_text.find(self.closing_parenthesis)
        location_last_opener = self.submitted_text.rfind(self.opening_parenthesis)
        location_last_closer = self.submitted_text.rfind(self.closing_parenthesis)

        if ( location_first_opener > location_first_closer or
            location_last_opener > location_last_closer ):
            return False

        return True

    def get_list_of_parenthesis_content(self):
        """Returns a list of the contents of each pair of parenthesis."""
        if ( self.count_parenthesis_pairs() == -1 or
                self.count_parenthesis_pairs() == 0 or
                self.verify_parenthesis_balance() == False):
            return False

        modified_text = self.submitted_text[:]
        parsed_contents = []

        while self.opening_parenthesis in modified_text:
            closing_location = modified_text.find(self.closing_parenthesis) + 1
            opening_location = modified_text.rfind(self.opening_parenthesis, 0, closing_location)

            parsed_contents.append(self.submitted_text[opening_location:closing_location])

            slice = modified_text[opening_location:closing_location]
            modified_text = modified_text.replace(slice, '*' * len(slice))

        return parsed_contents
