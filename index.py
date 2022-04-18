import json

print("Loading function")


def lambda_handler(event, context):
    transactionType = event['type']
    transactionAmount = event['amount']

    print(f"transactioType - {transactionType}")
    print(f"transactioAmount - {transactionAmount}")

    transactionResponse = {}
    transactionResponse['transactionType'] = transactionType
    transactionResponse['transactionAmount'] = transactionAmount
    transactionResponse['message'] = "Transaction Process"

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['header'] = {}
    responseObject['header']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject
