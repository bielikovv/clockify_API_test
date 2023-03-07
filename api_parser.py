import requests
import copy
from dateutil.parser import parse
import datetime

X_API_KEY = 'CLOCKIFY_API_KEY'
headers = {'X-Api-Key': X_API_KEY}
workspace_id = '62ac83c82518aa18da253802'
project_id = '62ac86842518aa18da2563fd'
user_id = '62ac83c82518aa18da253801'

url = 'https://api.clockify.me/api/v1'
PATH = f'/workspaces/{workspace_id}/projects/{project_id}/tasks'
PATH_FOR_PROJECT = f'/workspaces/{workspace_id}/user/{user_id}/time-entries'
saeas = 123124

response = requests.get(f'{url}{PATH}', headers={'X-Api-Key': X_API_KEY}).json()
response_with_time = requests.get(f'{url}{PATH_FOR_PROJECT}', headers={'X-Api-Key': X_API_KEY}).json()


def remove_sym(x, val):
    x = copy.deepcopy(item['timeInterval'][val])
    x = x.split('T')
    x[1] = x[1][:-1]
    x = ' '.join(x)
    return x

TOTAL_TIME_FOR_POJECT = 0


for item in response_with_time:
    for el in response:
        if el['id'] == item['taskId']:
            #FOR START TIME
            start = copy.deepcopy(item['timeInterval']['start'])
            start = remove_sym(start, 'start')

            #FOR END TIME
            end = copy.deepcopy(item['timeInterval']['end'])
            end = remove_sym(end, 'end')

            changed_start = start.replace(' ', '/')
            changed_end = end.replace(' ', '/')

            a = parse(changed_start)
            b = parse(changed_end)
            total = (b - a).total_seconds()
            TOTAL_TIME_FOR_POJECT += total
            formated_total = datetime.timedelta(seconds=total)


            print("Task: " + el['name'])
            print("Start: " + start)
            print("End: " + end)
            print(f"Total time for task: {str(formated_total)}")
            print(' ')
            print(' ')

print(f'TOTAL PROJECT TIME: {datetime.timedelta(seconds=TOTAL_TIME_FOR_POJECT)}')


