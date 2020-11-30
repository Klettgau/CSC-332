from PIL import Image as img

#only does Least significant bit storage.
#20201125 The bitshift logic was copying too many bits orrected this issues, now use a tui library

vessel_path = "robo.PNG"
secret_path = "gyarados.png"

vessel = img.open(vessel_path)

secret = img.open(secret_path)
print(vessel.size)
print(secret.size)


# vessel must be at least equal or greater in size due to no compression used
def check_size(vessel_img, secret_img):
    vwidth, vheight = vessel_img.size
    swidth, sheight = secret_img.size
    if swidth <= vwidth and sheight <= vheight:
        return True
    return False


def resize_image(vessel_img, secret_img):
    vwidth, vheight = vessel_img.size
    resize_secret = secret_img.resize((vwidth, vheight))  # this filter is optional
    return resize_secret


def merge_photo(vessel_img, secret_img):
    # main logic of looping over the two images
    # combine the MSB and LSB bits
    # rowxcol
    vessel_pix = vessel_img.load()
    secret_pix = secret_img.load()
    horocrux = img.new('RGBA', vessel_img.size)
    horocrux_pix = horocrux.load()

    for i in range(vessel_img.size[0]):
        for j in range(vessel_img.size[1]):
            # for each rgb pair in vessel and secret, grab them ,
            # call combine bits and then pass the tuple back to its pos
            rgb_updated = combine_bits(vessel_pix[i, j], secret_pix[i, j], 3, True, True)
            horocrux_pix[i, j] = rgb_updated
    horocrux.show()
    return horocrux


def unmerge_photo(vessel_img):
    vessel_pix = vessel_img.load()
    print(vessel_pix)
    horocrux = img.new('RGBA', vessel_img.size)
    horocrux_pix = horocrux.load()
    for i in range(vessel_img.size[0]):
        for j in range(vessel_img.size[1]):
            # for each rgb pair in vessel and secret, grab them ,
            # call combine bits and then pass the tuple back to its pos
            rgb_updated = seperate_bits(vessel_pix[i, j], 3, True, True)
            #print(f"{rgb_updated} index {i, j}")
            horocrux_pix[i, j] = rgb_updated
    horocrux.show()
    return horocrux

    return 1


# the grey valuesi 144,144,160 ????
def seperate_bits(vessel_rgb, bits_used, vessel_has_alpha, secret_has_alph):
    # for each tuple we take the MSB bits and turn into a seperate tuple for original , take LSB and set as MSB for the hidden image.
    r, g, b, alpha = vessel_rgb
    delta = 8 - bits_used
    lsb = 255 - (256-pow(2,bits_used))  # 1111 1111 -> 1110 0000 keep the 3 top bits
    return (((r & lsb) << delta) & 255, ((g & lsb) << delta) & 255, ((b & lsb) << delta) & 255, alpha)


def combine_bits(rgb_vessel, rgb_secret, bit_amt, vessel_has_alpha, secret_has_alpha):
    if secret_has_alpha:
        rs, gs, bs, alpha_secret = rgb_secret
    else:
        rs, gs, bs = rgb_secret
    if vessel_has_alpha:
        rv, gv, bv, alpha = rgb_vessel
    else:
        rv, gv, bv = rgb_vessel
    msb = (255 - (pow(2, (bit_amt)) - 1))  # 1111 1111  -> 1111 1000 3 secret bits
    lsb = 255 - (pow(2, 8 - bit_amt) - 1)  # 1111 1111 -> 1110 0000 keep the 3 top bits
    # need to rework the bitwise logic here for combining
    return ((msb & rv) | (rs & lsb) >> 8 - bit_amt, (msb & gv) | (gs & lsb) >> 8 - bit_amt,
            msb & bv | (bs & lsb) >> 8 - bit_amt, alpha)


# doesnt cap the int to a byte argh!!!


secret_updated = resize_image(vessel, secret)
imgy = merge_photo(vessel, secret_updated)
unmerge_photo(imgy)
