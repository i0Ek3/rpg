from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


# 常量定义
SPEC_STR = "!@#$%&*"
CHOICE_MIX = string.ascii_letters + string.digits
CHOICE_DIG = string.digits
CHOICE_LET = string.ascii_letters
RANDOM_INT = random.randint(10, 12)
HTML_TEMPLATE = "index.html"


# 生成指定长度的由字母+数字+特殊字符组成的密码
def genpwd(length):
    # 确保密码不以特殊字符开头
    password = random.choice(CHOICE_MIX)

    characters = CHOICE_MIX + SPEC_STR
    password += "".join(
        random.choice(characters) for _ in range(length - 2)
    )

    # 确保密码不以特殊字符结尾
    password += random.choice(CHOICE_MIX)

    return insert_special_character(password, SPEC_STR)


# 如果生成的密码中不存在特殊字符，则随机插入一个特殊字符到密码中
def insert_special_character(ori_str, special_characters):
    has_special_character = False

    for char in special_characters:
        if char in ori_str:
            has_special_character = True
            break

    if not has_special_character:
        # 随机选择插入位置
        index = random.randint(1, len(ori_str) - 1)
        previous_char = ori_str[index - 1]
        next_char = ori_str[index]

        while previous_char in special_characters or next_char in special_characters:
            index = random.randint(1, len(ori_str) - 1)
            previous_char = ori_str[index - 1]
            next_char = ori_str[index]

        char_to_insert = random.choice(special_characters)
        ori_str = ori_str[:index] + char_to_insert + ori_str[index:]

    # 删除多余的特殊字符
    indices = [i for i in range(1, len(ori_str) - 1) if ori_str[i] in special_characters]
    if len(indices) > 1:
        index_to_remove = random.choice(indices[:-1])
        ori_str = ori_str[:index_to_remove] + ori_str[index_to_remove + 1:]

    return ori_str


# 移除末尾的连接符-
def remove_trailing_hyphen(password):
    last = password[-1]
    if last == "-":
        return password[:-1]
    else:
        return password


# 根据 choice 生成指定长度的密码
def genpwd_by(choice):
    password = ""
    for _ in range(3):
        segment = "".join(
            random.choice(choice) for _ in range(4)
        )

        password += segment

    return remove_trailing_hyphen(password)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pwda = genpwd(RANDOM_INT)
        pwdb = genpwd_by(CHOICE_MIX)
        pwdc = genpwd_by(CHOICE_DIG)
        pwdd = genpwd_by(CHOICE_LET)

        # 返回列表，模板引擎可以直接遍历
        return render_template(HTML_TEMPLATE, password_list = [pwda, pwdb, pwdc, pwdd])

    return render_template(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run()
