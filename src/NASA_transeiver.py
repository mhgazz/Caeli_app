import os
from skyfield.api import load
from datetime import datetime
import pytz
import os
#os.environ['REQUESTS_CA_BUNDLE'] = '/Caeli_app/nasa_ca.pem'

""" 
paso previo:
pip install skyfiled 
pip install pytz
"""

class NASA_transeiver():

    def __init__(self):
        pass

    def get_positions_now(self):
        """ obtener posiciones planetarias ahora """

        # Cargar efemérides y tiempos
        planetas = load('de421.bsp')  # Modelo planetario
        ts = load.timescale()
        ahora = ts.now()  # Tiempo actual exacto

        # Definir cuerpos celestes
        tierra = planetas['earth']
        marte = planetas['mars']
        luna = planetas['moon']

        # Calcular posiciones
        pos_marte = tierra.at(ahora).observe(marte).apparent()
        pos_luna = tierra.at(ahora).observe(luna).apparent()

        # Coordenadas eclípticas (usadas en astrología)
        lat_marte, lon_marte, _ = pos_marte.ecliptic_latlon()
        lat_luna, lon_luna, _ = pos_luna.ecliptic_latlon()

        # Distancia (en UA)
        dist_marte = pos_marte.distance().au
        dist_luna = pos_luna.distance().au

        # Imprimir resultados
        print(f"📅 Fecha y hora: {ahora.utc_datetime().strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print(f"\n🔴 Marte:")
        print(f"- Longitud eclíptica: {lon_marte.degrees:.2f}°")
        print(f"- Latitud eclíptica: {lat_marte.degrees:.2f}°")
        print(f"- Distancia a la Tierra: {dist_marte:.3f} UA")

        print(f"\n🌕 Luna:")
        print(f"- Longitud eclíptica: {lon_luna.degrees:.2f}°")
        print(f"- Latitud eclíptica: {lat_luna.degrees:.2f}°")
        print(f"- Distancia a la Tierra: {dist_luna:.6f} UA (~{dist_luna * 384400:.1f} km)")

        # Bonus: ¿En qué signo zodiacal está la Luna? (astrología tropical)
        signos = ['Aries', 'Tauro', 'Géminis', 'Cáncer', 'Leo', 'Virgo', 
                'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario', 'Piscis']
        signo_luna = signos[int(lon_luna.degrees // 30)]
        signo_marte = signos[int(lon_marte.degrees // 30)]
        print(f"\n✨ Astrológicas")
        pos_luna = str(int(lon_luna.degrees % 30))
        pos_marte = str(int(lon_marte.degrees % 30))
        print(f"La Luna está en {pos_luna} grados {signo_luna}")
        print(f"Marte está en {pos_marte} grados {signo_marte}")

        return "{{'luna';'" + signo_luna + "';" + pos_luna + "}" \
            ",{'marte';'" + signo_marte + "';" + pos_marte + "}}"