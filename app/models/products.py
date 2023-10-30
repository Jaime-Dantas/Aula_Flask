from app import db
class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement':True}
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    data_despesa = db.Column(db.String(255))
    valor = db.Column(db.Float)
    meto_pagamento = db.Column(db.String(255))
    descricao = db.Column(db.String(255))
    status_despesa = db.Column(db.String(255))

    def __init__(self,name,price,data_despesa,valor,meto_pagamento,descricao,status_despesa ):
        self.name = name
        self.price = price
        self.data_despesa = data_despesa
        self.valor = valor
        self.meto_pagamento = meto_pagamento
        self.descricao = descricao
        self.status_despesa = status_despesa

    
    def json(self):
        return {
            'name': self.name,
            'price': self.price,
            'data_despesa':self.data_despesa,
            'valor':self.valor,
            'meto_pagamento':self.meto_pagamento,
            'descricao':self.descricao,
            'status_despesa':self.status_despesa
        }
     
    def save_products(self, name, price,data_despesa,valor,meto_pagamento,descricao,status_despesa): #salvar a instancia no banco de dados
        try:
            add_banco = Products(name, price,data_despesa,valor,meto_pagamento,descricao,status_despesa)
            db.session.add(add_banco) #adicionar a instância
            db.session.commit() #confirma
        except Exception as e: #se a -operação de salvar falhas, cai na exceção
            print(e)