# Password Strength Checker

This project is a simple **Password Strength Checker** built using Python and **Streamlit**. It evaluates the strength of a password based on various criteria, such as length, presence of uppercase and lowercase letters, digits, and special characters, and provides real-time feedback on the password's strength.

## Features

- **Real-time Password Assessment**: As you type a password, the tool dynamically evaluates and provides feedback on its strength.
- **Criteria for Strength**:
  - Password length (minimum 8 characters)
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
  - Contains at least one special character (e.g., `!@#$%^&*`)
- **Password Strength Levels**:
  - **Very Weak**
  - **Weak**
  - **Medium**
  - **Strong**
  - **Very Strong**
- **Progress Bar Visualization**: The password strength is visually represented as a progress bar.
- **Improvement Suggestions**: If the password is not strong enough, the tool provides suggestions for improving it.

## How It Works

1. **Password Input**: The user enters a password in the input field.
2. **Password Strength Check**: The tool evaluates the password against the following criteria:
   - Length of the password
   - Presence of uppercase and lowercase letters
   - Presence of digits
   - Presence of special characters
3. **Feedback**: Based on the score (out of 5), the tool provides feedback on the password strength (Very Weak, Weak, Medium, Strong, Very Strong) and displays a progress bar.
4. **Improvement Suggestions**: If the password does not meet the highest criteria, suggestions for improvement are displayed to help users create stronger passwords.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run password.py
   ```

2. Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).

3. Enter a password in the input field and receive instant feedback on its strength.

## Screenshots

![WhatsApp Image 2024-09-19 at 1 21 44 AM](https://github.com/user-attachments/assets/132b2e13-f1bb-4723-93a1-1abc07b4c149)
![WhatsApp Image 2024-09-19 at 1 21 43 AM](https://github.com/user-attachments/assets/e137f93d-5ffa-40e5-aa5c-1a236e132479)

## Contributing

Feel free to fork this repository and make contributions! Pull requests are welcome.

## License

This project is licensed under the MIT License.
