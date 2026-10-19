# # Project 3: Shop Billing System
# # 1. Show Products
# # 2. Add Product to Bill
# # 3. View Total
# # 4. Apply Discount
# # 5. Exit




print('''
======================================
       || SHOOPING BILL SYSTEM ||
======================================''')


def Bill_system():
    products_price={'Shyampoo':400,
                     'Soap':30,
                     'Oil':100,
                     'Biscuit':50,
                     'ChoCho':20,
                     'DairyMilk':120
                                    } 


    while True:
        product_menu=input('''
                            1. Show Products
                            2. Add Products
                            3. View Total
                            4. Apply Discount
                            5. Exit
                            Enter Your Choice!!: 
                            ''')

        match product_menu:
            case '1':
                for products,price in products_price.items():
                    print(f'Prodects {products} = {price} Rs Price')
                
            case '2':
                products=input('Enter the product Name:')
                if products in products_price:
                    print('Allready added!!')
                else:
                    print('add Your Products!!')
                    price=int(input('Enter your Product Price:Rs '))
                    products_price[products]=price
                    print('Added Successful!!',price)

            case '3':
                for products,price in products_price.items():
                    print(f'{products}:{price}')
        
            case '4':
                   total = 0
                   for products, price in cart.items():
                       print(f'{products}: Rs. {price}')
                       total += price
                       print(f'----------------------------')
                       print(f'Total Amount: Rs. {total}\n')
                
                
            case '5':
                    print('Exit')
                    break
                
            case _:
                  print('invalid Menu!!')
Bill_system()