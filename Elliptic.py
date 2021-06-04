from utils import *
import pandas as pd
import numpy

class Elliptic():
    '''
    (E) y^2 = x^3 + ax +b (mod p)
    '''
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def Q_p(self):
        arr =[]
        p = self.p
        len_Q = int((p+1)/2)
        for i in range(1,len_Q):
            x = pow(i, 2)%p
            arr.append(x)
        arr.sort()
        return arr

    def pow_y_2(self):
        arr = []
        p = self.p
        a = self.a
        b = self.b
        for i in range(p):
            x = (pow(i, 3) + a*i + b)%p
            arr.append(x)
        return arr

    def la_tp_trong_Q_p(self, n):
        arr = self.Q_p()
        for i in range(len(arr)):
            if n==arr[i]:
                return 'Y'
        return 'N'

    def Q_p_table(self):
        arr = []
        yp2 = self.pow_y_2()
        for i in range(len(yp2)):
            x = self.la_tp_trong_Q_p(yp2[i])
            arr.append(x)
        return arr

    def tim_y1_y2(self, n):
        p = self.p
        for i in range(p):
            x = pow(i, 2)%p
            if n==x:
                return i, p-i
        return 0
    def y1_y2_array(self):
        a = self.pow_y_2()
        b = self.Q_p_table()
        arr_y1 = []
        arr_y2 = []
        for i in range(len(a)):
            if b[i] == 'N':
                arr_y1.append('-')
                arr_y2.append('-')
            else:
                if b[i]=='Y':
                    x, _x = self.tim_y1_y2(a[i])
                    arr_y1.append(x)
                    arr_y2.append(_x)
        return arr_y1, arr_y2

    def bang_tong_hop(self):
        a = self.pow_y_2()
        b = self.Q_p_table()
        c, _c = self.y1_y2_array()
        show =  pd.DataFrame([a,b,c,_c], columns=[i for i in range(len(a))], index = ['y^2', 'y^2inQp', 'y1', 'y2'])
        print(show)

    def hien_thi_cac_diem(self):
        arr = []
        b = self.Q_p_table()
        c, _c = self.y1_y2_array()
        for i in range(len(b)):
            if b[i] == 'Y':
                arr.append(str(c[i])+'-'+str(_c[i]))
        for i in range(len(b)):
            if b[i] == 'Y':
                arr.append(str(_c[i])+'-'+str(c[i]))
        return arr

if __name__ == '__main__':
    p = 1380864490032731408911462402432229722964523240629
    a = 4
    b = 2
    ell = Elliptic(p, a, b)
    print('Với đường cong (E): y^2 = x^3 +',a,'x+',b,'(mod',p,')')
    arr = ell.Q_p()
    print('Q_',p,' có số phần tử là: ',len(arr))
    print('Q_',p,'=',arr)
    print('Ta có bảng biểu diễn sau:')
    ell.bang_tong_hop()
    print('Các điểm thuộc đường cong đã cho:')
    points = ell.hien_thi_cac_diem()
    print(points)
    print('Tổng số điểm:', len(points)+1)

