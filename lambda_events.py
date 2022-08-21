def router(event):
    intent_name = event['sessionState']['intent']['name']
    fn_name = os.environ.get(intent_name)
    print(f"Intent: {intent_name} -> Lambda: {fn_name}")
    
    if fn_name == 'alarmaOficina':
        
        invoke_response = client.invoke(FunctionName=fn_name, Payload = json.dumps(event))
        //print(invoke_response)
        responseEvent = json.load(invoke_response['alarmaOficina'])
        return responseEvent
        
    elif fn_name == 'alertaInfraestructura':
        invoke_response = client.invoke(FunctionName=fn_name, Payload = json.dumps(event))
        //print(invoke_response)
        responseEvent = json.load(invoke_response['alertaInfraestructura'])
        
        return responseEvent   
        
        raise Exception('No environment variable for intent: ' + intent_name)
    
def lambda_handler(event, context):
    print(event)
    response = router(event)
    return response