from flask import Flask, Response
import requests

app = Flask(__name__)

STEAM_TEMPLATE = "https://img.shields.io/steam/update-date/{steam_id}?style=for-the-badge&logo=steam&label=last%20updated%20%20⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

@app.route('/b/sud/<id>')
def steam(id):
    image_url = STEAM_TEMPLATE.format(steam_id=id)
    r = requests.get(image_url)

    if r.status_code == 200:
        content_type = r.headers.get("Content-Type", "image/svg+xml")
        return Response(r.content, content_type=content_type, headers={"Access-Control-Allow-Origin": "*"})
    else:
        return "Failed to fetch", 500

DISCORD_TEMPLATE = "https://img.shields.io/discord/{discord_id}?style=for-the-badge&logo=discord&logoColor=white&color=cornflowerblue&label=discord%20server⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

@app.route('/b/d/<id>')
def discord(id):
    image_url = DISCORD_TEMPLATE.format(discord_id=id)
    r = requests.get(image_url)

    if r.status_code == 200:
        content_type = r.headers.get("Content-Type", "image/svg+xml")
        return Response(r.content, content_type=content_type, headers={"Access-Control-Allow-Origin": "*"})
    else:
        return "Failed to fetch", 500

PATREON_TEMPLATE = "https://img.shields.io/endpoint?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%2F%3Fusername%3D{patreon_id}%26type%3Dpatrons&style=for-the-badge&logo=patreon&label=patreon%20⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

@app.route('/b/p/<id>')
def patreon(id):
    image_url = PATREON_TEMPLATE.format(patreon_id=id)
    r = requests.get(image_url)

    if r.status_code == 200:
        content_type = r.headers.get("Content-Type", "image/svg+xml")
        return Response(r.content, content_type=content_type, headers={"Access-Control-Allow-Origin": "*"})
    else:
        return "Failed to fetch", 500