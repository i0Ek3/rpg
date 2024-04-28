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


# 根据 choice 生成 10-12 位密码
def genpwd_by(choice):
    password = ""
    for _ in range(3):
        segment = "".join(
            random.choice(choice) for _ in range(4)
        )
        password += segment + "-"
    
    password = password[:-1]  # 移除末尾的连接符-
    
    return password


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pwda = genpwd(random.randint(10, 12))
        pwdb = genpwd_by(string.ascii_letters + string.digits)
        pwdc = genpwd_by(string.digits)
        pwdd = genpwd_by(string.ascii_letters)
        
        return render_template("index.html", 
                               password=pwda, 
                               password2=pwdb, 
                               password3=pwdc,
                               password4=pwdd)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
