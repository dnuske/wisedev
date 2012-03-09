# -*- coding: utf-8 *-*
import tornado.ioloop
import tornado.web

import com


class MainHandler(tornado.web.RequestHandler):
    def __init__(self):
        super(MainHandler, self).__init__()

class read(tornado.web.RequestHandler):
    def get(self):
        ret = com.read(self.get_argument('timestamp'))
        self.write(ret)

class write(tornado.web.RequestHandler):
    def get(self):
        ret = com.write({'msg':self.get_argument('msg')})
        self.write(ret)

class index(tornado.web.RequestHandler):
    def get(self):
        ret = open('static/index.html').read()
        self.write(ret)

class jqueryjs(tornado.web.RequestHandler):
    def get(self):
        ret = open('static/jquery.js').read()
        self.write(ret)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ret = com.read(self.get_argument('timestamp'))
        self.write(ret)

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)






import server
class serverr(tornado.web.RequestHandler):
    def get(self):
        ret = com.write({'msg':self.request.query})

        method = self.get_argument('method')
        params = self.get_argument('params')

        res = getattr(server, method)(params)

        self.write(str(res))

application = tornado.web.Application([
    (r"/read.php", read),
    (r"/write.php", write),
    (r"/", index),
    (r"/jquery.js", jqueryjs),
    (r"/story/([0-9]+)", StoryHandler),
    (r"/server", serverr),
])






if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

"""

#clientSide prog
client events
onChangeLayout
onScroll
onLoad

#serverSide prog
    client.callMethod(name,params)
    client.getAttr
    client.setAttr
    client.removeAttr

    server.callMethod
    server.setMethod
    server.removeMethod

#client
server.execute(code)
server.callMethod(method, params)

"""

