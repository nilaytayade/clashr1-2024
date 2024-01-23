1. **MCQ View Test Case:**
   - Endpoint: `/mcq/`
   - Method: `GET`
     ```json
     {
         "username": "some_username"
     }
     ```

2. **Submit View Test Case:**
   - Endpoint: `/submit/`
   - Method: `POST`
     ```json
     {
         "username": "new_user",
         "question_id": 1,
         "selected_option": "A"
     }
     ```

3. **User Registration View Test Case:**
   - Endpoint: `/register/`
   - Method: `POST`
     ```json
     {
         "username": "new_user",
         "password": "some_password",
         "email": "new_user@example.com",
         "first_name": "First",
         "last_name": "Last"
     }
     ```

4. **Token Obtain Pair View Test Case:**
   - Endpoint: `/token/`
   - Method: `POST`
     ```json
     {
         "username": "new_user",
         "password": "some_password"
     }
     ```
