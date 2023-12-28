
import json
import requests
import pandas as pd
import logging
import traceback
logger = logging.getLogger('dev_log')

def scheduled_job():
    try:
        url="https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"

        data=requests.get(url=url)

        data=data.json()
        df = pd.DataFrame(data)
        tokens=df.set_index('symbol')['token'].to_dict()

        json_file_path = 'PROJECT50/datamanagement/token.json'

        # Write the dictionary to a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(tokens, json_file)

        logger.info("TOKEN FILE UPDATED SUCCESSFULLY")

    except Exception:
        logger.error(str(traceback.format_exc()))
        