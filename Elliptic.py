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

    # Tinh cac diem y^2
    def pow_y_2(self):
        arr = []
        p = self.p
        a = self.a
        b = self.b
        for i in range(p):
            x = (pow(i, 3) + a*i + b)%p
            arr.append(x)
        return arr

    # Kiem tra n co thuoc Q_p
    def la_tp_trong_Q_p(self, n):
        arr = self.Q_p()
        for i in range(len(arr)):
            if n==arr[i]:
                return 'Y'
        return 'N'

    # Ket qua cac diem thuoc va khong thuoc Q_p cho bang tong hop
    def Q_p_table(self):
        arr = []
        yp2 = self.pow_y_2()
        for i in range(len(yp2)):
            x = self.la_tp_trong_Q_p(yp2[i])
            arr.append(x)
        return arr

    # Tinh y1, y2
    def tim_y1_y2(self, n):
        p = self.p
        for i in range(p):
            x = pow(i, 2)%p
            if n==x:
                return i, p-i
        return 0
    # The hien y1, y2 cho bang tong hop
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

    # Bang tong hop cac diem thuoc duong cong eliptic
    def bang_tong_hop(self):
        a = self.pow_y_2()
        b = self.Q_p_table()
        c, _c = self.y1_y2_array()
        show =  pd.DataFrame([a,b,c,_c], columns=[i for i in range(len(a))], index = ['y^2', 'y^2inQp', 'y1', 'y2'])
        print(show)

    # Hien thi cac diem
    def hien_thi_cac_diem(self):
        arr = []
        b = self.Q_p_table()
        c, _c = self.y1_y2_array()
        for i in range(len(b)):
            if b[i] == 'Y':
                # arr.append(str(c[i])+'-'+str(_c[i]))
                arr.append([c[i], _c[i]])
        for i in range(len(b)):
            if b[i] == 'Y':
                # arr.append(str(_c[i])+'-'+str(c[i]))
                arr.append([_c[i], c[i]])
        return arr

    #Cap cua duong cong
    def l(self, x1, y1, x2, y2):
        if x1==x2 & y1==y2:
            l1 = 3*pow(x1, 2)+a
            l2 = 2*y1
        else:
            l1 = abs(y2-y1)
            l2 = abs(x2-x1)
        l = ((l1%p)*modInverse(l2,p))%p

        return l

    #Tinh tong hai diem
    def x3y3(self,x1, y1, x2, y2):
        l = self.l(x1, y1, x2, y2)
        x3 = abs(pow(l,2)-x1-x2);
        y3 = abs(l*(x1-x3)-y1);
        x3%=p
        y3%=p
        x3 = abs(x3)
        y3 = abs(y3)
        return [x3, y3]

    def x3y3Set(self, x1, y1):
        arr = []
        n = len(self.hien_thi_cac_diem())+1
        x2 = x1;
        y2 = y1
        for i in range(n):
            x= self.x3y3(x1, y1, x2, y2)
            arr.append(x)
            x2 = x[0]
            y2 = x[0]
        return arr

    def hien_thi_mot_diem(self, x1, x2):
        arr = self.x3y3Set(x1, x2)
        for i in range(len(arr)):
            print(i+2,'P =(',arr[i][0],arr[i][1], ')' )
    def thuoc_ECC(self,a):
        arr = self.hien_thi_cac_diem()
        for i in range(len(arr)):
            if a[0]==arr[i][0]&a[1] ==arr[i][1]:
                return'Y'
        return 'N'
    def mang1(self, x1, x2):
        arr = self.x3y3Set(x1, x2)
        arr1 = []
        for i in range(len(arr)):
            x = [arr[i][0], arr[i][1]]
            arr1.append(x)
        return arr1

    def hien_thi_cac_cap(self):
        arr = self.hien_thi_cac_diem()
        for i in range(len(arr)):
            print('* (',arr[i][0],',',arr[i][1],')')

            self.hien_thi_cac_diem(arr[i][0], arr[i][1])




if __name__ == '__main__':
    # p = 1380864490032731408911462402432229722964523240629
    p = 83
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
    ell.hien_thi_mot_diem(16,67)

