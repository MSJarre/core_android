#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
from urllib3 import PoolManager
from requests.adapters import HTTPAdapter
from mycroft.util.log import LOG


class TlsAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        LOG.info("TlsAdapter")
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_version=ssl.PROTOCOL_TLSv1_2)

    # def init_poolmanager(self, *args, **kwargs):
    #     ssl_context = ssl.create_default_context()
    #     ssl_context.options &= ~ssl.PROTOCOL_TLSv1_2
    #     ssl_context.check_hostname = False
    #     kwargs['ssl_context'] = ssl_context
    #     return super(TlsAdapter, self).init_poolmanager(*args, **kwargs)
