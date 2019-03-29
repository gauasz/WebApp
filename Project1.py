from flask import Flask, render_template

app = Flask(__name__)





@app.route('/')
def home():
    return render_template('home.html')

# Do zrobienia:
@app.route('/poll')
def poll():
    return render_template('poll.html')

@app.route('/thx/<user>') #Panel z podziękowaniem w stylu "Dzięki za wypełnienie ankiety, Ania/Ola/Paweł itp
def form(user):
    return render_template('thx.html', user=user)

#do zrobienia
@app.route('/dane')   #<- widok z którego można się wybrać do surowych lub obrobionych danych
def dane():
    return render_template('dane.html')

#do zrobienia
@app.route('/raw')
def raw():
    return render_template('raw.html')

#do zrobienia
@app.route('/processed')
def processed():
    return render_template('processed.html')


if __name__ == "__main__":
    app.run()