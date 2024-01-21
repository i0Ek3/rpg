from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def genpwd(length):
    characters = string.ascii_letters + string.digits + '!@#$%&*-'
    password = random.choice(string.ascii_letters + string.digits) # 确保密码不以特殊字符开头
    password += ''.join(random.choice(characters) for _ in range(length - 2))
    password += random.choice(string.ascii_letters + string.digits) # 确保密码不以特殊字符结尾
    return password

def genpwd2():
    password = ''
    for _ in range(3):
        segment = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
        password += segment + '-'
    password = password[:-1]  # 移除末尾的连接符-
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pwda, pwdb = genpwd2(), genpwd(random.randint(8, 12))
        return render_template('index.html', password=pwda, password2=pwdb)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()