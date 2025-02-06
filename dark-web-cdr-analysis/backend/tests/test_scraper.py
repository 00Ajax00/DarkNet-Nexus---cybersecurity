from backend.scraper import scrape_darkweb

def test_scraper_returns_data():
    data = scrape_darkweb()
    assert isinstance(data, list)
    assert len(data) > 0
