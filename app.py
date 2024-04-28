from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# 生成10-12位字母+数字+特殊字符
def genpwd(length):
    characters = string.ascii_letters + string.digits + "!@#$%&*-"
    password = random.choice(
        string.ascii_letters + string.digits
    )  # 确保密码不以特殊字符开头
    password += "".join(random.choice(characters) for _ in range(length - 2))
    password += random.choice(
        string.ascii_letters + string.digits
    )  # 确保密码不以特殊字符结尾
    return password

# 生成10-12位字母+数字
def genpwd2():
    password = ""
    for _ in range(3):
        segment = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(4)
        )
        password += segment + "-"
    password = password[:-1]  # 移除末尾的连接符-
    return password

# 生成10-12位纯数字
def genpwd3():
    password = ""
    for _ in range(3):
        segment = "".join(
            random.choice(string.digits) for _ in range(4)
        )
        password += segment
    password = password[:-1]  # 移除末尾的连接符-
    return password

# 生成10-12位纯字母
def genpwd4():
    password = ""
    for _ in range(3):
        segment = "".join(
            random.choice(string.ascii_letters) for _ in range(4)
        )
        password += segment
    password = password[:-1]  # 移除末尾的连接符-
    return password


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pwda = genpwd2()
        pwdb = genpwd(random.randint(10, 12))
        pwdc = genpwd3()
        pwdd = genpwd4()
        return render_template("index.html", 
                               password=pwda, 
                               password2=pwdb, 
                               password3=pwdc,
                               password4=pwdd)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
