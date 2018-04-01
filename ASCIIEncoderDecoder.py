class ASCIIFormatTransporter:
    def __init__(self, file, alreadyEncoded):
        self.alreadyEncoded = alreadyEncoded
        if file:
            with open(file) as f:
                self.data = f.read()
        else:
            raise ValueError("Could not read file")

    '''
    Encode the data that is associated with the current instance class
    '''
    def encode(self):
        if self.alreadyEncoded:
            raise ValueError("Error, cannot encode data that has already been encoded!")
        else:
            self.data = self.encode_transform()
            self.alreadyEncoded = True


    def encode_transform(self):
        """Used run-length encoding data compression algorithm to encode ASCII art"""

        # if file is empty then simply return empty string
        if not self.data:
            return ""

        # store each encountered character, and number of repetitions
        current = None
        current_count = 0
        character_count_list = []
        for char in self.data:
            # Keep track of how many times a certain character appears consecutively
            # Store character and count in list once a differenct character is encountered
            if not current:
                current_count += 1
                current = char
            elif current != char:
                # a different character has been encountered
                # so now we append the character with its count to the list.
                # update variables current and current_count with the new char
                character_count_list.append( str(current_count) + str(current))
                current_count = 1
                current = char
            else:
                # increment count of repeated character
                current_count += 1

        # must account for last character that has not been appended to end of list
        character_count_list.append(str(current_count) + str(current))

        # return a string that contains the characters and associated counts present in the file
        return " ".join(character_count_list)

    def decode(self):
        if not self.alreadyEncoded:
            raise ValueError("This data has already been decoded")
        else:
            self.data = self.decode_transform()
            self.alreadyEncoded = False

    def decode_transform(self):
        if not self.data:
            return ""
        reversed_data = self.data[::-1]
        current = None
        repetitions = ""
        result = ""
        i = 0

        # the purpose of reversing the string is to ensure that the first character we encounter after a white
        # space is unambiguously a part of the original input string rather than the repetition number

        while i < len(reversed_data):
            if not current:
                # we know the first character in the string must be a part of the original string
                current = reversed_data[i]
                i += 1
            else:
                # we know that the before the beginning of a character there is a white space
                i += 1
                current = reversed_data[i]
                repetitions = ''
                # this is to access the first index of number of repetitions
                i += 1
            while i < len(reversed_data) and reversed_data[i] != ' ':
                # the repetition number may be greater than 10
                # so we must keep appending the digit until another white space is found
                repetitions += reversed_data[i]
                i += 1
            # we must reverse the repetition because we generated it in the wrong order
            # then we multiply the character by the correct repetition number
            # and append this to the result string
            result += current * int(repetitions[::-1])
        return result[::-1]












