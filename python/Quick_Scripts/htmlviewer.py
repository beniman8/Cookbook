import http.server
import os 
import socketserver
import webbrowser


class HTMLViewer:
    def __init__(self,filename,port=8000):
        self.filename= filename
        self.port = port
        self._server: socketserver.TCPServer | None = None 
        
    def _open_browser(self):
        url = f"http://localhost:{self.port}/{self.filename}"
        webbrowser.open(url)
        
        
    def _serve(self):
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("",self.port),handler) as httpd:
            self._server = httpd 
            self._open_browser()
            print(f"Serving '{self.filename}' at http://localhost:{self.port}")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nKeyboard interrupt received. Shutting down server")
                httpd.shutdown()
                httpd.server_close()
                
    def start(self):
        os.chdir(os.path.dirname(os.path.abspath(self.filename)))
        self._serve()
                
