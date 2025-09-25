class Moto:

    def set_valor (self,valor):
        self.valor = valor
    def set_marca (self, marca):
        self.marca = marca
    def set_modelo (self, modelo):
        self.modelo = modelo

    def amostragem (self):
         return(f"o modelo {self.modelo} da marca {self.marca} tem um valor de mercado de ate {self.valor}")

moto1 = Moto()

moto1.set_valor(25000)
moto1.set_marca("Yamaha")
moto1.set_modelo("R15")

info=moto1.amostragem()
print(info)