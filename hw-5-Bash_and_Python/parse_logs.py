import re
import sys
import json

log_pattern = re.compile(r'(?P<ip>\d+.\d+.\d+.\d+) - - \[.+] \"(?P<req>.+) (?P<url>.+) HTTP/1\.\d" (?P<code>\d+) (?P<value>\d*)')


# Общее количество запросов
def return_count_requets():
    size = 0
    with open('access.log') as f:
        for line in f:
            size += 1
    return size


# Общее количество запросов по типу, например: GET - 20, POST - 10 и т.д.
def count_requests_with_type():
    req_type = []
    with open('access.log') as f:
        for line in f:
            result = log_pattern.search(line)
            if result:
                req_type.append(result.group("req")) # result.group(0)
    req_type = [(x, req_type.count(x)) for x in set(req_type)]
    return req_type


# Топ 10 самых частых запросов
def get_url():
    urls = []
    with open('access.log') as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer:
                urls += [answer.group("url")]
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])
    return urls[-10:]


# Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
def get_requests_with_400_status_code():
    urls = []
    with open('access.log') as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer and re.match(r"4\d{2}", answer.group("code")):
                urls.append([answer.group("url"), answer.group("code"), int(answer.group("value")), answer.group("ip")])
    urls = sorted(urls, key=lambda x: x[2])
    return urls[-5:]


# Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
def get_requests_with_500_status_code():
    urls = []
    with open('access.log') as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer and re.match(r"5\d{2}", answer.group("code")):
                urls.append(answer.group("ip"))
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])
    return urls[-5:]


data = {
    'count_of_request': return_count_requets(),
    'top_requests': {key[0]: key[1] for key in count_requests_with_type()},
    'frequent_requests': {key[0]: key[1] for key in get_url()},
    'requests_status_code_4XX': [i for i in get_requests_with_400_status_code()],
    'ip_status_code_5XX': {key[0]: key[1] for key in get_requests_with_500_status_code()}
}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--json':
        with open("parsed_log.json", 'w') as file:
            json.dump(data, file, indent=4)
    else:
        # Не хватило времени подумать над дизайном
        with open("parsed_log.txt", 'w') as file:
            file.write(f'Общее количество запросов: \n{data["count_of_request"]}\n\n')
            file.write(f'Общее количество запросов по типу: \n')
            for k, v in data['top_requests'].items():
                file.write(f'{k}: {v}\n')
            file.write(f'\n\nТоп 10 самых частых запросов: \n')
            for k, v in data['frequent_requests'].items():
                file.write(f'{k}: {v}\n')
            file.write(f'\n\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой: \n')
            for i in data['requests_status_code_4XX']:
                file.write(f'{i[0]}: {i[1]}, {i[2]}, {i[3]}\n')
            file.write(f'\n\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой: \n')
            for k, v in data['ip_status_code_5XX'].items():
                file.write(f'{k}: {v}\n')







