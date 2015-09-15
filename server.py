from wsgiref import simple_server
import preview

if __name__ == '__main__':

    server = simple_server.make_server('', 8080, preview.application)

    server.serve_forever()
