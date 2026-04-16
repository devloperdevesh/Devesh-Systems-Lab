## Components
- API Server
- Rate Limiter Service
- Redis (for shared state)

## Flow
Client → API → Rate Limiter → Redis → Allow/Deny