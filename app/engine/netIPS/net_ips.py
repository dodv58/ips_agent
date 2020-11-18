from app.engine.base_engine import BaseEngine
import json, yaml
import os
from app import utils

import logging
logger = logging.getLogger()

class NetIPS(BaseEngine):
    config = {}
    commands = None

    def init_app(self, app):
        for k, v in app.config.items():
            self.config[k] = v

        # read commands from config file
        config_file = "{}/engine/config/netIPS/netips_{}.conf".format(app.root_path, self.config.get('OS_TYPE') or 'centos')
        with open(config_file) as c:
            self.commands = json.load(c)

    def running_status(self):
        command = self.commands.get('engine_status')
        if not command:
            return False
        return_code, out, err = utils.system_execute(command)
        if return_code:
            logger.error(err)
            return False
        else:
            logger.info(out)
            return True

    def start_service(self):
        command = self.commands.get('start_engine')
        if not command:
            return False
        return_code, out, err = utils.system_execute(command)
        if return_code:
            logger.error(err)
            return False
        else:
            logger.info(out)
            return True

    def stop_service(self):
        command = self.commands.get('stop_engine')
        if not command:
            return False
        return_code, out, err = utils.system_execute(command)
        if return_code:
            logger.error(err)
            return False
        else:
            logger.info(out)
            return True
