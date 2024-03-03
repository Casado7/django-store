class Cart:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        cart=self.session.get("cart")
        if not cart:
            cart=self.session["cart"] ={}
        else: 
            self.cart=cart
    
    def add(self, product):
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id]={
                "product_id":product.id,
                "title": product.title,
                "price": str(product.price),
                "quantity":1,
                #"picture": product.imagen.url,
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.save_cart()

    def save_cart(self):
        self.session["cart"]=self.cart
        self.session.modified=True


    
    def delete(self, product):
        if(str(product.id) in self.cart.keys()):
            del self.cart[str(product.id)]
            self.save_cart()

    def subtract(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"<1]:
                    self.eliminar(product)
                break
        self.save_cart()

    def clear_cart(self):
        cart=self.session["cart"] ={}
        self.session.modified=True

