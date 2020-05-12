#一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
# 定义一个fight方法：
# final_hp = hp-enemy_power
# enemy_final_hp = enemy_hp - power
# 两个hp进行对比，血量剩余多的人获胜
class GAME:
    #函数构造,定义我的血量和我的攻击力
    def __init__(self):
        self.hp = 1000
        self.power = 2000
    #定义打斗方法
    def fight(self,enemy_power,enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        #比较我和敌人的最终生命
        if final_hp > enemy_final_hp:
            print("winner")
        else:
            print("lose")
    #实例化
g = GAME()
    #调用打斗方法，并且赋值 敌人的生命和攻击力
g.fight(800,1000)

class houyi(GAME):
    def __init__(self):
        self.defense = 100
    def defense(self,enemy_power,enemy_hp):
        final_hp = self.hp +self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        # 比较我和敌人的最终生命
        if final_hp > enemy_final_hp:
            print("winner")
        else:
            print("lose")