# クラス(データ型)の定義
class UserName:
    def __init__(self, name):
        self.name = name


bob = UserName(name='bob')
print(bob)


class UserName:
    def __init__(self, name, age):
        # nameのチェック
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}はルール違反です。')
        self.name = name
        self.age = age

    def battle_name(self):
        return self.name.upper()


bob = UserName(name='Bob Smith', age=19)
print(bob.name)
print(bob.battle_name())
print(bob.age)
