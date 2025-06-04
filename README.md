# Employee Leave Request Management System

A simple Python-based REST API for managing employee leave requests built with Flask.

## Features

- Create new leave requests
- Retrieve leave requests by employee ID
- Update existing leave requests
- Delete leave requests
- In-memory storage for quick development and testing

## API Endpoints

### Create Leave Request
```
POST /leave_request
```

**Request Body:**
```json
{
    "employee_id": 123,
    "start_date": "2024-07-01",
    "end_date": "2024-07-05",
    "leave_type": "vacation",
    "reason": "Family vacation"
}
```

**Response:**
- `201 Created` - Leave request created successfully
- `400 Bad Request` - Missing required fields

### Get Leave Request
```
GET /leave_request/<employee_id>
```

**Response:**
- `200 OK` - Returns leave request details
- `404 Not Found` - Leave request not found

**Example Response:**
```json
{
    "employee_id": 123,
    "start_date": "2024-07-01",
    "end_date": "2024-07-05",
    "leave_type": "vacation",
    "reason": "Family vacation"
}
```

### Update Leave Request
```
PUT /leave_request/<employee_id>
```

**Request Body:**
```json
{
    "start_date": "2024-07-02",
    "end_date": "2024-07-06",
    "leave_type": "vacation",
    "reason": "Extended family vacation"
}
```

**Response:**
- `200 OK` - Leave request updated successfully
- `401 Unauthorized` - Leave request not found
- `500 Internal Server Error` - Missing required fields

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employee-leave-request
```

2. Install required dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Usage Examples

### Create a leave request
```bash
curl -X POST http://localhost:5000/leave_request \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": 123,
    "start_date": "2024-07-01",
    "end_date": "2024-07-05",
    "leave_type": "sick",
    "reason": "Medical appointment"
  }'
```

### Get a leave request
```bash
curl http://localhost:5000/leave_request/123
```

### Update a leave request
```bash
curl -X PUT http://localhost:5000/leave_request/123 \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2024-07-02",
    "end_date": "2024-07-06",
    "leave_type": "vacation",
    "reason": "Extended vacation"
  }'
```

## Data Structure

### EmployeeLeaveRequest
- `employee_id` (int): Unique identifier for the employee
- `start_date` (string): Leave start date (YYYY-MM-DD format)
- `end_date` (string): Leave end date (YYYY-MM-DD format)
- `leave_type` (string): Type of leave (e.g., "vacation", "sick", "personal")
- `reason` (string): Reason for the leave request

## Project Structure

```
employee-leave-request/
├── app.py                 # Main Flask application
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Known Issues & Limitations

1. **In-memory storage**: Data is lost when the application restarts
2. **Single employee limit**: Current implementation stores only one leave request per employee
3. **No authentication**: API endpoints are not secured
4. **Limited validation**: Minimal input validation and error handling
5. **Missing endpoints**: No endpoint to get all leave requests or delete requests

## Future Enhancements

- [ ] Add database persistence (SQLite/PostgreSQL)
- [ ] Implement user authentication and authorization
- [ ] Add input validation for dates and employee IDs
- [ ] Support multiple leave requests per employee
- [ ] Add endpoints for listing all requests and deleting requests
- [ ] Implement leave request approval workflow
- [ ] Add unit tests
- [ ] Add logging and monitoring
- [ ] Implement date range validation
- [ ] Add leave balance tracking

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue in the GitHub repository.A RESTful API service for managing Employee Leave Requests. The service should handle leave request creation with validation rules and retrieval of leave requests.
