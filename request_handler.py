from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views import get_all_tags, get_single_tag
from views.user import create_user, login_user
from views import create_tag
from views.category_requests import get_all_categories, get_single_category


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def do_GET(self):
        response = {}
        parsed = self.parse_url()

        (resource, id) = parsed
        if resource == "categories":
            if id is not None:
                response = get_single_category(id)
                self._set_headers(200)
            else:
                response = get_all_categories()
                self._set_headers(200)
        if resource == "tags":
            if id is not None:
                response = get_single_tag(id)
                self._set_headers(200)
            else:
                response = get_all_tags()
                self._set_headers(200)
        self.wfile.write(json.dumps(response).encode())
    # def do_GET(self):
    #     self._set_headers(200)

    #     response = {}

    #     # Parse URL and store entire tuple in a variable
    #     parsed = self.parse_url(self.path)

    #     # If the path does not include a query parameter, continue with the original if block
    #     if '?' not in self.path:
    #         (resource, id) = parsed

    #         if resource == "tags":
    #             if id is not None:
    #                 response = get_single_tag(id)
    #             else:
    #                 response = get_all_tags()
    #         if resource == "categories":
    #             if id is not None:
    #                 response = get_single_category(id)
    #             else:
    #                 response = get_all_categories()

    #     self.wfile.write(json.dumps(response).encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, id) = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        elif resource == 'register':
            response = create_user(post_body)
        elif resource == 'tags':
            response = create_tag(post_body)

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        pass

    def do_DELETE(self):
        """Handle DELETE Requests"""
        pass


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
