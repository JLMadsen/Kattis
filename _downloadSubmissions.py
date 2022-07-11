"""
Small script for fetching all successfull submissions to Kattis

Provide account name (kattis.com/users/<name>) and session cookie
in enviornment variables under kattis-username and kattis-token
"""

import requests, re, os, sys, threading

ACCOUNT_NAME        = os.environ.get('kattis-username')
COOKIE              = {"EduSiteCookie": os.environ.get('kattis-token')}
URL                 = 'https://open.kattis.com'
ID_REGEX            = r'[0-9]{7}'
FETCHED             = set()
PROBLEM_REGEX       = r'/problems/[a-z]+'
PAGE_STOP           = False
CODE_REGEX          = r'data-language="{}">[^<]*</div'

lock_print = threading.Lock()
lock_list = threading.Lock()

languages = { "Python 3": 'py', 
              "C++": 'cpp', 
              "Java": 'java', 
              "C#": 'cs' }

formatting = { '&#039;': '\'', # single quote
               '&quot;': '\"', # double quote
               '&lt;':   '<',  # less than
               '&gt;':   '>',  # greather than
               '&amp;':  '&',  # ampersand
               '\r':     '',   # windows crlf
               '\n\n\n': '\n\n', }

def parse_submission(sub_id) -> None:
    submission = requests.get(f"{URL}/submissions/{sub_id}", cookies=COOKIE).text
    submission = re.sub('Submission history(.|\n)*<\/table>', '', submission)

    if 'status is-status-accepted' not in submission:
        return

    try:
        name = re.findall(PROBLEM_REGEX, submission)[0][10:]
    except:
        return

    for lang, ext in languages.items():
        try:
            code = re.findall(CODE_REGEX.format(lang), submission)[0]
        except:
            continue

        filename = f"{name}.{ext}"

        if filename in FETCHED:
            return
        with lock_list:
            FETCHED.add(filename)
        
        with open(filename, 'w') as f:

            code = (code[17+len(lang):][:-5])
            [code := code.replace(raw, rep) for raw, rep in formatting.items()]

            f.write(code)

            with lock_print:
                print('Saved:', filename, sub_id)
        return

def parse_page(page_nr) -> bool:
    if page_nr > 20: return False
    with lock_print:
        print('Fetch page', page_nr)

    page_url = f"{URL}/users/{ACCOUNT_NAME}?page={page_nr}"
    page = requests.get(page_url, cookies=COOKIE)
    submissions = set(re.findall(ID_REGEX, page.text))

    if not submissions:
        return False

    threads = [threading.Thread(target=parse_submission, args=(sub_id,)) for sub_id in submissions]
    [t.start() for t in threads]
    [t.join() for t in threads]

    return True

def main():
    print('Fetching submissions from', ACCOUNT_NAME)

    counter = 0
    while parse_page(counter):
        counter += 1

if __name__ == '__main__':
    main()