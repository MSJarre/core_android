#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['EkylibreApi']

from mycroft.configuration import ConfigurationManager
from mycroft.util.log import LOG
# from mycroft_ekylibre_utils.tls_adapter import TlsAdapter
import requests


class EkylibreApi:
    """Ekylibre API class"""

    def __init__(self):
        self.config_api = ConfigurationManager.get().get("ekylibre_api")
        self.url = "https://{host}/api/v1/".format(host=self.config_api.get('host'))
        self.user = self.config_api.get('user')
        self.password = self.config_api.get('password')
        # self.token = self.config_api.get('token')
        self.session = requests.Session()
        # if self.host:
        #     self.session.headers.update({'Host': self.host})
        # self.session.mount("https://", TlsAdapter())
        # self.session.verify = False
        self.auth = None
        self.get_token()

    def close_session(self):
        if self.session:
            self.session.close()

    def get(self, endpoint, payload=None):
        LOG.debug("GET")

        try:
            url = self.url + endpoint
            LOG.debug("PAYLOAD -> {}".format(str(payload)))
            r = self.session.get(url, json=payload)
        except Exception as err:
            LOG.error("API POST error: {}".format(err))
            return "API GET error: {}".format(err)
        return r.json()

    def post(self, endpoint, payload):
        LOG.debug("POST")

        try:
            url = self.url + endpoint
            LOG.debug("PAYLOAD -> {}".format(str(payload)))
            r = self.session.post(url, json=payload)
        except Exception as err:
            LOG.error("API POST error: {}".format(err))
            return "API POST error: {}".format(err)
        return r.json()

    def get_token(self):
        LOG.info("GET TOKEN")
        try:
            endpoint = self.url + "tokens"
            payload = {'email': self.user, 'password': self.password}

            r = self.session.post(endpoint, data=payload)
            r.encoding = 'utf-8'
            LOG.info("response " + r.text)

            if r.status_code == requests.codes.ok:
                token = r.json()
                self.auth = "simple-token {} {}".format(self.user, token['token'])
                self.session.headers.update({'Authorization': self.auth})
            else:
                LOG.error(r.status_code, r.content)

        except Exception as err:
            LOG.error("Unable to get token: {0}".format(err))
            return "Unable to get token: {0}".format(err)
