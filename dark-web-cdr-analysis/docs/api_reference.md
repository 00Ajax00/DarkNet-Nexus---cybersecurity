# docs/api_reference.md

## **Authentication**
### `POST /login`
- **Description:** Authenticates a user and returns a JWT token.
- **Response:** `{ "token": "xyz" }`

## **Dark Web Scraper**
### `GET /scrape`
- **Description:** Fetches data from the dark web.
- **Response:** `{ "data": "scraped content" }`

## **Anomaly Detection**
### `GET /detect`
- **Description:** Detects anomalies in CDR data.
- **Response:** `{ "anomalies": [] }`
