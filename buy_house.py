class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地%.2f平方米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python能够自动将一对括号内部的代码连接在一起，使代码看起来更简洁
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("添加%s" % item)
        # 1. 判断家具面积，太大添加不了
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" % item.name)

            return

        # 2. 将家具的名称添加到列表中
        self.item_list.append(item.name)

        # 3. 计算剩余面积
        self.free_area -= item.area


# 1.创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 21.5)

# 2.创建房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
