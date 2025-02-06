from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# 常量定义
SPEC_STR = "!@#$%&*"
CHOICE_MIX = string.ascii_letters + string.digits
CHOICE_DIG = string.digits
CHOICE_LET = string.ascii_letters
RANDOM_INT = random.randint(12, 16)
HTML_TEMPLATE = "index.html"


# 生成指定长度的由字母+数字+特殊字符组成的密码
def genpwd(length):
    # 初始化密码
    password = ""
    characters = CHOICE_MIX + SPEC_STR
    while len(password) < length:
        if len(password) == 0 or len(password) == length - 1:
            # 确保密码不以特殊字符开头和结尾
            char = random.choice(CHOICE_MIX)
        else:
            char = random.choice(characters)
        password += char

    # 确保至少有2个特殊字符
    special_count = sum(1 for char in password if char in SPEC_STR)
    while special_count < 2:
        # 随机选择一个非开头和结尾的位置
        index = random.randint(1, length - 2)
        previous_char = password[index - 1]
        next_char = password[index + 1] if index < length - 2 else None
        while previous_char in SPEC_STR or (next_char and next_char in SPEC_STR):
            index = random.randint(1, length - 2)
            previous_char = password[index - 1]
            next_char = password[index + 1] if index < length - 2 else None

        # 移除原位置字符并插入特殊字符
        password = password[:index] + random.choice(SPEC_STR) + password[index + 1:]
        special_count = sum(1 for char in password if char in SPEC_STR)

    return password


# 根据 choice 生成指定长度（12-16）的密码
def genpwd_by(choice):
    return "".join(random.choice(choice) for _ in range(RANDOM_INT))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pwda = genpwd(RANDOM_INT)
        pwdb = genpwd_by(CHOICE_MIX)
        pwdc = genpwd_by(CHOICE_DIG)
        pwdd = genpwd_by(CHOICE_LET)

        # 返回列表，模板引擎可以直接遍历
        return render_template(HTML_TEMPLATE, password_list=[pwda, pwdb, pwdc, pwdd])

    return render_template(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run()