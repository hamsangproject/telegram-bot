import sqlite3
import json

dict_names = {
    'Sereh': 'سره',
    'Motaradef': 'مترادف',
    'Teyfi': 'طیفی',
    'Farhangestan': 'فرهنگستان',
    'Emlaei': 'املایی',
}

database_filename = 'core/databases/dics.db'
# database_filename = 'databases/dics.db'

def _get_meaning_dict(word: str, database: str):
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()
    table_name = database
    if database == '*':
        tables_list = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

        output = []
        for (table_name) in tables_list:
            table_name = table_name[0]
            query_text = f'SELECT * FROM {table_name} WHERE word IS \'{word}\';'
            query_result = connection.execute(query_text)
            table_output = []
            for result in query_result:
                result_dict = {'id': result[0],
                            'word': result[1],
                            'definition': result[2],
                            'context': result[3],
                            }
                table_output.append(result_dict)
                output.append({
                    'table_name': table_name,
                    'dict_name': dict_names[table_name],
                    'result': table_output
                })

    else:
        query_text = f'SELECT * FROM {table_name} WHERE word IS \'{word}\';'
        query_result = connection.execute(query_text)
        output = []
        for result in query_result:
            result_dict = {'id': result[0],
                        'word': result[1],
                        'definition': result[2],
                        'context': result[3],
                        }
            output.append({'table_name':table_name, 'result':result_dict})
    
    return output


def get_meaning(word: str, database: str='*', json_out: bool = False):
    if json_out == True:
        return json.dumps(_get_meaning_dict(word, database), ensure_ascii=False, indent=1)
    else:
        return _get_meaning_dict(word, database)
