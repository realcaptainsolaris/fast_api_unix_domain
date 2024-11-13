# FastAPI Microservices Communication via Unix Domain Sockets with Docker

This project demonstrates how to set up two FastAPI microservices, `service_a` and `service_b`, to communicate via Unix Domain Sockets (UDS) within Docker. UDS provides a faster and more secure way to exchange data between services running on the same host compared to traditional TCP/IP.

## Project Structure

The directory structure for the project is as follows:

```
fastapi-uds-example/
├── docker-compose.yml   # Docker Compose file to manage both services
├── service_a/
│   ├── main.py          # FastAPI app for Service A
│   └── Dockerfile       # Dockerfile for Service A
└── service_b/
    ├── main.py          # FastAPI app for Service B
    └── Dockerfile       # Dockerfile for Service B
```

- `service_a` acts as a client and calls `service_b` over UDS.
- `service_b` listens on a Unix Domain Socket for requests.

## Requirements

- **Docker**: To containerize and run the microservices.
- **Python Libraries**: `fastapi`, `uvicorn`, and `httpx`.
  
## Setting Up the Microservices

### 1. `service_b` (Server)

`service_b` is a FastAPI service that exposes an endpoint at `/data`.

### 2. `service_a` (Client)

`service_a` makes an HTTP request to `service_b` over the UDS. It connects using `httpx` and a custom transport layer that supports UDS.

- **Volumes**: Both `service_a` and `service_b` share `/tmp`, allowing `service_a` to access the Unix Domain Socket at `/tmp/service_b.sock`.
- **Ports**: Port `8000` on `service_a` is mapped to port `8000` on the host, allowing access to the `/call-service-b` endpoint.

## Running the Application

To build and start both services:

```bash
docker-compose up --build
```

This command:

1. Builds the Docker images for `service_a` and `service_b`.
2. Starts `service_b`, which listens on `/tmp/service_b.sock`.
3. Starts `service_a`, which communicates with `service_b` via the Unix Domain Socket.

## Testing the Setup

Once both services are running, you can test the communication by calling `service_a`’s `/call-service-b` endpoint.

Open a new terminal and run:

```bash
curl http://localhost:8000/call-service-b
```

### Expected Output

```json
{"message": "Hello from Service B!"}
```

This response indicates that `service_a` successfully communicated with `service_b` over the Unix Domain Socket.

## Troubleshooting

If you encounter issues, here are some tips:

1. **Error: `Error loading ASGI app. Could not import module "main"`**:
   - Verify that `main.py` is correctly located in `/app` and that the `WORKDIR` is set to `/app` in the Dockerfile.

2. **Error: `httpx.UnsupportedProtocol: Request URL has an unsupported protocol 'http+unix://'`**:
   - Ensure `httpx.AsyncHTTPTransport(uds="/tmp/service_b.sock")` is used, and the URL format is `http://service_b/data`, without the `http+unix://` scheme.

## Summary

In this project:

- We set up two FastAPI services (`service_a` and `service_b`).
- Configured `service_a` to communicate with `service_b` over a Unix Domain Socket within Docker.
- Used `httpx` with `AsyncHTTPTransport` for efficient UDS-based requests.

Using Unix Domain Sockets with Docker and FastAPI is a powerful way to optimize local service communication, reducing network overhead and improving security. This setup is ideal for high-performance, local microservices architectures.
