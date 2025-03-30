from flask import Flask, render_template

app = Flask(__name__)

# 路由：首頁
@app.route('/')
def home():
    return render_template('index.html')

# 路由：關於頁面
@app.route('/about')
def about():
    return render_template('about.html')

# 路由：聯繫頁面
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
