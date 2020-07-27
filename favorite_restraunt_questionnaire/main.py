import csv
import operator
import os
from termcolor import colored

print(colored('==================================================\n' \
      'こんにちは！私はRobokoです。あなたの名前は何ですか？\n' \
      'Hello, I am Roboko. What is your name?\n' \
      '==================================================', 'red'))

person_name = input()

csv_name = 'ranking.csv'
if(os.path.exists(csv_name)):
    with open(csv_name, 'r', newline='', encoding='shift_jis') as r_csv_file:

        csv_reader = csv.reader(r_csv_file)

        header = next(csv_reader)
        rows = [[row[0], row[1]] for row in csv_reader]
        sort_datas = sorted(rows, key=operator.itemgetter(1), reverse=True)

        for row in sort_datas:
            print(colored('==================================================\n' +
                          '私のオススメのレストランは、' + row[0] + 'です。\n' +
                          'I recommend ' + row[0] + '.\n\n' +
                          'このレストランは好きですか？ [Yes/No]\n' +
                          'Do you like it? [y/n]\n'
                          '==================================================', 'red'))

            is_favorite_restaurant = input().lower()

            if is_favorite_restaurant == 'yes' or is_favorite_restaurant == 'y':
                with open(csv_name, 'a') as w_csv_file:
                    fieldnames = ['Name', 'Count']
                    w_csv_datas = csv.DictWriter(w_csv_file, fieldnames=fieldnames)
                    w_csv_datas.writerow({'Name': row[0], 'Count': int(row[1]) + 1})
            elif is_favorite_restaurant == 'no' or is_favorite_restaurant == 'n':
                pass
            else:
                print(colored('==================================================\n' +
                              'YesかNoで答えて下さい。\n' +
                              'Anser Yes or No.'
                              '==================================================', 'red'))

    print(colored('==================================================\n' +
                  person_name + 'さん。どこのレストランが好きですか？\n' +
                  person_name + ', which restaurants do you like?\n' +
                  '==================================================', 'red'))

    favorite_restaurant = input().title()

    with open(csv_name, 'a') as a_csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(a_csv_file, fieldnames=fieldnames)
        writer.writerow({'Name': favorite_restaurant, 'Count': 1})

else:
    print(colored('==================================================\n' +
           person_name + 'さん。どこのレストランが好きですか？\n' +
           person_name + ', which restaurants do you like?\n' +
           '==================================================', 'red'))
    
    favorite_restaurant = input().title()
    
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    
        count = 0
        with open('ranking.csv', 'r') as r_csv_file:
              reader = csv.DictReader(r_csv_file)
              for row in reader:
                    if row['Name'] == favorite_restaurant:
                          count = row['Count']
        count += 1
    
        writer.writerow({'Name': favorite_restaurant, 'Count': count})
    
print(colored('==================================================\n' +
       'Roboko: ' + person_name + 'さん。ありがとうございました。\n' +
       'Roboko: Thank you so much, ' + person_name + '!\n\n' +
       '良い一日を！さようなら。\n' +
       'Have a good day!\n' +
       '==================================================', 'red'))