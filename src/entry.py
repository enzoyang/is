#coding:UTF-8
import web

urls=()

app = web.application(urls,globals())

if __name__ == '__main__':
    app.run()