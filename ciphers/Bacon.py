import re
import ciphers.CustomParser as Parser
from flask_restful import Resource


class Bacon(Resource):
    def clean_message(self, msg, flag):
        # will remove spaces and punctation
        pat_space = re.compile("(\s)+", re.S)
        pat_punc = re.compile("[^\s\d\w]|_", re.S)
        msg = re.sub(pat_space, " ", msg)
        msg = re.sub(pat_punc, "", msg)
        spaces = list()
        for pos, c in enumerate(msg):
            if c is ' ':
                spaces.append(pos)
        msg = re.sub(pat_space, "", msg)
        if flag:
            return msg.upper(), spaces
        else:
            return msg, spaces

    def create_steno_msg(self, encoded_msg, vessel, vessel_spaces):
        steno = list()
        for pos, c in enumerate(encoded_msg):
            if c is 'A':
                steno.append(vessel[pos].lower())
            else:
                steno.append(vessel[pos].upper())
        steno = steno + list(vessel[len(encoded_msg):])
        for space in vessel_spaces:
            steno.insert(space, " ")
        return ''.join(steno)

    def check_length(self, hidden_msg, vessel):
        steno_msg_len_min = len(hidden_msg) * 5
        if len(vessel) < steno_msg_len_min:
            return False
        return True

    def encode(self, msg, vessel):
        parsed_msg, _ = self.clean_message(msg, True)
        vessel_clean, vesssel_spaces = self.clean_message(vessel, True)
        if self.check_length(parsed_msg, vessel_clean) is False:
            return False
        encoded_msg = ''.join([alph[x] for x in parsed_msg])
        return self.create_steno_msg(encoded_msg, vessel_clean, vesssel_spaces)

    def decode(self, encoded_msg):
        lookup = dict([(v, k) for (k, v) in alph.items()])
        abba = list()
        encoded_msg, spaces = self.clean_message(encoded_msg, False)
        for c in encoded_msg:
            if c.isupper():
                abba.append('B')
            else:
                abba.append('A')
        abba = ''.join(abba)
        msg_decoded = [lookup[abba[c:c + 5]] for c in range(0, len(abba), 5)]
        return ''.join(msg_decoded)


alph = {'A': 'AAAAA', 'I': 'ABAAA', 'B': 'AAAAB', 'C': 'AAABA',
        'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA',
        'H': 'AABBB', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
        'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB',
        'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
        'Y': 'BBAAA', 'Z': 'BBAAB', '_': 'BBBBB'}
