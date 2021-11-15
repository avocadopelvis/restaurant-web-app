from restaurant.routes import app

#checks if main.py has executed directly and not imported
if __name__ == '__main__':
    app.run(debug = True)



