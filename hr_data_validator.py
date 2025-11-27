# CUSTOM MCP TOOL: Employee Data Validator 

def validate_employee_data(raw_name: str, raw_salary: float) -> dict:
    """
    A custom MCP tool to validate and standardize employee data.

    In a real scenario, this would be deployed as a microservice 
    or a packaged component within the MCP framework.
    """
    
    # 1. Standardization Logic (e.g. Title Case Name)
    standardized_name = raw_name.strip().title()

    # 2. Validation Logic (e.g., Check for minimum salary threshold)
    MIN_SALARY_USD = 40000.0
    is_valid_salary = raw_salary >= MIN_SALARY_USD
    
    # 3. Decision Logic
    validation_status = "PASS" if is_valid_salary else "FAIL - BELOW THRESHOLD"

    # 4. Return Structured Output (The tool's result payload)
    result = {
        "Name": standardized_name,
        "Original_Salary": raw_salary,
        "Validation_Status": validation_status,
        "Is_Valid": is_valid_salary,
        "Timestamp": '2025-11-27T12:00:00Z' # Placeholder for current time
    }
    
    return result


# SIMULATED MCP WORKFLOW

def run_mcp_workflow(employee_records):
    """
    Simulates a workflow where the MCP calls the custom tool for each record.
    """
    print("MCP Workflow Starting: Running Custom Data Validator Tool...")
    print("-" * 50)

    processed_results = []
    
    for record in employee_records:
        name = record.get('name')
        salary = record.get('salary')
        
        print(f"\nProcessing record for: **{name}** (Salary: ${salary:,.2f})")
        
        # 1. MCP LOGIC: Calling the Custom Tool
        # This is the core demonstration of reusability and integration.
        validation_output = validate_employee_data(name, salary)
        
        # 2. MCP LOGIC: Taking action based on tool output
        if validation_output["Is_Valid"]:
            action = "Forwarded to Onboarding System."
            print(f"Tool Output: Status **{validation_output['Validation_Status']}**. Action: {action}")
        else:
            action = "Stopped workflow. Requires HR Manager Review."
            print(f"Tool Output: Status **{validation_output['Validation_Status']}**. Action: {action}")
            
        processed_results.append(validation_output)

    print("-" * 50)
    print("MCP Workflow Complete.")
    return processed_results


# MAIN EXECUTION 
if __name__ == "__main__":
    
    # Simulate the raw input data the MCP receives
    raw_data_stream = [
        {'name': 'alice smith ', 'salary': 55000.00},  # Valid, needs cleaning
        {'name': 'bob jones', 'salary': 35000.00},   # Invalid (too low)
        {'name': 'CHarlie BROWN', 'salary': 105000.50},# Valid, needs cleaning
    ]

    final_report = run_mcp_workflow(raw_data_stream)
    
    print("\nSummary of Tool Execution Results")
    for res in final_report:
        print(f"- {res['Name']}: Status **{res['Validation_Status']}**")
        
