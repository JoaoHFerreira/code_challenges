# How to Run  
(TODO Add a diagram)
To start the application, use the following command:  

```bash
uv run main.py
```  

### What This Command Does  

1. **Creates the necessary tables** in the database.  
2. **Populates the `code_challenges` table** with available coding challenges.  
3. **Randomly selects a challenge and programming language**, then asks the user whether they want to accept it.  
   - This loop continues until the user accepts a challenge.  
   - Once accepted, the `challenges_tracker` table is updated, recording:  
     - The accepted challenge  
     - The start date  
     - The selected programming language  
4. **Handles challenge progression**:  
   - When the program starts, it first checks if the user has any ongoing challenges.  
     - If an open challenge exists, the user is asked whether they have finished it.  
     - If the user confirms (`y`), the challenge is marked as completed:  
       - The completion time is recorded.  
       - The `is_done` field is set to `true`.  
     - If the user has not finished, the end date is recorded, but `is_done` remains `false`.  
   - When a new challenge is selected, a new tracking entry is created.  
