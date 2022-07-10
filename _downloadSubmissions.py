"""
Small script for fetching all successfull submissions to Kattis

Provide account name (kattis.com/users/<name>) and session cookie
Either change variables or call script with vars: python main.py <account_name> <cookie>
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
PROBLEM_REGEX       = r'/problems/[a-z]+'
PAGE_STOP           = False
CODE_REGEX          = r'<div class="source-highlight" data-language="{}">[^<]*</div'

languages = { "Python 3": 'py', 
              "C++": 'cpp', 
              "Java": 'java', 
              "C#": 'cs' }

def parse_page(page_nr) -> bool:
    print('Fetch page', page_nr)
    page_url = URL + '/users/' + ACCOUNT_NAME + '?page=' + str(page_nr)
    page = requests.get(page_url, cookies=COOKIE)
    submissions = set(re.findall(ID_REGEX, page.text))
    
    if not submissions:
        return False

    for id in submissions:
        if id in FETCHED:
            continue

        submission = requests.get(URL + '/submissions/' + id, cookies=COOKIE).text
        submission = re.sub('Submission history(.|\n)*<\/table>', '', submission)

        if 'status is-status-accepted' not in submission:
            continue

        for lang, ext in languages.items():
            try:
                name = re.findall(PROBLEM_REGEX, submission)[0][10:]
            except:
                break

            try:
                code = re.findall(CODE_REGEX.format(lang), submission)[0]
            except:
                continue

            with open(name + '.' + ext, 'w') as f:

                code = (code
                    [len('<div class="source-highlight" data-language="'+ lang +'">'):]
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
            break

    return True

def main():
    print('Fetching submissions from', ACCOUNT_NAME)

    counter = 0
    while parse_page(counter):
        counter += 1

if __name__ == '__main__':
    main()