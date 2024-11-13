from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/call-service-b")
async def call_service_b():
    # Define the path to the Unix Domain Socket
    uds_path = "/tmp/service_b.sock"

    # Use a custom transport to make requests via the UDS
    transport = httpx.AsyncHTTPTransport(uds=uds_path)

    # Construct the URL as if we're communicating over regular HTTP
    url = "http://service_b/data"  # No need for http+unix://

    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get(url)
    return response.json()
