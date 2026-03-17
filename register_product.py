# 4. Solución Propuesta
# La solución consiste en desarrollar un módulo que permita registrar productos dentro del sistema utilizando estructuras de datos adecuadas.
# Los productos serán representados mediante **tuplas** y almacenados dentro de un **diccionario** para facilitar su acceso.
# Ejemplo de estructura:
# products = {
# product_id: (product_id, product_name, unit_price)
# }

# Esta estructura permite acceder rápidamente a los productos registrados.

def register_product(products):
    id_product = len (products) + 1
    name_product = input ('Enter the name of the product: ')
    price_product = float (input ('Enter the price of the product: '))
    products [id_product] = (id_product, name_product, price_product)
    products.update ({id_product : (name_product, price_product)})
    print (f'Product registered successfully. Total products: {len(products)+1}')
    print (f'Diccionario: {id_product} | Name: {name_product} | Price: {price_product}\n')

o=0
products = {}
while o == 0 :
    register_product(products)
    o= int(input ("You're new register? 0 for yes, 1 for no: "))