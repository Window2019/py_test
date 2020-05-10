#定义了一个Bicycle类
class Bicycle:
#定义了一个run方法，需要传入一个KM参数
    def run(self,km):
        print("自行车的骑行里程为{}""KM".format(km))

#括号内填写其他类名，可以继承它的方法
class EBicycle(Bicycle):
#构造函数
    def __init__(self,volume):
        self.volume = volume

    def get_volume(self):
        print("当前电量为" ,self.volume)
#定义方法
    def fill_charge(self,vol):
        print("充电的电量为",vol)

    def run(self):
#电瓶最大续航
        e_miles = self.volume * 10
#假如电瓶有10度电，支持的最大里程数就是10*10=100
        miles = km - e_miles
        if miles <=0:
            print("电瓶车骑了" , km)
        else:
            #因为子类有run方法，把父类的run覆盖掉了
            super.run(miles)
#实例化
EB = EBicycle(10)
EB.run(20)
