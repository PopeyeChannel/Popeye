import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.3)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik(' Terima kasih Mr.H4CKMU5')
mengetik(' Tuan sudah mengkonfirmasi identitas anda')
mengetik(' Mari sekarang SINTA antar Tuan')
mengetik(' Menuju ke Tools yang Tuan tuju')
mengetik(' ')
mengetik(' SALAM_HACKERS')