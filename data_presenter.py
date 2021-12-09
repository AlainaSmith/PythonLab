invoices = open('CupcakeInvoices.csv')


    # print(data)



# total_strawberry = 0
# total_chocolate = 0
# total_vanilla = 0
# for data in invoices:
#   data = data.split(',')
#   for value in data:
#     if value == 'strawberry':
#       total_strawberry += 1
#     elif value == 'chocolate':
#       total_chocolate += 1
#     elif value == 'vanilla':
#       total_vanilla += 1
# print(total_strawberry, total_chocolate, total_vanilla)




invoices = open('CupcakeInvoices.csv')

for data in invoices:
    values = data.split(',')
    print(values[2])