class Cylinder:
    from decimal import Decimal
    import math
    def __init__(self,r=None,h=None,bottom_area=None,d=None,area_C=None,C=None,V=None,π='3.14',count_mian=2):
        self.r=r
        self.bottom_area=bottom_area
        self.h=h
        self.d=str(d)
        self.C=C
        self.V=V
        self.π=π
        self.count_mian=count_mian
        if area_C==None and r!=None:
            self.r=str(self.r)
            self.r=self.Decimal(self.r)
            self.area_C_init=self.Decimal(2*self.Decimal(π)*self.r)
        elif area_C==None and d!=None:
            self.d=str(self.d)
            self.π=self.Decimal(self.π)
            self.d=self.Decimal(self.d)
            self.area_C_init=self.Decimal(self.π*self.d)
        elif area_C!=None:
            self.π=self.Decimal(self.π)
            self.area_C_init=self.Decimal(str(area_C))
            self.r=self.area_C_init/self.π/2
    def Get_Volume(self):
        '''
        You can get the "Volume" of the Cylinder in this function.
        你可以得到这个圆柱的体积在这个函数。
        '''
        if self.r!=None and self.h!=None:
            self.r=str(self.r)
            self.r=self.Decimal(self.r)
            self.h=self.Decimal(self.h)
            self.π=self.Decimal(self.π)
            self.bottom_area=self.π*self.r*self.r      #计算出圆柱的底面积 公式: π(≈3.14)*r(半径)*r
            self.bottom_area=self.Decimal(self.bottom_area)
            self.V=self.bottom_area*self.h      #计算出圆柱的体积,公式: V=sh    体积等于底面积乘以高  
            self.V=self.Decimal(self.V)
            print(self.bottom_area,'*',self.h,'=',self.V)    #打印出计算的结果
            return(self.V)
        elif self.bottom_area!=None and self.h!=None:
            self.bottom_area=str(self.bottom_area)
            self.bottom_area=self.Decimal(self.bottom_area)    #初始化底面积
            self.h=self.Decimal(self.h)      #初始化高
            self.V=self.bottom_area*self.h      #计算出圆柱的体积,公式: V=sh    体积等于底面积乘以高  
            self.V=self.Decimal(self.V)
            print(self.bottom_area,'*',self.h,'=',self.V)    #打印出计算的结果
            return(self.V)
        elif self.C!=None and self.h!=None:
            self.C=self.Decimal(str(self.C))    #初始化 周长 高 π
            self.h=self.Decimal(self.h)
            self.π=self.Decimal(self.π)
            self.r=self.C/self.π/2    #计算出半径并初始化为Decimal对象
            self.bottom_area=self.π*self.r*self.r      #计算出圆柱的底面积 公式: π(≈3.14)*r(半径)*r
            self.bottom_area=self.Decimal(self.bottom_area)
            self.V=self.bottom_area*self.h      #计算出圆柱的体积,公式: V=sh    体积等于底面积乘以高  
            self.V=self.Decimal(self.V)
            print(self.bottom_area,'*',self.h,'=',self.V)    #打印出计算的结果
            return(self.V)
        elif self.d!=None and self.h!=None:
            self.d=str(self.d)
            self.d=self.Decimal(self.d)
            self.h=self.Decimal(self.h)
            self.π=self.Decimal(self.π)
            self.r=self.Decimal(self.d/2)    #计算出半径的值 (用直径除以2)
            self.bottom_area=self.π*self.r*self.r      #计算出圆柱的底面积 公式: π(≈3.14)*r(半径)*r
            self.bottom_area=self.Decimal(self.bottom_area)
            self.V=self.bottom_area*self.h      #计算出圆柱的体积,公式: V=sh    体积等于底面积乘以高  
            self.V=self.Decimal(self.V)
            print(self.bottom_area,'*',self.h,'=',self.V)    #打印出计算的结果
            return(self.V)
    def Get_Surface(self):
        if self.r==None and self.d!=None:    #如果半径没有值，并且直径有值,半径就等于直径除以2
            self.r=self.Decimal(self.d/2)
        self.π=self.Decimal(self.π)    #初始化π的类型，方便后面计算
        self.Lateral_area=self.Decimal(self.area_C_init*self.h)    #计算出侧面积, 公式底面积的周长*高
        if self.h!=None:     #如果高有值
            if self.bottom_area!=None:     #如果底面积没有值
                self.Surface=self.Decimal(self.Lateral_area+(self.bottom_area*self.count_mian))    #表面积就等于侧面积加上两个底面积(可通过修改count_mian变量来更改底面的计算数量)
            elif self.bottom_area==None:      #如果底面积没有值
                self.bottom_area=self.Decimal(self.r*self.r*self.π)    #计算出底面积的值 公式: 半径*半径*π
                self.Surface=self.Decimal(self.Lateral_area+(self.bottom_area*self.count_mian))     #表面积就等于侧面积加上两个底面积(可通过修改count_mian变量来更改底面的计算数量)
            print('表面积:',self.Surface)   #打印计算的结果
            print('侧面积:',self.Lateral_area)
if __name__ == '__main__':
    test=Cylinder(bottom_area=30,h=10)
    test.Get_Volume()
