import Julius as jul
import Jefferson as jeff
import Vigenere as vig
import Affine as aff
import Engima
import Colors
import CustomParser
import argparse

color = Colors.textMod()
grandfather = CustomParser.Parsely()

def main():

    parser = argparse.ArgumentParser(description="Please Enter 0 for Caesar Cipher\n"
          "\nPlease Enter 1 for Affine Cipher\n"
          "Please Enter 2 for Vigenere Cipher\n"
          "Please Enter 3 for Jefferson Cipher\n"
          "Please Enter 4 for Enigma")
    parser.add_argument("-m", "--mode", help="this picks the type of cipher", type=int,required=True)
    args,unknown = parser.parse_known_args()

    if args.mode == 0:  # julius
        custom_parser=grandfather.parser_jules()
        custom_parser,unknown=custom_parser.parse_known_args()
        jul.display_values(custom_parser.key, custom_parser.text)
        encodeResult = jul.encode(custom_parser.text, custom_parser.key)
        jul.print_text(encodeResult, 0)
        decodedResult = jul.decode(encodeResult, custom_parser.key)
        print("decode result")
        jul.print_text(decodedResult, 1)
    elif args.mode == 1:  # affine  
        # key=m , wabbit =b
        custom_parser=grandfather.parser_jules()
        print(".....")
        custom_parser,unknown=custom_parser.parse_known_args()
        proposed_value, bol = aff.checkCoPrime(custom_parser.key, 26)
        if bol != True:
            print("Please pick one of these following coprime values", proposed_value)
        else:
            cipherText = aff.encode(custom_parser.text, custom_parser.key, custom_parser.intercept)
            print("\nBelow is the Decoded Text \n")
            aff.decode(cipherText, proposed_value, custom_parser.intercept)
    # need to add the ability to organize all 26
    elif args.mode == 2:  # jeff
        custom_parser=grandfather.parser_jeff()
        custom_parser,unknown=custom_parser.parse_known_args()

        cipherText = jeff.encode(custom_parser.text, custom_parser.key)
        print(cipherText)
        print(jeff.decode(cipherText, custom_parser.key))
    elif args.mode == 3:
        custom_parser=grandfather.parser_vig()
        custom_parser,unknown=custom_parser.parse_known_args()
        print(custom_parser.text, custom_parser.key)
        resy = vig.encode(custom_parser.text, custom_parser.key)
        print("Cipher-Text:", resy)
        print("Plain-Text:", vig.decode(resy, custom_parser.key))
    elif args.mode == 4:
        custom_parser=grandfather.parser_enig()
        custom_parser,unknown=custom_parser.parse_known_args()
        eng = Engima.M3()
        eng.vienna(custom_parser.text, custom_parser.stecker, custom_parser.ring, custom_parser.rotor, custom_parser.startPos)


if __name__ == '__main__':
    main()
