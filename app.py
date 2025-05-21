from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate')
def generate():
    try:
        n = int(request.args.get('n'))
        evens = [str(i * 2) for i in range(n)]
        return render_template('result.html', evens=evens)
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
