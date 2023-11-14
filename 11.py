# # name = "   13 gao jian bin xiao qing qing 456"
# # for i in range(len(name)):
# #     print(f"{name[i]}",end="")
# # print()
# # print(len(name))
# # print(name.index("i"))
# # print(name.replace("gao","GAO"))
# # name1 = name.split(" ")
# # print(name1)
# # print(f"name1 is {name1},the old is {name}")
# # print(f"the type of name1 is {type(name1)}")
# # lis = ["gao", "jian","bin", "nihao"]
# # a = lis.reverse()
# # print(a)
# # print("reverse", lis)
# # lis.sort()
# # # print(lis)

# name1 = '1  2  3  4  5  67  8'
# print(name1.split(' '))
# a = name.split(" ")
# print(a)
# # print(name.split(" "))
name = "  1 3 gao jian bin xiao qing qing 45\n   "
print(name.strip())
print(name)
name1 = name.strip("1 4g5")
print(name1)
print(type(name1))
# # a = name.upper()
# # print(a)
# # print(name.strip("1 4g5"))
# # print(name.count("i"))
# string = "gao jian bin ai xiao qing qing"
# print(f"the count of a is {string.count('a')}")
# print(f"replaced is the:\n{string.replace(' ','|')}")
# print(f"old is {string.split(' ')}")
#
# print(string[1::3])
# print(string[1:3])
# print(string[:18:5])
# print("--------------------------")
# tupl = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(tupl[0::-1])
# print("--------------------------")
# haha = "零基础，学IT，就来黑马程序员，月薪过万"
# haha1 = haha.split("，")[-2].replace("就来", "")[::-1]
# print(haha1)
# print("--------------------------")
# lis1 = [1,2,3,4,5,6,7]
# lis1.reverse()
# print(lis1)
#
#
#
#
#
#
#
#
#
#
#
#
# 8
#
#
#
#
#
import itertools

# def calculate_pi():
#     terms = itertools.count(1, step=2)
#     pi_estimate = 0
#     sign = 1
#
#     for term in terms:
#         pi_estimate += sign * (4 / term)
#         sign = -sign
#         yield pi_estimate
#
# if __name__ == "__main__":
#     pi_generator = calculate_pi()
#     while True:
#         current_estimate = next(pi_generator)
#         print(f"当前估计值：{current_estimate}")
# import random
#
# def calculate_pi_monte_carlo():
#     inside_circle = 0
#     total_points = 0
#
#     while True:
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
#         distance = x**2 + y**2
#
#         if distance <= 1:
#             inside_circle += 1
#
#         total_points += 1
#         pi_estimate = 4 * (inside_circle / total_points)
#         yield pi_estimate
#
# if __name__ == "__main__":
#     pi_generator = calculate_pi_monte_carlo()
#     while True:
#         current_estimate = next(pi_generator)
#         print(f"当前估计值：{current_estimate}")

import mpmath

# def calculate_pi_decimal_places(digits):
#     mpmath.mp.dps = digits  # 设置计算精度
#     pi = mpmath.pi
#     return str(pi)  # 将π的值转换为字符串以保留所有小数位
#
# if __name__ == "__main__":
#     while True:
#         try:
#             num_decimal_places = int(input("输入要计算的π的小数点后位数: "))
#             if num_decimal_places < 1:
#                 print("请输入一个大于等于1的数字。")
#             else:
#                 pi_value = calculate_pi_decimal_places(num_decimal_places)
#                 formatted_pi = f"π的值（小数点后 {num_decimal_places} 位）: \n{pi_value}"
#                 # 将结果每20位添加一个换行符
#                 formatted_pi = '\n'.join([formatted_pi[i:i+20] for i in range(0, len(formatted_pi), 20)])
#                 print(formatted_pi)
#         except ValueError:
#             print("请输入一个有效的整数。")
#
#
#
#
# import pygame
# import random
#
# # 游戏参数
# WIDTH, HEIGHT = 300, 600
# GRID_SIZE = 30
# GRID_WIDTH = WIDTH // GRID_SIZE
# GRID_HEIGHT = HEIGHT // GRID_SIZE
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
# # 俄罗斯方块的形状和颜色
# SHAPES = [
#     [[1, 1, 1, 1]],            # I 形
#     [[1, 1], [1, 1]],          # O 形
#     [[1, 1, 1], [0, 1, 0]],    # T 形
#     [[1, 1, 1], [1, 0, 0]],    # L 形
#     [[1, 1, 1], [0, 0, 1]],    # J 形
#     [[1, 1, 0], [0, 1, 1]],    # S 形
#     [[0, 1, 1], [1, 1, 0]]     # Z 形
# ]
# SHAPES_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
#                  (255, 0, 255), (0, 255, 255), (128, 128, 128)]  # 形状对应的颜色
#
# # 初始化 Pygame
# pygame.init()
#
# # 创建游戏窗口
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('俄罗斯方块')
#
# # 创建网格
# grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
#
# # 初始化游戏状态
# current_shape = None
# current_shape_color = None
# current_x = 0
# current_y = 0
# score = 0
# game_over = False
#
# # 生成新的俄罗斯方块
# def new_shape():
#     global current_shape, current_shape_color, current_x, current_y
#     current_shape = random.choice(SHAPES)
#     current_shape_color = random.choice(SHAPES_COLORS)
#     current_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
#     current_y = 0
#
# # 检查是否可以移动俄罗斯方块
# def can_move(x, y):
#     for row in range(len(current_shape)):
#         for col in range(len(current_shape[0])):
#             if current_shape[row][col] == 1:
#                 if (x + col < 0 or x + col >= GRID_WIDTH or
#                     y + row >= GRID_HEIGHT or
#                     grid[y + row][x + col] != 0):
#                     return False
#     return True
#
# # 将俄罗斯方块固定在底部并检查是否有完整的行
# def place_shape():
#     global score
#     for row in range(len(current_shape)):
#         for col in range(len(current_shape[0])):
#             if current_shape[row][col] == 1:
#                 grid[current_y + row][current_x + col] = current_shape_color
#     # 检查是否有完整的行
#     complete_rows = []
#     for row in range(GRID_HEIGHT):
#         if all(grid[row]):
#             complete_rows.append(row)
#     # 删除完整的行并在顶部添加新行
#     for row in complete_rows:
#         del grid[row]
#         grid.insert(0, [0] * GRID_WIDTH)
#         score += 100 * len(complete_rows)
#
# # 游戏主循环
# clock = pygame.time.Clock()
# new_shape()
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT and can_move(current_x - 1, current_y):
#                 current_x -= 1
#             elif event.key == pygame.K_RIGHT and can_move(current_x + 1, current_y):
#                 current_x += 1
#             elif event.key == pygame.K_DOWN and can_move(current_x, current_y + 1):
#                 current_y += 1
#
#     # 自动下落俄罗斯方块
#     if can_move(current_x, current_y + 1):
#         current_y += 1
#     else:
#         place_shape()
#         new_shape()
#
#     # 渲染游戏界面
#     screen.fill(BLACK)
#     for row in range(GRID_HEIGHT):
#         for col in range(GRID_WIDTH):
#             color = grid[row][col]
#             if color != 0:
#                 pygame.draw.rect(screen, color,
#                                  pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
#     for row in range(len(current_shape)):
#         for col in range(len(current_shape[0])):
#             if current_shape[row][col] == 1:
#                 pygame.draw.rect(screen, current_shape_color,
#                                  pygame.Rect((current_x + col) * GRID_SIZE, (current_y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 2)
#     pygame.display.flip()
#
#     # 游戏结束条件
#     if current_y == 0:
#         game_over = True
#
#     clock.tick(5)  # 控制游戏速度
#
# # 游戏结束时显示分数
# font = pygame.font.Font(None, 36)
# game_over_text = font.render(f'Game Over - Score: {score}', True, WHITE)
# screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
# pygame.display.flip()
#
# # 等待用户关闭窗口
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
