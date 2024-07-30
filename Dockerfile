# 使用官方的 Python 镜像作为基础镜像
FROM python:3.12

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到容器的 /app 目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 默认运行的端口
EXPOSE 5000

# 设置环境变量，告诉 Flask 在容器中运行
ENV FLASK_APP=app.py

# 启动 Flask 应用程序
CMD ["flask", "run"]
