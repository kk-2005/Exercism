def rows(row_count):
    # 1. Error Handling: Enforce the negative row check with the exact requested message
    if row_count < 0:
        raise ValueError("number of rows is negative")
        
    # 2. Base Cases
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    
    # 3. Recursive Step: Get all previous rows
    previous_rows = rows(row_count - 1)
    last_row = previous_rows[-1]
    
    # 4. Helper Function: Recursively construct the next row based on neighbor sums
    def make_next_row(idx, current_row):
        # Base case: When index equals the row length, the row is complete
        if idx == len(last_row) + 1:
            return current_row
            
        # Treat out-of-bounds positions (left and right) as 0
        left_val = last_row[idx - 1] if idx - 1 >= 0 else 0
        right_val = last_row[idx] if idx < len(last_row) else 0
        
        # Append the sum and move to the next index recursively
        return make_next_row(idx + 1, current_row + [left_val + right_val])
    
    # Generate the new row and append it to the accumulator matrix
    new_row = make_next_row(0, [])
    return previous_rows + [new_row]



