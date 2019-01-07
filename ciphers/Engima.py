import ciphers.CustomParser as Parser
import string
from flask import request


from flask_restful import Resource
from flask import jsonify


class M3(Resource):
    """Represents the Enigma Machine used by the  Wehrmacht/Heer.


    Attributes:
        slow_rotor:This is the leftmost rotor,the rotor that steps the least.
        medium_rotor: This is the middle rotor,the rotor that double steps.
        fast_rotor:This is the rightmost rotor, steps for every character.
        reflector: This is the chosen reflector, it defualts to B reflector.
        stecker_board: This is the generated stecker board.
        fast_counter: Counts  the amount of times stepped for Fast Rotor
        medium_counter: Counts  the amount of times stepped for Middle Rotor.
        slow_counter: Counts the amount of times stepped for Slowest Rotor.
        right_rotor_ring: Ring setting for the Fastest Rotor.
        middle_rotor_ring: Ring setting for the Slow Rotor.
        left_rotor_ring: Ring setting for the Slowest Rotor.
        rotor_choices:This is a dictionary of the five rotor's wiring and
            the stepping position for each rotor.
        reflector:This is a dictionary that stores the two reflectors used.
    """

    def __init__(self):
        self.fast_rotor = rotor_choices[3]
        self.medium_rotor = rotor_choices[2]
        self.slow_rotor = rotor_choices[1]
        self.reflector = self.reflector['reflector_b']
        self.stecker_board = set()
        self.max_pairs = 10
        self.fast_counter = 25
        self.medium_counter = 0
        self.slow_counter = 0
        self.right_rotor_ring = 0
        self.middle_rotor_ring = 0
        self.left_rotor_ring = 0

    def get(self):
        """
        This is for all get requests for Enigma.

        Returns:
            The message decoded/encoded.
        """

        message = self.set_up()
        return jsonify({'message': (''.join(self.run_machine(message)))})

    def set_up(self):
        """
        Set up the machine according to user provided values.

        Returns:
             The user provided message.
        """
        custom_parser = Parser.Parsely.Enigma(Parser.Parsely)
        custom_parser = custom_parser.parse_args()
        self.create_stecker_board(custom_parser.stecker_pair)
        self.set_rotors(custom_parser.rotor_order[0], custom_parser.rotor_order[1], custom_parser.rotor_order[2])
        self.set_rotors_intial_position(custom_parser.start_position)
        self.set_ring_setting(custom_parser.ring_setting)
        return custom_parser.message.upper().strip()

    def run_machine(self, message):
        """
        Runs through each character and encodes/decodes it.
        Args:
            message:The user provided message.

        Returns:
             The outout of encoding/decoding the message.
        """
        output = []
        for z in message:
            if ord(z) >= 65 and ord(z) <= 90:
                self.step_rotors()
                z = self.stecker_board_output(z)
                forward_encode = self.forward(z)
                lamp_outout = self.reflector_result(forward_encode)
                reverse_encode = self.reverse(lamp_outout)
                steckerboard_final = self.stecker_board_output(chr(reverse_encode + 65))
                output.append(steckerboard_final)
            else:
                output.append(z)
        return output

    def step_rotors(self):
        """
            Steps the User Chosen Rotors of the Enigma Machine for each character.
            The Middle Rotor does  contain the double step flaw.

            Returns:
                No return value,updates internal position of the rotor.

            Raises:
                KeyError: The key doesn't exist in the rotor.
        """
        if chr(self.fast_counter + 65) is self.fast_rotor['step']:
            if chr(self.medium_counter + 65) is self.medium_rotor['step']:
                self.slow_counter += 1
            self.medium_counter += 1
        else:
            if chr(self.medium_counter + 65) is self.medium_rotor['step']:
                self.slow_counter += 1
                self.medium_counter += 1
        self.fast_counter += 1
        if self.fast_counter > 25:
            self.fast_counter = 0
        if self.slow_counter > 25:
            self.slow_counter = 0
        if self.medium_counter > 25:
            self.medium_counter = 0

    def set_rotors(self, slow, medium, fast):
        """
        Sets the Rotors to use from User Input.

        Args:
            slow:This is the leftmost rotor,the rotor that steps the least.
            medium: This is the middle rotor,the rotor that double steps.
            fast:This is the rightmost rotor, steps for every character.

        Returns:
            No return value,updates internal reference of chosen rotor.

        Raises:
            ValueError: The passed in rotor string is not a valid integer

        """
        self.fast_rotor = rotor_choices[int(fast)]
        self.medium_rotor = rotor_choices[int(medium)]
        self.slow_rotor = rotor_choices[int(slow)]

    def set_rotors_intial_position(self, user_input):
        """
        Sets the Rotors starting position.

        Args:
            user_input:The User Provided string of the rotors start position.

        Returns:
            No return values,updates the internal reference of the rotors position.
        """
        user_input = user_input.upper()
        self.fast_counter = ord(user_input[2]) - 65
        self.medium_counter = ord(user_input[1]) - 65
        self.slow_counter = ord(user_input[0]) - 65

    def check_valid_char(self, suspected_char):

        if ord(suspected_char) < 65 or ord(suspected_char) > 90:
            return False
        else:
            return True

    # if this returns false, the system assumes everything is self-steckered
    def check_stecker_restrictions(self, stecker_pair):
        """
        Checks if user provided stecker board pairs is valid.

        Args:
            stecker_pair: String that represent the stecker board pairs.

        Returns:
            True or False if the user provided values are valid.
        """
        no_spaces = stecker_pair.replace(" ", "")
        split_pair = stecker_pair.split()
        unique_chars = set(no_spaces)
        if len(no_spaces) != len(unique_chars) or len(split_pair) > self.max_pairs:
            if len(no_spaces) % 2 != 0:
                return False  # need even number of pairs
            return False  # raise the exception you reused a letter or had too many pairs
        else:
            return True

    def create_stecker_board(self, wire_pairing):
        """
        Thanks to Brian Neal's Enigma project as a reference steckerboard.
        Creates the Stecker Board based off the pairs provided by the User.
        Max amount of Pairs allowed are 10.

        Args:
            wire_pairing:Space seperated String that contains max 10 pairs
                IOT populate the Steckerboard.Example "AB HG LK ZI".

        Returns:
            No return values but can raise aborts if the request is malformed.
        """
        if not wire_pairing:
            return
        string_pairs = wire_pairing.upper().split()  # list of the combos
        pairs = set()  # this will allow us to avoid checking repeats
        if self.check_stecker_restrictions(wire_pairing) is True:
            for combo in string_pairs:
                if self.check_valid_char(combo[0]) and self.check_valid_char(combo[1]) is True:
                    x = combo[0]
                    y = combo[1]
                    if y != x and (y, x) not in pairs:
                        pairs.add((x, y))
                else:
                    return False  # raise an exception here so the api returns the error
            self.stecker_board = pairs
        print("failed")

    def stecker_board_output(self, char_to_be_stecker):
        """
        The result of the character passing through the steckerboard.
        Args:
            char_to_be_stecker: The current character to pass through the stecker.

        Returns:
            Either returns a character that is self-steckered or the result
            of the steckerboard.
        """
        stecker = self.stecker_board
        if not stecker:
            return char_to_be_stecker
        for pair in stecker:
            if char_to_be_stecker in pair:
                a, b = pair
                if char_to_be_stecker != a:
                    return a
                else:
                    return b
            else:
                return char_to_be_stecker

    def reflector_result(self, char):
        return self.reflector[char]

    def set_ring_setting(self, user_input):
        user_input = user_input.upper()
        self.right_rotor_ring = ord(user_input[2]) - 65
        self.middle_rotor_ring = ord(user_input[1]) - 65
        self.left_rotor_ring = ord(user_input[0]) - 65

    def forward(self, input):
        """
        The character is passed through the machine right to left.

        Args:
            input: The message to be passed through the machine.

        Returns:
            The char encoded/decoded is returned.
        """
        current_char = (ord(input) - 65) % 26
        for y in range(3, 0, -1):
            if y is 3:
                ring = self.right_rotor_ring
                count = self.fast_counter
            elif y is 2:
                ring = self.middle_rotor_ring
                count = self.medium_counter
            else:
                ring = self.left_rotor_ring
                count = self.slow_counter
            trans = (((current_char - ring) % 26) + count) % 26
            encoded = self.rotor_choices[y]['wiring'][trans]
            xx = (((ord(encoded) - 65) % 26) - count) % 26
            before_ring = (xx + ring) % 26
            current_char = before_ring
        return current_char

    def reverse(self, input):
        """
        The character is passed through the machine left to right.

        Args:
            input: The message to be passed through the machine.

        Returns:
            The char encoded/decoded is returned.
        """

        current_char = (ord(input) - 65) % 26
        for y in range(1, 4):
            if y is 3:
                ring = self.right_rotor_ring
                count = self.fast_counter
            elif y is 2:
                ring = self.middle_rotor_ring
                count = self.medium_counter
            else:
                ring = self.left_rotor_ring
                count = self.slow_counter
            trans = (((current_char - ring) % 26) + count) % 26
            encoded = self.rotor_choices[y]['wiring'].index(string.ascii_uppercase[trans])
            xx = (encoded - count) % 26
            beforeRing = (xx + ring) % 26
            if y is 3:
                beforeRing = (beforeRing) % 26
            current_char = beforeRing
        return current_char


rotor_choices = {
    1: {
        'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
        'step': 'Q'
    },
    2: {
        'wiring': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
        'step': 'E'
    },
    3: {
        'wiring': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        'step': 'V'
    },
    4: {
        'wiring': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
        'step': 'J'
    },
    5: {
        'wiring': 'VZBRGITYUPSDNHLXAWMJQOFECK',
        'step': 'Z'
    },
}
reflector = {
    'reflector_b': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',  # b reflector
    'reflector_c': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'  # c reflector
}
