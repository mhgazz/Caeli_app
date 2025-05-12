""" 
Flask
paso previo:
pip install skyfiled 
pip install pytz
"""

from flask import Flask
from NASA_transeiver import NASA_transeiver

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello():
    greeting = "<html><head></head><body>" \
        "<H1>Bienvenido a Caeli</H1>" \
        "Interfaz astrobiologico" \
        "<br/><br/>" \
        "<b>Verbos</b>" \
        "<br/>/efemerides/now : posiciones en el cielo actual" \
        "<br/>/efemerides/-fecha-/-hora- : posiciones para un momento especificado" \
        "</body></html>"
    return str(greeting)

@app.route('/efemerides/now')
# ‘/’ URL is bound with hello_world() function.
def efemerides_now():
    """ obtener efemerides del momento actual """
    trans = NASA_transeiver()
    metrics = trans.get_positions_now()
    return str(metrics)

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()