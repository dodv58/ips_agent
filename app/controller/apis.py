from flask import request
from app.utils import json_response
from app import _engine
from . import (
    blueprint
)

@blueprint.route('/status', methods=['GET'])
def get_engine_running_status():
    res = _engine.running_status()
    return json_response(data=res)

@blueprint.route('/start', methods=['GET'])
def start_engine():
    res = _engine.start_service()
    return json_response(data={
        'status': res
    })

@blueprint.route('/stop', methods=['GET'])
def stop_engine():
    res = _engine.stop_service()
    return json_response(data={
        'status': res
    })

@blueprint.route('/iface-list', methods=['GET'])
def get_iface_list():
    res = _engine.get_iface_list()
    return json_response(data={
        'status': res
    })
