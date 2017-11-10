code_of_products1=int(input())
Num_of_products1=int(input())
price_of_products1=float(input())


code_of_products2=int(input())
Num_of_products2=int(input())
price_of_products2=float(input())

paid1=Num_of_products1*price_of_products1
paid2=Num_of_products2*price_of_products2
Valor_a_pagar=paid1+paid2

print("Valor a pagar: R$ %.2f"%Valor_a_pagar)

