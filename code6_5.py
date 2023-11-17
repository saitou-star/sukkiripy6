class Hero:
    name = '松田'
    hp = 100
    def sleep(self, hours):
        print(f'{self.name}は{hours}時間た！')
        self.hp += hours


# ゲーム開始
print('スッキリファンタジーⅤ ~金色のユートピア~')
h = Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')