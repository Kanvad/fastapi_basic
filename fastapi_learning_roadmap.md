# FastAPI Learning Roadmap

> Mục tiêu: xây một RESTful Task API bằng FastAPI theo hướng có cấu trúc, dễ mở rộng và gần với project thực tế.

## 1. FastAPI Fundamentals

- FastAPI app và routing
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Path parameters
- Query parameters
- Request body
- Swagger UI / OpenAPI

## 2. Pydantic & Data Validation

- `BaseModel`
- Required / Optional fields
- `Field`
- Kiểu dữ liệu và validation
- Request schema và response schema
- `response_model`

## 3. REST API Design

- Resource-based URL
- CRUD design
- HTTP status codes
- `HTTPException`
- PUT vs PATCH
- API response cơ bản

## 4. Project Structure

- Tách `main.py`
- Tách `schemas.py`
- Tách dữ liệu khỏi router
- `APIRouter`
- Router `prefix`
- Router `tags`
- Chia module theo resource

## 5. Dependency Injection

- `Depends`
- Dependency function
- Dùng dependency để tái sử dụng logic
- Dependency cho resource lookup
- Dependency có nhiều tầng

## 6. Database

- Vì sao in-memory list không phù hợp cho project thật
- SQL và relational database cơ bản
- SQLAlchemy / SQLModel
- Model và schema khác nhau
- CRUD với database
- Session và transaction
- Migration với Alembic

## 7. API Error Handling

- Chuẩn hóa lỗi
- Custom exception
- Exception handler
- Validation error
- Response format cho lỗi

## 8. Authentication & Authorization

- Authentication vs Authorization
- Password hashing
- Login / register
- JWT
- OAuth2 trong FastAPI
- Protected endpoints
- User ownership của resource

## 9. Testing

- Test API với `pytest`
- FastAPI `TestClient`
- Test CRUD
- Test validation
- Test authentication
- Test error cases

## 10. Async & Performance

- `async` / `await`
- Khi nào cần async
- Async database access
- Blocking vs non-blocking code
- Những lỗi phổ biến khi dùng async

## 11. Configuration & Environment

- Environment variables
- `.env`
- Settings management
- Development / production configuration
- Secret management cơ bản

## 12. Middleware & API Features

- Middleware
- CORS
- Request logging
- Pagination
- Filtering
- Sorting
- API versioning cơ bản

## 13. Background Tasks & External Services

- Background tasks
- Gửi email / xử lý tác vụ ngoài request
- Gọi external API
- Timeout và retry cơ bản

## 14. Deployment

- Uvicorn và production server
- Docker
- Database trong production
- Reverse proxy cơ bản
- Environment configuration
- Health check

## 15. Project hoàn chỉnh

Xây một API hoàn chỉnh thay cho Task API demo, có:

- User
- Authentication
- CRUD resource
- Database
- Validation
- Error handling
- Testing
- Docker
- API documentation

