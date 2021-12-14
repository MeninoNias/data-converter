from datetime import date, datetime

file = open('teste.txt', 'r')

file_out = open('date_format.txt', 'w+')

for data in file:
    print('date', data[:10])
    try:
        data = datetime.strptime(data[:10], '%Y-%m-%d').date()
    except ValueError:
        data = datetime.strptime(data[:10], '%d/%m/%Y').date()

    dataFormatada = data.strftime('%d/%m/%Y')
    print(dataFormatada)
    file_out.write("{}\n".format(dataFormatada))

file_out.close()
file.close()