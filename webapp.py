from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app= Flask(__name__)
Bootstrap(app)

@app.route("/myapp")

def index():
    products = product_list()
    return render_template('index.html', products=products)


# some logic for this list

def product_list():
    product1={
        'product_name':'wireless headphones',
        'price':'$20',
        'stock':10,
        'buy_now':"http://www.google.com"
    }
    product2={
        'product_name':'laptop',
        'price':'$800',
        'stock':10,
        'buy_now':"http://www.google.com"
    }
    product3={
        'product_name':'mobile phone',
        'price':'$200',
        'stock':10,
        'buy_now':"http://www.google.com"
    }
    product4={
        'product_name':'Mouse and Keyboard',
        'price':'$100',
        'stock':8,
        'buy_now':"http://www.google.com"
    }
    return [product1, product2, product3,product4]

if __name__ =='__main__':
    app.run(port=5000,debug=True)