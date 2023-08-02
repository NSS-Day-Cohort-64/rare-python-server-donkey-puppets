from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views import get_all_tags, get_single_tag
from views.user import create_user, login_user
from views.category_requests import get_all_categories, get_single_category, create_category
from views.tag_requests import get_single_tag, get_all_tags
from views import get_all_categories, get_single_category, get_all_posts
from urllib.parse import urlparse
from views import create_post



class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""
    def parse_url(self, path):
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)
    def do_GET(self):
        response = ""
        parsed = self.parse_url(self.path)
        ( resource, id, query_params) = parsed

        if resource == "posts":
            response = get_all_posts()
            self._set_headers(200)

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
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        parsed = self.parse_url(self.path)
        ( resource, id, query_params) = parsed
        response = None

        if resource == 'login':
            response = login_user(post_body)
        elif resource == 'register':
            response = create_user(post_body)

        if resource == 'categories':
            response = create_category(post_body)

        elif resource == 'posts':
            response = create_post(post_body)

        if response is not None:
            self._set_headers(201)
            response_str = json.dumps(response)
            self.wfile.write(response_str.encode())
        else:
            self._set_headers(400)
            error_response = {"error": "Invalid request"}
            error_response_str = json.dumps(error_response)
            self.wfile.write(error_response_str.encode())



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
