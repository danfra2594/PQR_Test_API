import json
import os
import boto3
from boto3.dynamodb.conditions import Attr
from types import SimpleNamespace
import datetime

def registarCaso(event, context):

    try:
        object = json.loads(event['body'], object_hook=lambda d: SimpleNamespace(**d))
        REGISTER_TABLE = os.environ['REGISTRARCASO_TABLE']
        dynamodb = boto3.resource('dynamodb')
        tableRegister = dynamodb.Table(REGISTER_TABLE)

        result = tableRegister.put_item(
                Item={
                    'id': object.Id,
                    'caso': object.Caso,
                    'identificacion': object.Identificacion,
                    'nombre': object.Nombre,
                    'direccion': object.Direccion,
                    'telefono': object.Telefono,
                    'email': object.Email,
                    'mensaje': object.Mensaje,
                    'fecha': datetime.datetime.now().isoformat()
                }
            )

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(result)
        }
        return response
    except Exception as e:
        err = format(e)
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(str(err))
        }
        return response

def listarCasos(event, context):

    try:
        REGISTER_TABLE = os.environ['REGISTRARCASO_TABLE']
        dynamodb = boto3.resource('dynamodb')
        tableRegister = dynamodb.Table(REGISTER_TABLE)

        result = tableRegister.scan(
        )

        result1 = str(result['Items'])
        # print(result1)
        result1 = result1.replace("Decimal('", "")
        result1 = result1.replace("')", "")
        result1 = result1.replace("'", '"')
        # print(result1)

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(result1)
        }
        return response
    except Exception as e:
        err = format(e)
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(str(err))
        }
        return response

def registrarRespuesta(event, context):
    try:
        object = json.loads(event['body'], object_hook=lambda d: SimpleNamespace(**d))
        SEGUIMIENTOCASO_TABLE = os.environ['SEGUIMIENTOCASO_TABLE']
        dynamodb = boto3.resource('dynamodb')
        tableSeguimiento = dynamodb.Table(SEGUIMIENTOCASO_TABLE)

        result = tableSeguimiento.put_item(
                Item={
                    'id': object.Id,
                    'idRegister': object.IdRegister,
                    'respuestaAdmin': object.RespuestaAdmin,
                    'respuestaUser': object.RespuestaUser,
                    'mensaje': object.Mensaje,
                    'fecha': datetime.datetime.now().isoformat()
                }
            )

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(result)
        }
        return response  
    except Exception as e:
        err = format(e)
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(str(err))
        }
        return response
        
def listarRespuesta(event, context):
    try:

        idRegister = str(event['queryStringParameters']['IdRegister'])
        SEGUIMIENTOCASO_TABLE = os.environ['SEGUIMIENTOCASO_TABLE']
        dynamodb = boto3.resource('dynamodb')
        tableSeguimiento = dynamodb.Table(SEGUIMIENTOCASO_TABLE)

        result = tableSeguimiento.scan(
        )

        result1 = str(result['Items'])
        # print(result1)
        result1 = result1.replace("Decimal('", "")
        result1 = result1.replace("')", "")
        result1 = result1.replace("'", '"')
        result1 = result1.replace("True", 'true')
        result1 = result1.replace("False", 'false')
        # print(result1)

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(result1)
        }
        return response
    except Exception as e:
        err = format(e)
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(str(err))
        }
        return response