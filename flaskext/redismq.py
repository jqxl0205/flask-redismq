# -*- coding: utf-8 -*-
"""
    flaskext.redismq
    ~~~~~~~~~~~~~~~~

    Adds message queue using Redis support to your application.

    :copyright: (c) 2011 by He Weiwei.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps
from hotqueue import HotQueue

class RedisMQ(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

        self._tasks = {}

    def init_app(self, app):
        name = app.config.setdefault('REDISMQ_NAME', 'mq')
        host = app.config.setdefault('REDISMQ_HOST', 'localhost')
        port = app.config.setdefault('REDISMQ_PORT', 6379)
        db = app.config.setdefault('REDISMQ_DB', 0)
        password = app.config.setdefault('REDISMQ_PASSWORD', None)

        app.config.get('REDISMQ_BLOCK', True),
        app.config.get('REDISMQ_BLOCK_TIMEOUT', 0)
        
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['redismq'] = self

        self.app = app
        self._hq = HotQueue(name, host=host, port=port, db=db,
                            password=password)

    def task(self, func):
        
        func_name = "%s.%s" % (func.__module__, func.__name__)
        self._tasks[func_name] = func

        @wraps(func)
        def _func(*args, **kwargs):
            self._hq.put((func_name, args, kwargs))

        setattr(func, "async", _func)
        return func        

    def work(self, *args, **kwargs):
        kwargs.update({
            'block': self.app.config.get('REDISMQ_BLOCK', True),
            'timeout': self.app.config.get('REDISMQ_BLOCK_TIMEOUT', 0)
        })
        
        @self._hq.worker(*args, **kwargs)
        def _worker(msg):
            try:
                func_name, args, kwargs = msg
                self._tasks[func_name](*args, **kwargs)
            except Exception, e:
                pass

        return _worker()
