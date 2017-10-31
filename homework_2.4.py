import os


def get_files_gener(dir_name, extention):
    return (f_name for f_name in os.listdir(dir_name) if f_name.endswith('.{}'.format(extention)))

def get_appropriate_files(dir, file_list, text):
    new_file_list = []
    for f in file_list:
        with open(os.path.join(dir, f), 'r') as fp:
            for line in fp:
                if text in line:
                    new_file_list.append(f)
                    break
    return new_file_list

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    migrations_dir = os.path.join(current_dir, migrations)
    sql_files = get_files_gener(migrations_dir, 'sql')
    while True:
        text = input('Введите строку: ')
        sql_files = get_appropriate_files(migrations_dir, sql_files, text)
        for f in sql_files:
            print(f)
        print('Всего {}'.format(len(sql_files)))

if __name__ == '__main__':
    main()
