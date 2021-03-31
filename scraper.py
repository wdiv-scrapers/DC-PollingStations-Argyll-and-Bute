from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://opendata.arcgis.com/datasets/6b49d2cc9ce44026a3fc232461780c42_18.geojson"
districts_url = "https://opendata.arcgis.com/datasets/acae4681cabe4ed58d150f3ec9697e25_19.geojson"
council_id = 'AGB'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
