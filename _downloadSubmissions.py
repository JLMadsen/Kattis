"""
Small script for fetching last successfull of all submissions to Kattis

Provide account name (kattis.com/users/<name>) and session cookie
Either change variables or call script with vars: python main.py <account_name> <cookie>

Code formatting in terms of newlines may differ from submission

Only works with python 3 scripts currently
"""

import requests
import re
import sys
import os

ACCOUNT_NAME        = os.environ.get('kattis-username')
COOKIE              = {"EduSiteCookie": os.environ.get('kattis-token')}

URL                 = 'https://open.kattis.com'
ID_REGEX            = r'[0-9]{7}'
FETCHED             = set()
PYTHON_CODE_REGEX   = r'<div class="source-highlight" data-language="Python 3">[^<]*</div'
CPP_CODE_REGEX      = r'<div class="source-highlight" data-language="C\+\+">[^<]*</div'
JAVA_CODE_REGEX     = r'<div class="source-highlight" data-language="Java">[^<]*</div'
CS_CODE_REGEX       = r'<div class="source-highlight" data-language="C#">[^<]*</div'

CODE = { "Python 3": 'py', "C++": 'cpp', "Java": 'java', "C#": 'cs' }

PROBLEM_REGEX       = r'/problems/[a-z]+'
PAGE_STOP           = False


def parse_page(page_nr) -> bool:
    print('Fetch page', page_nr)
    page_url = URL + '/users/' + ACCOUNT_NAME + '?page=' + str(page_nr)
    page = requests.get(page_url, cookies=COOKIE)
    submissions = re.findall(ID_REGEX, page.text)
    
    for n in ['1641570', '7900000', '6651308', '1287607', '0744694', 
              '2943484', '5615381', '7812191', '2125286', '7900000', 
              '6964286', '4662756', '3682872', '3835793', '1733243', 
              '2397923', '3932722']:
        try:
            submissions.remove(n)
        except:
            pass

    if not len(submissions):
        return False

    for id in submissions:
        if id in FETCHED:
            continue

        submission_url = URL + '/submissions/' + id
        submission = requests.get(submission_url, cookies=COOKIE)
        submission = submission.text

        if '<span class="accepted">' not in submission:
            continue

        try:
            name = re.findall(PROBLEM_REGEX, submission)[0][10:]
        except:
            continue

        try:
            code = re.findall(PYTHON_CODE_REGEX, submission)[0]
        except:
            continue

        with open(name + '.py', 'w') as f:

            code = (code
                [len('<div class="source-highlight" data-language="Python 3">'):]
                [:-len('</div')]
                .replace('&#039;', '\'') # fix html encoding
                .replace('&quot;', '\"')
                .replace('&lt;', '<') # less than
                .replace('&gt;', '>') # greather than
                .replace('&amp;', '&') # ampersand
                .replace('\r', '') # fix windows crlf
                .replace('\n\n', '\n'))

            f.write(code)

        FETCHED.add(id)
        print('save', name, id)

    return True

def main():
    global ACCOUNT_NAME
    global COOKIE

    if len(sys.argv) > 1:
        ACCOUNT_NAME = sys.argv[1]
        COOKIE = {"EduSiteCookie": sys.argv[2]}

    print(sys.argv)

    print('Fetching submissions by', ACCOUNT_NAME)

    counter = 0
    while 1:
        if not parse_page(counter):
            print('break at page', counter)
            break

        counter += 1

if __name__ == '__main__':
    main()