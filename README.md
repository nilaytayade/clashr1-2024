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
         "username": "some_username",
         "question_id": 1,
         "selected_option": "Option A"
     }
     ```

3. **User Registration View Test Case:**
   - Endpoint: `/register/`
   - Method: `POST`
     ```json
     {
         "username": "new_user",
         "password": "some_password",
         "email": "new_user@example.com"
     }
     ```

4. **Token Obtain Pair View Test Case:**
   - Endpoint: `/token/`
   - Method: `POST`
     ```json
     {
         "username": "existing_user",
         "password": "user_password"
     }
     ```
