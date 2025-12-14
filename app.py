from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# 常量定义
SPEC_STR = "!@#$%&*"
CHOICE_MIX = string.ascii_letters + string.digits
CHOICE_DIG = string.digits
CHOICE_LET = string.ascii_letters
HTML_TEMPLATE = "index.html"


# 生成指定长度的由字母+数字+特殊字符组成的密码
def genpwd(length=None):
    if length is None:
        length = random.randint(12, 16)
        
    # 确保首尾不是特殊字符
    # 0 和 -1 位置使用 CHOICE_MIX
    first = random.choice(CHOICE_MIX)
    last = random.choice(CHOICE_MIX)
    
    # 中间部分可以是混合+特殊
    middle_len = length - 2
    chars = CHOICE_MIX + SPEC_STR
    middle = [random.choice(chars) for _ in range(middle_len)]
    
    # 确保至少有2个特殊字符
    current_specials = sum(1 for char in middle if char in SPEC_STR)
    while current_specials < 2:
        # 随机选择一个非特殊字符的位置进行替换
        non_spec_indices = [i for i, char in enumerate(middle) if char not in SPEC_STR]
        if not non_spec_indices:
            # 理论上不太可能发生（除非长度极短且全随机为特殊字符）
            break
        
        idx = random.choice(non_spec_indices)
        middle[idx] = random.choice(SPEC_STR)
        current_specials += 1
        
    return first + "".join(middle) + last


# 根据 choice 生成指定长度（12-16）的密码
def genpwd_by(choice, length=None):
    if length is None:
        length = random.randint(12, 16)
    return "".join(random.choice(choice) for _ in range(length))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 每种类型生成5个密码
        pwda_list = [genpwd() for _ in range(5)]
        pwdb_list = [genpwd_by(CHOICE_MIX) for _ in range(5)]
        pwdc_list = [genpwd_by(CHOICE_DIG) for _ in range(5)]
        pwdd_list = [genpwd_by(CHOICE_LET) for _ in range(5)]

        # 构建分组数据（包含类别名称和对应密码列表，更友好）
        password_groups = [
            {"name": "字母+数字+特殊字符", "passwords": pwda_list},
            {"name": "字母+数字", "passwords": pwdb_list},
            {"name": "纯数字", "passwords": pwdc_list},
            {"name": "纯字母", "passwords": pwdd_list},
        ]
        # 传递分组数据给模板（替换原来的password_list）
        return render_template(HTML_TEMPLATE, password_groups=password_groups)

    return render_template(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run()