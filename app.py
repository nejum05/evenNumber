from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/generate">
            Enter a number: <input type="number" name="n">
            <input type="submit" value="Generate">
        </form>
    '''

@app.route('/generate')
def generate():
    try:
        n = int(request.args.get('n'))
        evens = [str(i*2) for i in range(n)]
        return 'Even numbers: ' + ', '.join(evens)
    except:
        return 'Please enter a valid number.'

if __name__ == "__main__":
    app.run()
