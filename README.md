## Pin Food

[![Support me on Patreon](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3DTryFullStack%26type%3Dpatrons%26suffix%3DTry%2520Full%2520Stack&style=for-the-badge)](https://patreon.com/TryFullStack)

Is a web application (Built with Flask and MariaDB) that displays a page containing an
interactive map. The user can mark the location of a new "food stall" on the map.
Users can enter the date, category, and description of the "food stall".

![show](https://github.com/try-fullstack/pin-food-web-app-flask/blob/master/header.jpg)

## Quick Start

Run the following command to install the dependency packages:

```
pip install -r requirements.txt
```

Open `templates/home.py` and replace `YOUR_APIKEY` with your API Key: 

```html
<script
  type="text/javascript"
  src="https://maps.googleapis.com/maps/api/js?key=YOUR_APIKEY&callback=init">
</script>
```

Run MySQL/MariaDB Server, then run `dbsetup.py` to create the database and table:

```
python dbsetup.py
```

Run this project:

```
python pinfood.py
```

Open the url `http://localhost:5000` in a browser.

## System Requirements

- Google API Key to access the Google Map.
- MySQL or MariaDB to store data on food stalls.
- Python 3.x.



