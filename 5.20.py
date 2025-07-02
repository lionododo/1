def check(o):
    if o.upper() == "Y":
        return "达标"
    elif o.upper() == "N":
        return "不达标"
    else:
        return "输入错误"

asport = []
astudy = []
cishu1 = 0
cishu2 = 0

# 用户输入
for i in range(4):
    sport = input(f"第{i+1}天运动情况（Y/N）：")
    study = input(f"第{i+1}天学习情况（Y/N）：")
    asport.append(sport)
    astudy.append(study)

# 保存过程和结果到文件
with open("打卡记录.txt", "w", encoding="utf-8") as f:
    for i in range(4):
        resport = check(asport[i])
        restudy = check(astudy[i])

        f.write(f"第{i+1}天的运动情况：{resport}\n")
        f.write(f"第{i+1}天的学习情况：{restudy}\n")

        if resport == "达标":
            cishu1 += 1
        if restudy == "达标":
            cishu2 += 1

    # 写入统计结果
    f.write(f"\n总运动达标天数：{cishu1}\n")
    f.write(f"总学习达标天数：{cishu2}\n")
    f.write("—— 打卡结束 ——\n")

print("打卡完成，记录已保存到【打卡记录.txt】")
