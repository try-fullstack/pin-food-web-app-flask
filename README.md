## Pin Food

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

## System Requirements

- Google API Key to access the Google Map.
- MySQL or MariaDB to store data on food stalls.
- Python 3.x.



