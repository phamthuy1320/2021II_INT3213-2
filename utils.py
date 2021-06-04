import math

# so nguyen to
def SNT(a):
    if a<2:
        return False;
    count = 0;
    for i in range(2,a,1):
        if a%i==0:
            count+=1
            return False
    if count==0:
        return True

# cac so nguyen to nho hon n
def SNT_mang(n):
    arr = []
    for i in range(2,n,1):
        if SNT(i)==True:
            arr.append(i)
    return arr
# Uoc chung lon nhat
def UCLN(p, q):
    while q != 0:
        p, q = q, p % q
    return p

# So nguyen to cung nhau
def NTCN (a, b):
    return UCLN(a,b)==1

def NTCN_gan_nhat(a):
    arr = SNT_mang(a)
    # arr1 = [NTCN(n, a) for n in arr]
    return arr[-1]
#
# print(NTCN_gan_nhat(3101))
# 3089

# modulo mu a^b%n
def pow_mod(b, e, m):
    if m==1:
        return 0
    c = 1
    for a in range(e):
        c = (c*b)%m
    return c

# modulo nghich dao a^-1 (mod m)
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

#modulo luy thua nghich dao (x^a)^-1 (mod m)
def powModInverse(x,a,m):
    for i in range(1,m):
        if ((pow_mod(x,a,m)) * (i%m)) % m == 1:
            return i

    return 1
#Cac thua so nguyen to
def TSNT (x):
    arr =[]
    for i in range(2,x,1):
        if x%i==0 & SNT(i)==True:
            arr.append(i)
    return arr
# Kiem tra n co phai phan tu nguyen thuy
def KTLTNT(n, p):
    arr = TSNT(p-1)
    for i in arr:
        _p = p/i
        _n = pow(n,_p)%p
        if _n !=1:
            return True
    return False

# Luy thua nguyen thuy
def LTNT(p):
    for i in range(1,p,1):
        if KTLTNT(i,p)==True:
            return i
    return 0
