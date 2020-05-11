class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp * 10
        self.power = self.power / 2
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        if self.hp > enemy_hp:
            print("天山童姥赢了")
        elif self.hp < enemy_hp:
            print("敌人赢了")
        else:
            print("平手")


tonglao = TongLao(1000, 200)
tonglao.see_people("李秋水")
tonglao.fight_zms(1000, 500)
