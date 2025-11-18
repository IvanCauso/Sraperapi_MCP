import os
from scraperapi_mcp_server import create_app

SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")
PORT = int(os.getenv("PORT", "8080"))

# Create MCP server app from package
app = create_app(api_key=SCRAPER_API_KEY)

# Start HTTP server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
