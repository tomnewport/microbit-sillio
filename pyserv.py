import os
import tornado.ioloop
import tornado.web
from subprocess import check_output
from time import sleep

outputs = {
    "/lh" :
"""

   [ No microbits display found ]








""",

    "/lhK" :

"""

   [ xxxxx ]
   [ x   x ]
   [ x   x ]
   [ x   x ]
   [ xxxx  ]

  A [ ]  B [ ]

""",

    "/lhKA" :

"""

   [ xxxxx ]
   [ xx xx ]
   [ x   x ]
   [ xx xx ]
   [ xxxx  ]

  A [x]  B [ ]

""",

    "/lhKB" :

"""

   [ xxxxx ]
   [ x   x ]
   [ x x x ]
   [ x   x ]
   [ xxxx  ]

  A [ ]  B [x]

""",

    "/lhKAB" :

"""

   [ xxxxx ]
   [ xx xx ]
   [ x x x ]
   [ xx xx ]
   [ xxxx  ]

  A [x]  B [x]

"""
}

class StaticFileHandler(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(StaticFileHandler, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(StaticFileHandler, self).get(self.filename, include_body)

class Nyandler(tornado.web.RequestHandler):
    def get(self):
        if checknyan()["nyan"]:
            nyanstop()
        else:
            nyanstart()

class LightHandler(tornado.web.RequestHandler):
    def get(self):
        if self.request.uri != "/lh":
            print("\n"*10)
            print(outputs[self.request.uri])

app = tornado.web.Application([
    ('/', StaticFileHandler, {'path': './index.htm'}),
    ('/node_modules/tracking/build/tracking-min.js', StaticFileHandler, {'path': './node_modules/tracking/build/tracking-min.js'}),
    (r'/lh.*', LightHandler)
])

app.listen(8888)
tornado.ioloop.IOLoop.current().start()
