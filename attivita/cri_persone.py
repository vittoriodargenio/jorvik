import requests
from django.conf import settings
import logging
from urllib.parse import urlencode, quote_plus


end_point = settings.APIS_CONF['crip']['endpoint']
am_end_pont = settings.APIS_CONF['crip']['am_end_pont']

logger = logging.getLogger(__name__)


def getServiziStandard(max_result=500, summary='', description='', obbiettivo=None):

    params = {}
    if summary:
        params['summary'] = '{}*'.format(summary)
    if description:
        params['description'] = '{}*'.format(description)
    if obbiettivo:
        params['strategic_objective'] = 'Obiettivo {}'.format(obbiettivo)

    r = requests.get(
        '{}/service/?maxResults={}{}'.format(
            end_point,
            max_result,
            '&{}'.format(urlencode(params, quote_plus))
        )
    )

    resp = r.json()
    logger.debug('- getServiziStandard {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if r.status_code == 200 else {}


def getBeneficiary():
    r = requests.get(
        '{}/generic_issue/CRIP-BeneficiaryType/'.format(end_point)
    )
    return r.json() if r.status_code == 200 else {}


def getPrevisioning():
    r = requests.get(
        '{}/generic_issue/CRIP-Provision'.format(end_point)
    )
    return r.json() if r.status_code == 200 else {}


def updateServizio(key, **kwargs):
    data = {}
    if kwargs.get('referenti'):
        data['accountables'] = [{'name': '{}.{}'.format(
            ref.nome.lower(), ref.cognome.lower()
        )} for ref in kwargs.get('referenti')]
        logger.debug('- referenti {}'.format(kwargs.get('referenti')))

    if kwargs.get('precedenti'):
        l = []
        for ref in kwargs.get('precedenti'):
            l.append({'name': ref})
        if 'accountables' in data:
            data['accountables'].extend(l)
        else:
            data['accountables'] = l
        logger.debug('- precedenti {}'.format(kwargs.get('precedenti')))

    if kwargs.get('servizi'):
        ss = ""
        for s in kwargs.get('servizi'):
            ss += "{},".format(s)
        data['service'] = [ss[:-1] if ss else ""]
        print(data['service'])

    if kwargs.get('testo'):
        data['description'] = kwargs.get('testo')

    if kwargs.get('address'):
        data['address'] = kwargs.get('address')

    if kwargs.get('summary'):
        data['summary'] = kwargs.get('summary')

    if kwargs.get('project'):
        data['project'] = kwargs.get('project')

    r = requests.put(
        '{}/offeredserviceextended/{}/'.format(end_point, key),
        json=data
    )
    resp = r.json()
    logger.debug('- updateServizio {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'result' in resp and resp['result']['code'] == 204 else {}


def update_service(key, **kwargs):

    r = requests.put(
        '{}/offeredserviceextended/{}/'.format(end_point, key),
        json=kwargs
    )
    print(kwargs)
    resp = r.json()
    logger.debug('- _updateServizio {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'result' in resp and resp['result']['code'] == 204 else {}

def changeState(key='', state='', new_state=''):

    STATE_TO_CODE = {
        "11301": {
            "10413": 11
        },
        "10413": {
            "11301": 51,
            "6": 21
        },
        "6": {
            "10413": 31,
            "11301": 41
        }
    }

    r = requests.post(
        '{}/offeredservice/{}/transition/{}/'.format(end_point, key, STATE_TO_CODE[state][new_state])
    )
    resp = r.json()
    logger.debug('- changeState {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'result' in resp and resp['result']['code'] == 204 else {}


def createServizio(comitato, nome_progetto, servizi=[]):
    ss = ""
    for s in servizi:
        ss += "{},".format(s)

    data = {
        "committee": str(comitato),
        "project": nome_progetto,
        "service": [ss[:-1]],
        "summary": nome_progetto
    }

    r = requests.post(
        '{}/offeredservice/'.format(end_point),
        json=data
    )
    resp = r.json()
    logger.debug('- createServizio {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'data' in resp and resp['data'] else {}


def getServizio(key=''):
    r = requests.get(
        '{}/offeredserviceextended/{}'.format(end_point, key)
    )
    resp = r.json()
    logger.debug('- getServizio {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'data' in resp and resp['data'] else {}


def getListService(comitato, name=''):

    params = {}
    if comitato:
        params['committee'] = '{}'.format(comitato)
    if name:
        params['project'] = '{}'.format(name)

    r = requests.get(
        '{}/offeredservice/?{}'.format(
            end_point,
            urlencode(params, quote_plus)
        )
    )

    resp = r.json()
    logger.debug('- getListService {} {} {}'.format(r.url, resp['result']['code'], resp['result']['description']))
    return resp if 'data' in resp and resp['data'] else {}


def deleteService(key=''):
    r = requests.delete(
        '{}/offeredservice/{}'.format(end_point, key)
    )
    resp = r.json()
    logger.debug('- deleteService {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'result' in resp and resp['result']['code'] == 204 else {}


def createStagilTurni(giorni=[], apertura='', chiusura='', id=0):
    data = {
        "giorno": giorni,
        "orario_apertura": apertura,
        "orario_chiusura": chiusura,
        "customFieldId": "11723",
        "issueId": id
    }

    r = requests.post(
        '{}/stagiltables/'.format(end_point),
        json=data
    )
    resp = r.json()
    logger.debug('- createStagilTurni {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'data' in resp and resp['data'] else {}

def deleteStagil(id=0):
    r = requests.delete(
        '{}/stagiltables/{}/'.format(end_point, id)
    )
    resp = r.json()
    logger.debug('- deleteStagil {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'result' in resp and resp['result']['code'] == 204 else {}


def createStagilContatti(tipo_contatto='', nome='', telefono='', email='', id=0):
    data = {
        "tipo_contatto": [str(tipo_contatto)],
        "nome": nome,
        "telefono": telefono,
        "email": email,
        "customFieldId": "11857",
        "issueId": id
    }

    r = requests.post(
        '{}/stagiltables/'.format(end_point),
        json=data
    )
    resp = r.json()
    logger.debug('- createStagilContatti {} {}'.format(resp['result']['code'], resp['result']['description']))
    return resp if 'data' in resp and resp['data'] else {}
