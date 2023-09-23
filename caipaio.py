import random
import datetime

def print_message(message):
    print(message)
    return

def generate_random_ticket():
    red_numbers = random.sample(range(1, 34), 6)
    blue_number = random.randint(1, 16)
    return red_numbers, blue_number

def display_ticket_info(ticket_id, ticket_type, numbers):
    print("======彩===票===信===息=====")
    print(f"投注时间：{datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")
    print(f"开奖期数：{current_draw}")
    print(f"彩票id：{ticket_id}")
    print(f"投注方式：{ticket_type}")
    print("投注号码：")
    for number in numbers:
        print(number)
    print("======彩===票===信===息=====")

def check_winning(ticket, winning_numbers):
    user_numbers, user_blue_number = ticket
    winning_red_numbers, winning_blue_number = winning_numbers
    red_matches = len(set(user_numbers).intersection(winning_red_numbers))
    blue_match = (user_blue_number == winning_blue_number)
    
    if red_matches == 6 and blue_match:
        return "一等奖"
    elif red_matches == 6:
        return "二等奖"
    elif red_matches == 5 and blue_match:
        return "三等奖"
    elif red_matches == 5 or (red_matches == 4 and blue_match):
        return "四等奖"
    elif red_matches == 4 or (red_matches == 3 and blue_match):
        return "五等奖"
    else:
        return "未中奖"

print_message("===========双色球彩票模拟===========")

# 存储彩票ID和对应信息的字典
ticket_data = {}
# 当前开奖期数
current_draw = 1
# 是否已经开奖的标志
is_drawn = False

while True:
    user_choice = input("1-彩票投注\n2-彩票开奖\n3-中奖查询\n0-退出\n请输入序号:")

    if user_choice == "1":
        while True:
            ticket_type_choice = input("===接下来您可以购买1张彩票===\n1-机选投注\n2-单式投注\n3-复式投注\n4-胆拖投注\n请输入序号:")
            
            if ticket_type_choice == "1":
                num_tickets = int(input("请输入机选投注的注数:"))
                if num_tickets >= 0:
                    for _ in range(num_tickets):
                        red_numbers, blue_number = generate_random_ticket()
                        ticket_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
                        ticket_data[ticket_id] = ("机选", (red_numbers, blue_number))
                        display_ticket_info(ticket_id, "机选", (red_numbers, blue_number))
                    
                    continue_choice = input("是否继续自选投注(y/n): ")
                    if continue_choice.lower() != "y":
                        break
                else:
                    print_message("机选投注的注数有误")
            
            elif ticket_type_choice == "2":
                # 单式投注的逻辑
                while True:
                    user_input = input("请依次输入6个红色球和1个蓝色球号码（以空格隔开）:")
                    user_numbers = tuple(map(int, user_input.split()))
                    if len(user_numbers) == 7:
                        ticket_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
                        ticket_data[ticket_id] = ("单式", user_numbers)
                        display_ticket_info(ticket_id, "单式", user_numbers)
                        
                        continue_choice = input("是否继续自选投注(y/n): ")
                        if continue_choice.lower() != "y":
                            break
                    else:
                        print_message("输入号码数量有误")
                        break

            elif ticket_type_choice == "3":
                # 实现复式投注的逻辑
                red_numbers = []
                blue_numbers = []

                while True:
                    red_input = input("请输入6-20个红色球号码（以空格隔开）:")
                    red_user_numbers = list(map(int, red_input.split()))
                    if 6 <= len(red_user_numbers) <= 20:
                        red_numbers = red_user_numbers
                        break
                    else:
                        print_message("红球号码数量不符合要求，请重新输入")

                while True:
                    blue_input = input("请输入至少1个蓝色球号码（以空格隔开）:")
                    blue_user_numbers = list(map(int, blue_input.split()))
                    if len(blue_user_numbers) >= 1:
                        blue_numbers = blue_user_numbers
                        break
                    else:
                        print_message("蓝球号码数量不符合要求，请重新输入")

                ticket_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
                ticket_data[ticket_id] = ("复式", (red_numbers, blue_numbers))
                display_ticket_info(ticket_id, "复式", (red_numbers, blue_numbers))

                continue_choice = input("是否继续复式投注(y/n): ")
                if continue_choice.lower() != "y":
                    break

            elif ticket_type_choice == "4":
                # 实现胆拖投注的逻辑
                while True:
                    red_balls_dan = []
                    red_balls_tuo = []
                    blue_balls = []

                    while True:
                        red_input_dan = input("请输入1-5个红色球胆码（以空格隔开）:")
                        red_numbers_dan = list(map(int, red_input_dan.split()))
                        if 1 <= len(red_numbers_dan) <= 5:
                            red_balls_dan = red_numbers_dan
                            break
                        else:
                            print_message("红球胆码数量不符合要求，请重新输入")

                    while True:
                        red_input_tuo = input("请输入1-16个红色球拖码（以空格隔开）:")
                        red_numbers_tuo = list(map(int, red_input_tuo.split()))
                        if 1 <= len(red_numbers_tuo) <= 16:
                            red_balls_tuo = red_numbers_tuo
                            break
                        else:
                            print_message("红球拖码数量不符合要求，请重新输入")

                    red_balls = red_balls_dan + red_balls_tuo

                    while True:
                        blue_input = input("请输入至少1个蓝色球号码（以空格隔开）:")
                        blue_user_numbers = list(map(int, blue_input.split()))
                        if len(blue_user_numbers) >= 1:
                            blue_balls = blue_user_numbers
                            break
                        else:
                            print_message("蓝球号码数量不符合要求，请重新输入")
                    
                    if len(red_balls) + len(blue_balls) < 7:
                        print_message("胆码和拖码之和必须大于等于7个号码！！")
                    else:
                        ticket_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
                        ticket_data[ticket_id] = ("胆拖", (red_balls, blue_balls))
                        display_ticket_info(ticket_id, "胆拖", (red_balls, blue_balls))

                        continue_choice = input("是否继续胆拖投注(y/n): ")
                        if continue_choice.lower() != "y":
                            break

            else:
                print_message("无效的选项，请重新选择")

    elif user_choice == "2":
        if not is_drawn:
            print("=======正在开奖=======")
            print(f"开奖期数：{current_draw}")
            print(f"开奖时间：{datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")
            winning_red_balls = random.sample(range(1, 34), 6)
            winning_blue_ball = random.randint(1, 16)
            print("红色球号码:", "    ".join(map(str, winning_red_balls)))
            print(f"蓝色球号码：{winning_blue_ball}")
            is_drawn = True
            current_draw += 1
        else:
            print("本期已经开奖，无需重复开奖")

    elif user_choice == "3":
        while True:
            ticket_id = input("请输入一个12位的彩票id:")
            if ticket_id in ticket_data:
                if is_drawn:
                    ticket_type, numbers = ticket_data[ticket_id]
                    winning_numbers = (winning_red_balls, winning_blue_ball)
                    result = check_winning(numbers, winning_numbers)
                    if result == "未中奖":
                        print("遗憾，您的彩票未中奖！！！")
                    else:
                        print(f"恭喜你中奖了，中奖等级：{result}")
                else:
                    print("此彩票尚未开奖，请进行开奖！！！")
                    break
            else:
                print("输入的彩票id不存在！")

            continue_choice = input("是否继续查询彩票中奖？(y/n): ")
            if continue_choice.lower() != "y":
                break

    elif user_choice == "0":
        print_message("再见了，祝你好运！！！")
        print_message("===========按任意键退出===========")
        break

    else:
        print_message("无效的选项，请重新选择")
