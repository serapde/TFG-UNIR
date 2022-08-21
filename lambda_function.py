import json
import random
import decimal 



def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']
    
def get_slot(intent_request, slotName):
    slots = get_slots(intent_request)
    if slots is not None and slotName in slots and slots[slotName] is not None:
        return slots[slotName]['value']['interpretedValue']
    else:
        return None    

def get_session_attributes(intent_request):
    sessionState = intent_request['sessionState']
    if 'sessionAttributes' in sessionState:
        return sessionState['sessionAttributes']

    return {}

def elicit_intent(intent_request, session_attributes, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent'
            },
            'sessionAttributes': session_attributes
        },
        'messages': [ message ] if message != None else None,
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }

def vacaciones(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    desde = get_slot(intent_request, 'desde')
    hasta = get_slot(intent_request, 'hasta')

    text = "Muchas Gracias. Sus vacaciones desde "+desde+" hasta "+hasta+" han sido confirmadas."
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)   

def reservaSala(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    desde = get_slot(intent_request, 'desdeReunion')
    hasta = get_slot(intent_request, 'hastaReunion')
    fechaSala = get_slot(intent_request, 'fechaSala')
    #text = "Su sala ha sido confirmada"
    #text = " desde "+desde+" as "+hasta+"."

    text = "Muchas Gracias. La sala  ha sido reservada "+fechaSala+" desde "+desde+" hasta "+hasta+" han sido confirmada."
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)   
    
def envioDocumentos(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    tipo = get_slot(intent_request, 'tipo')
    ciudad = get_slot(intent_request, 'ciudad')
    direccion = get_slot(intent_request, 'direccion')
    atencion= get_slot(intent_request, 'atencion')


    text = "Su peticion de envio de paquete tipo "+tipo+" a "+ciudad+" en la direccion "+direccion+" a la atención "+atencion+" ha sido procesada. La empresa de transporte se pondrá en contacto con usted"
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message) 
    
def informacionProveedor(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    nombreEmpresa = get_slot(intent_request, 'nombreEmpresa')



    text = " La información sobre "+nombreEmpresa+" es la siguiente ..."
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message) 
    
def localizacionPersonal(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    nombrePersona = get_slot(intent_request, 'nombrePersona')



    text = " La información sobre "+nombrePersona+" es la siguiente ..."
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message) 
    
def obtenerNominas(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    desde = get_slot(intent_request, 'Desde')
    hasta = get_slot(intent_request, 'hasta')



    text = "En el siguiente enlace tiene las nominas desde "+desde+" hasta "+hasta+""
    #text = "Prueba"
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message) 
    

def incidenciaTecnica(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    tipoIncidencia = get_slot(intent_request, 'tipoIncidencia')
    evidencias = get_slot(intent_request, 'evidencias')



    text = "Se ha abierto el siguente caso  "+tipoIncidencia+" en el sistema"
  
    
    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
    
def obtencionCertificado(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    tipoCertificado = get_slot(intent_request, 'tipoCertificado')
    anyo = get_slot(intent_request, 'anyo')


    text = "En el siguiente enlace tiene el certificado "+tipoCertificado+" del "+anyo+""
  

    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
    
def justificacionAusencia(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    fechaAusencia = get_slot(intent_request, 'fechaAusencia')
    desdeAusencia = get_slot(intent_request, 'desdeAusencia')
    hastaAusencia = get_slot(intent_request, 'hastaAusencia')
    motivo = get_slot(intent_request, 'motivo')
    documento = get_slot(intent_request, 'documento')


    text = "El documento de la ausencia "+motivo+"  ha sido dado de alta correctamente"
  

    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)

def justificacionGastos(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)
    fechaAusencia = get_slot(intent_request, 'fechaAusencia')
    desdeGastos = get_slot(intent_request, 'desdeGastos')
    hastaGastos = get_slot(intent_request, 'hastaGastos')
    motivoGastos = get_slot(intent_request, 'motivoGastos')
    ficheroGastos = get_slot(intent_request, 'ficheroGastos')


    text = "El documento de los gastos "+motivoGastos+"  ha sido dado de alta correctamente"
  

    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
    
def confirmacionAlarma(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)



    text = "Confirmación que estamos a la espera de que solucione la alarma"
  

    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
  
def confirmacionAlerta(intent_request):
    session_attributes = get_session_attributes(intent_request)
    slots = get_slots(intent_request)



    text = "Confirmación que estamos a la espera de que solucione la alerta"
  

    message =  {
            'contentType': 'PlainText',
            'content': text
        }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)
    
def dispatch(intent_request):
    intent_name = intent_request['sessionState']['intent']['name']
    response = None
    # Dispatch to your bot's intent handlers
    if intent_name == 'vacaciones':
        return vacaciones(intent_request)
        
    elif intent_name == 'reservaSala':
        return reservaSala(intent_request)
        
    elif intent_name == 'envioDocumentos':
        return envioDocumentos(intent_request)

    elif intent_name == 'informacionProveedor':
        return informacionProveedor(intent_request)

    elif intent_name == 'localizacionPersonal':
        return localizacionPersonal(intent_request)

    elif intent_name == 'obtenerNominas':
        return obtenerNominas(intent_request)
        
    elif intent_name == 'incidenciaTecnica':
        return incidenciaTecnica(intent_request)

    elif intent_name == 'obtencionCertificado':
        return obtencionCertificado(intent_request)
        
    elif intent_name == 'justificacionAusencia':
        return justificacionAusencia(intent_request)
        
    elif intent_name == 'justificacionGastos':
        return justificacionGastos(intent_request)
        
    elif intent_name == 'confirmacionAlarma':
        return confirmacionAlarma(intent_request)
        
    elif intent_name == 'confirmacionAlerta':
        return confirmacionAlerta(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

def lambda_handler(event, context):
    response = dispatch(event)
    return response
    