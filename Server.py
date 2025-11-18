import os
import requests
from fastmcp import FastMCP

# Initialize MCP server
app = FastMCP("ScraperAPI MCP")

SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")

@app.tool()
def scrape_url(url: str):
    """
    Scrape a URL using ScraperAPI with autoparse enabled.
    Returns parsed SERP JSON or error details.
    """
    if not SCRAPER_API_KEY:
        return {"error": "SCRAPER_API_KEY not set"}

    try:
        api_url = (
            "https://api.scraperapi.com?"
            f"api_key={SCRAPER_API_KEY}"
            "&autoparse=true"
            "&url=" + requests.utils.quote(url)
        )

        print(f"[DEBUG] Scraping: {api_url}")

        resp = requests.get(api_url, timeout=25)
        resp.raise_for_status()

        return {
            "input_url": url,
            "scraperapi_request_url": api_url,
            "result": resp.json()
        }

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return {"error": str(e), "url": url}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    print(f"[INFO] ScraperAPI MCP server running on port {port}")
    app.run("http", host="0.0.0.0", port=port)
