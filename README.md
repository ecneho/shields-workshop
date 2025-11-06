# shields-workshop
Make your Workshop pages clean and stylish by displaying custom [shields.io](https://shields.io/badges) badges:
- Steam Update Date
- Discord Server Online
- Patreon Member Count

Helps shorten long links, saving valuable space on both the page and preview cards.

## Usage
This script is hosted on **`https://ecneho.pythonanywhere.com`** and can be fetched from for free anytime.

To run locally, refer to the [Flask Documentation: Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/).

## Endpoints
|Route					| Used Badge Type  								|
|---------------------------------------|-----------------------------------------------------------------------|
|`<host>/b/d/<discord-server-id>`	| [Discord](https://shields.io/badges/discord)  			|
|`<host>/b/sud/<workshop-id>`		| [Steam Update Date](https://shields.io/badges/steam-update-date)  	|
|`<host>/b/p/<patreon-nickname>`	| [Patreon Badge by Endel](https://shieldsio-patreon.vercel.app)  	|

## Steam Workshop Examples

`[img]https://ecneho.pythonanywhere.com/b/sud/2851584592[/img]`

<img src="https://ecneho.pythonanywhere.com/b/sud/2851584592">

-----

`[img]https://ecneho.pythonanywhere.com/b/d/1341422960308912280[/img]`

<img src="https://ecneho.pythonanywhere.com/b/d/1341422960308912280">

-----

`[img]https://ecneho.pythonanywhere.com/b/p/ecneho[/img]`

<img src="https://ecneho.pythonanywhere.com/b/p/ecneho">