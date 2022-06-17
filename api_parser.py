import requests

X_API_KEY = 'CLOCKIFY_API_KEY'
headers = {'X-Api-Key': X_API_KEY}
workspace_id = '62ac83c82518aa18da253802'
project_id = '62ac86842518aa18da2563fd'


url = 'https://api.clockify.me/api/v1'
PATH = f'/workspaces/{workspace_id}/projects/{project_id}/tasks'


response = requests.get(f'{url}{PATH}', headers={'X-Api-Key': X_API_KEY}).json()


for item in response:
    print('Task: ' + item['name'])
