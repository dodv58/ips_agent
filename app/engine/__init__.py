from .suricata.suricata import Suricata
from .netIPS.net_ips import NetIPS

def init_engine(app):
    if app.config.get('IPS_ENGINE') == 'suricata':
        engine = Suricata()
    elif app.config.get('IPS_ENGINE') == 'netips':
        engine = NetIPS()

    if engine:
        engine.init_app(app)
        return engine
    else:
        return None