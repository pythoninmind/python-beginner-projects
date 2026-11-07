import http.client
import json
import urllib.parse
from datetime import datetime

def get_coordinates(city_name):
    """Holt die Breiten- und Längengrade für eine Stadt über die Open-Meteo Geocoding API."""
    encoded_city = urllib.parse.quote(city_name)
    geo_url = f"/v1/search?name={encoded_city}&count=1&language=de&format=json"
    
    conn = http.client.HTTPSConnection("geocoding-api.open-meteo.com")
    try:
        conn.request("GET", geo_url)
        response = conn.getresponse()
        if response.status != 200:
            return None
        
        data = json.loads(response.read().decode())
        if not data.get("results"):
            return None
        
        result = data["results"][0]
        return {
            "lat": result["latitude"],
            "lon": result["longitude"],
            "name": result["name"],
            "country": result.get("country", "")
        }
    except Exception:
        return None
    finally:
        conn.close()

def get_weather_report(lat, lon):
    """Ruft aktuelle Wetterdaten und Stundenvorhersagen von Open-Meteo ab."""
    weather_url = (
        f"/v1/forecast?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m"
        "&hourly=temperature_2m,weather_code&forecast_days=1"
    )
    
    conn = http.client.HTTPSConnection("api.open-meteo.com")
    try:
        conn.request("GET", weather_url)
        response = conn.getresponse()
        if response.status != 200:
            return None
        return json.loads(response.read().decode())
    except Exception:
        return None
    finally:
        conn.close()

def interpret_wmo_code(code):
    """Übersetzt WMO-Wettercodes in lesbaren Text und Emojis."""
    wmo_codes = {
        0: ("Klarer Himmel", "☀️"),
        1: ("Hauptsächlich klar", "🌤️"),
        2: ("Teilweise bewölkt", "⛅"),
        3: ("Bedeckt", "☁️"),
        45: ("Nebel", "🌫️"),
        48: ("Ablagernder Reifnebel", "🌫️"),
        51: ("Leichter Nieselregen", "🌧️"),
        53: ("Mäßiger Nieselregen", "🌧️"),
        55: ("Dichter Nieselregen", "🌧️"),
        61: ("Leichter Regen", "💧"),
        63: ("Mäßiger Regen", "🌧️"),
        65: ("Starker Regen", "🌧️"),
        71: ("Leichter Schneefall", "🌨️"),
        73: ("Mäßiger Schneefall", "🌨️"),
        75: ("Starker Schneefall", "🌨️"),
        80: ("Leichte Regenschauer", "🌦️"),
        81: ("Mäßige Regenschauer", "🌧️"),
        82: ("Starke Regenschauer", "⛈️"),
        95: ("Gewitter", "⛈️"),
    }
    return wmo_codes.get(code, ("Unbekannt", "❓"))

def main():
    print("=" * 45)
    print("      API-BASIERTER WETTERBERICHT")
    print("=" * 45)
    
    city_input = input("Bitte geben Sie den Städtenamen ein: ").strip()
    if not city_input:
        print("Ungültige Eingabe.")
        return

    print(\n[Info] Suche nach Koordinaten für '{city_input}'...")
    location = get_coordinates(city_input)
    
    if not location:
        print("[-] Stadt konnte nicht gefunden oder Geocoding-API nicht erreicht werden.")
        return

    print(f"[+] Gefunden: {location['name']} ({location['country']})")
    print("[Info] Rufe aktuelle Wetterdaten ab...")
    
    weather_data = get_weather_report(location['lat'], location['lon'])
    if not weather_data:
        print("[-] Wetterdaten konnten nicht geladen werden.")
        return

    # Aktuelle Wetterdaten extrahieren
    current = weather_data["current"]
    condition, emoji = interpret_wmo_code(current["weather_code"])
    
    print("\n" + "=" * 45)
    print(f" WETTERBERICHT FÜR {location['name'].upper()}")
    print("=" * 45)
    print(f"Stand:          {datetime.fromisoformat(current['time']).strftime('%d.%m.%Y %H:%M')}")
    print(f"Zustand:        {emoji} {condition}")
    print(f"Temperatur:     {current['temperature_2m']} °C (Gefühlt: {current['apparent_temperature']} °C)")
    print(f"Luftfeuchtigkeit:{current['relative_humidity_2m']}%")
    print(f"Windgeschw.:    {current['wind_speed_10m']} km/h")
    print(f"Niederschlag:   {current['precipitation']} mm")
    print("=" * 45)

    # Vorschau für die nächsten Stunden (alle 3 Stunden gefiltert)
    print(" VORSCHAU FÜR HEUTE:")
    print("-" * 45)
    hourly = weather_data["hourly"]
    
    current_hour = datetime.now().hour
    count = 0
    
    for time_str, temp, code in zip(hourly["time"], hourly["temperature_2m"], hourly["weather_code"]):
        forecast_time = datetime.fromisoformat(time_str)
        
        # Zeige nur zukünftige Stunden des heutigen Tages im 3-Stunden-Takt
        if forecast_time.hour >= current_hour and count < 4:
            hr_condition, hr_emoji = interpret_wmo_code(code)
            time_formatted = forecast_time.strftime("%H:%M")
            print(f" [{time_formatted}]  {temp:5.1f} °C   {hr_emoji}  {hr_condition}")
            count += 1
            
    print("=" * 45)

if __name__ == "__main__":
    main()
