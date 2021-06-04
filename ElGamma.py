from utils import *

class ElGamal():
    def __init__(self, p, a, k):
        self.p = p
        self.a = a
        self.k = k

    def Tao_khoa(self):
        p = self.p
        a = self.a
        Alpha = 2
        Beta = pow_mod(Alpha, a, p)
        return Alpha, Beta

    def Ma_hoa(self,x):
        k = self.k
        p = self.p
        Alpha, Beta = self.Tao_khoa()
        y1 = pow_mod(Alpha, k, p)
        y21 = x%p
        y22 = pow_mod(Beta, k, p)
        y2 = (y21*y22)%p;
        return y1, y2

    def Giai_ma(self, y1, y2):
        p = self.p
        a = self.a
        d1 = y2%p
        d2 = powModInverse(y1, a, p)
        d = (d1*d2)%p
        return d

if __name__ == '__main__':
    # p = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    p =10007
    a = 513
    k = 1010
    x = 339220 % p
    print('Ban ma:',x)
    elg = ElGamal(p, a, k)
    print('Tao khoa:')
    print(elg.Tao_khoa())
    print('Ma hoa:')
    print(elg.Ma_hoa(x))
    print('Giai ma:')
    y1, y2 = elg.Ma_hoa(x)
    print(elg.Giai_ma(y1, y2))
