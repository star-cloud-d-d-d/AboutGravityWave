from flask import Flask, render_template

app = Flask(__name__)

#路由:首頁
@app.route('/')
def home():
    return render_template('index.html')

#路由:補充說明
@app.route('/some')
def about():
    return render_template('some.html')

#路由:參考資料
@app.route('/ref')
def contact():
    return render_template('ref.html')

if __name__ == '__main__':
    app.run(debug=True)
