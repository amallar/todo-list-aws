import json
import logging
import todoList


def create(event, context):
    data = json.loads(event['body'])
    try:
        if 'text' not in data:
            logging.error("Validation failed")
            raise Exception("Couldn't create the todo item.")
        item = todoList.put_item(data['text'])
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }
        return response
    except:
        print("es un error")
