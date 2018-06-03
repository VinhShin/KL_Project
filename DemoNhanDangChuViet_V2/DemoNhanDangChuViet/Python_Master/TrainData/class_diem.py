class Diem:
    def __init__(self, mssv, diemso,diemchu,mssvCnt,diemsoCnt,diemchuCnt):
        self.mssv = mssv
        self.diemso = diemso
        self.diemchu = diemchu
        self.mssvCnt = None
        self.diemsoCnt = None
        self.diemchuCnt = None
    def getMssv(self):
        return self.mssv
    def getDiemSo(self):
        return self.diemso
    def getDiemChu(self):
        return self.diemchu
    def setMssv(self, mssv):
        self.mssv = mssv
    def setDiemSo(self, diemso):
        self.diemso = diemso
    def setDiemChu(self, diemchu):
        self.diemchu = diemchu
    def setCntMssv(self, cnt):
        self.mssvCnt = cnt
    def setCntDiemSo(self, cnt):
        self.diemsoCnt = cnt
    def setCntDiemChu(self, cnt):
        self.diemchuCnt = cnt

