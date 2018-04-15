import requests
import re
import os
import shutil

websites = {
    'google': 'http://google.com',
    'endouble': 'https://endouble.com'
}

regexes = {
    'regex_name': 'google',
    'script_tag': 'script',
    'body_tag': 'body',
}

results_folder = 'results/'


def main():
    print('Here we go!')

    if os.path.exists(results_folder):
        shutil.rmtree(results_folder)
        os.makedirs(results_folder)

    for name, url in websites.items():

        results_file = open(results_folder + name + '.txt', 'w+')

        webpage = requests.get(url)

        for regex_name, regex in regexes.items():
            hits = re.findall(regex, webpage.content)
            results_file.writelines(regex_name + ' : ' + str(len(hits)) + '\n')

    print('Job\'s done!')


main()
