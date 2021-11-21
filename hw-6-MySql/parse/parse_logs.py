import re
import os

log_pattern = re.compile(r'(?P<ip>\d+.\d+.\d+.\d+) - - \[.+] \"(?P<req>.+) (?P<url>.+) HTTP/1\.\d" (?P<code>\d+) (?P<value>\d*)')


def return_count_requests(path):
    size = 0
    with open(path) as f:
        for line in f:
            size += 1
    return size


def count_requests_with_type(path):
    req_type = []
    with open(path) as f:
        for line in f:
            result = log_pattern.search(line)
            if result:
                req_type.append(result.group("req")) # result.group(0)
    req_type = [(x, req_type.count(x)) for x in set(req_type)]
    return req_type


def get_url(path):
    urls = []
    with open(path) as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer:
                urls += [answer.group("url")]
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])
    return urls[-10:]


def get_requests_with_400_status_code(path):
    urls = []
    with open(path) as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer and re.match(r"4\d{2}", answer.group("code")):
                urls.append((answer.group("url"), answer.group("code"), int(answer.group("value")), answer.group("ip")))
    urls = sorted(urls, key=lambda x: x[2])
    return urls[-5:]


def get_requests_with_500_status_code(path):
    urls = []
    with open(path) as file:
        for line in file:
            answer = log_pattern.search(line)
            if answer and re.match(r"5\d{2}", answer.group("code")):
                urls.append(answer.group("ip"))
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])
    return urls[-5:]


