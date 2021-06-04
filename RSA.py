from utils import *
class RSA():
    def __init__(self,p,q, m, e):
        self.p = p
        self.q = q
        self.m = m
        self.e = e
    '''
        p va q, hai so nguyen to chon ban dau
        d so mu bi mat
        n modulo
        e mu cong khai
    '''
    def tao_khoa(self):
        p = self.p
        q = self.q
        n = p * q
        e = self.e
        # n = self.n
        phi = (p - 1) * (q - 1);
        d = modInverse(e, phi)
        return e, n, d

    def RSA_ma_hoa(self):
        m = self.m
        e, n, d = self.tao_khoa()
        c = pow(m, e)%n
        return c

    def RSA_giai_ma(self):
        c = self.RSA_ma_hoa()
        e, n, d = self.tao_khoa()
        de = pow(c, d)%n
        return de

if __name__ == '__main__':
    '''
    p, q: so nguyen to duoc chon
    m: ban ro ma hoa
    e: so mu cong khai
    n = pq 
    
    Voi n = 512 bit, chon:
    n= 
    '''
    # p = 61
    # q = 53
    p = 66879465661348111229871989287968040993513351195484998191057052014006844134449
    q = 109939025753834733498749075564102728424911782303658486825359178646821371085889
    n = p*q
    m = 123
    e = 65537

    rsa = RSA(p,q,m,e)
    e, n, d = rsa.tao_khoa()
    print('Khóa công khai là cặp (e, n) = (', e, ',', n, '). Khóa bí mật là d = ', d)
    print('Bản can ma hoa m =',m)
    c = rsa.RSA_ma_hoa()
    print('Ma hoa ', c)
    print('==========================================================================')
    print('Với bản ma hoa c =',c)
    d = rsa.RSA_giai_ma()
    print('Giải ma:', d)
