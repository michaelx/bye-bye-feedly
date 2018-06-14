import io
import json
import requests
import time


# Add your feedly API credentials
user_id = ''
access_token = ''


def get_saved_items(user_id, access_token):
    headers = {'Authorization' : 'OAuth ' + access_token}
    url = 'https://cloud.feedly.com/v3/streams/contents?streamId=user/' + user_id + '/tag/global.saved&count=10000'

    print('Requesting saved items')
    r = requests.get(url, headers = headers)

    if r.status_code == 200:
        filename = 'data.json'
        # For testing feel free to use the below filename instead
        # filename = 'feedly-saved-' + time.strftime("%Y%m%d-%H%M%S") + '.json'
        r.encoding = 'UTF-8'

        # Write compact JSON
        # Replace 'separators' argument with 'indent=4' if you don’t want it minified
        with io.open(filename, 'w', encoding='UTF-8') as output_file:
          try:
            json.dump(r.json(), output_file, separators=(',',':'))
            print('Success: Created ' + filename)
          except ValueError as error:
            print(error)

    else:
        print('Error: Saved items couldn’t be fetched')
        print('Status code: ' + str(r.status_code))
        print(r.json())
        exit(1)


get_saved_items(user_id, access_token)
