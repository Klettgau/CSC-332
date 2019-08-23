import numpy as np

table = {0:'A',1:'D',2:'F',3:'G',4:'V',5:'X'}

def seed_polybius(seed):
    encountered = set()
    poly=np.random.permutation(36).reshape((6,6))
    row = 0
    for pos,c in enumerate(seed):
        if pos >0 and pos%6 is 0:
            row +=1
        if c in encountered:
            break
        else:
            encountered.add(c)
            rez =np.where(poly ==(ord(c)-97))
            tmp = poly[row,(pos%6)]
            poly[row,pos%6] = ord(c)-97
            poly[rez[0],rez[1]] = tmp

    print(poly)
    return poly
def matrix_lookup(secret_key,secret_msg,poly):
    encoded = list()
    for pos, c in enumerate(secret_msg):
        res = np.where(poly==(ord(c)-97))
        encoded.append(table[res[0][0]]+table[res[1][0]])
    k=np.array(encoded).reshape((len(secret_msg)//4,4))
    #repeat letters when sorted will be undetermined
    headers = list()
    for pos, c in enumerate(secret_key):
        headers.append((c,pos))
    order = sorted(headers )

    print("encoded before the sort")
    print(k)
    for _,x in order:
        print([k[y,x] for y in range(4)])



msg_seed = "thebangles"
msg_key="riki"
secret_msg = "iliketomoveititt"
matrix =seed_polybius(msg_seed)
matrix_lookup(msg_key,secret_msg,matrix)
