def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    result = [bytes(i + '\n', 'utf8') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return iter(result)
