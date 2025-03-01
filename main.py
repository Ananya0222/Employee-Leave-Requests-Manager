leave_requests = []
class EmployeeLeaveRequest:
    def __init__(self, employee_id, start_date, end_date, leave_type, reason):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.leave_type = leave_type
        self.reason = reason
    def to_dict(self):
        return{
            'employee_id': self.employee_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'leave_type': self.leave_type,
            'reason': self.reason
            
        }
        
class LeaveRequestManager:
    def __init__(self):
        self.leave_requests = {}
    def add_request(self, leave_request): 
        self.leave_requests[leave_request.employee_id] = leave_request
    def get_request(self, employee_id):
        return self.leave_requests.get(employee_id)
    def get_all_requests(self):
        return [leave_request.to_dict() for leave_request in self.leave_requests.values()]
        
    def delete_request(self, employee_id):
        if employee_id in self.leave_requests : 
            del self.leave_requests[employee_id]
            return True
        return False
        
    def update_request(self, employee_id, updated_leave_request):
        if employee_id in self.leave_requests:
            self.leave_requests[employee_id] = updated_leave_request
            return True
        return False
        
leave_request_manager = LeaveRequestManager()
#@app.route('leave_request', methods=['POST'])
def create_leave_request():
    data = request.get_json()
        
    if not data or not all (k in data for k in ("employee_id","start_date", "end_date", "leave_type", "reason" )):
            return jsonify({"message": "Required Feilds are Missing "}), 400
    
    leave_request = EmployeeLeaveRequest(
            employee_id = data['employee_id'],
            start_date = data['start_date'],
            end_date = data['end_date'], 
            leave_type = data['leave_type'], 
            reason = data ['reason'])
            
    leave_request_manager.add_request(leave_request)
    return jsonify(leave_request.to_dict()), 201
        
#@app.route('/leave_request/<int:employee_id>', methods=['GET'])
def get_leave_requests(employee_id):
        leave_request = leave_request_manager.get_request(employee_id)
        if leave_request:
            return jsonify(leave_request.to_dict())
        return jsonify({"message": "Leave request not found"}), 404
#@app.route('/leave_request/<int:employee_id>', methods=['PUT'])
def update_leave_request(employee_id):
    data = request.get_json()
    if not data or not all(k in data for k in ("start_date","end_date", "reason")):
        return jsonify({"message": "Missing required feilds"}), 500
    updated_leave_request = EmployeeLeaveRequest(employee_id = employee_id,
        start_date = data['start_date'],
        end_date = data['end_date'], 
        leave_type = data['leave_type'], 
        reason = data ['reason'])
    if leave_request_manager.update_request(employee_id, updated_leave_request):
        return jsonify(updated_leave_request.to_dict())
    return jsonify({"message": "No leave request found"}), 401