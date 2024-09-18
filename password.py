import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    # Criteria for password strength
    if len(password) >= 8:
        score += 1  # Length >= 8
    if re.search(r'[A-Z]', password):
        score += 1  # Has uppercase letters
    if re.search(r'[a-z]', password):
        score += 1  # Has lowercase letters
    if re.search(r'[0-9]', password):
        score += 1  # Has digits
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1  # Has special characters
    
    return score

# Password strength feedback based on the score
def password_feedback(score):
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:  
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Streamlit UI
def main():
    st.title("Password Strength Checker")
    
    # Input box for password
    password = st.text_input("Enter a password", type="password")
    
    if password:
        score = check_password_strength(password)
        feedback = password_feedback(score)
        
        # Display the score and feedback
        st.write(f"Password Strength: {feedback}")
        
        # Provide additional feedback
        st.progress(score/5, text=f"Strength Level: {feedback}")
        
        # Password improvement suggestions
        if score < 5:
            st.write("Suggestions to improve your password strength:")
            if len(password) < 8:
                st.write("- Make the password at least 8 characters long.")
            if not re.search(r'[A-Z]', password):
                st.write("- Include at least one uppercase letter.")
            if not re.search(r'[a-z]', password):
                st.write("- Include at least one lowercase letter.")
            if not re.search(r'[0-9]', password):
                st.write("- Include at least one number.")
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                st.write("- Include at least one special character.")
    
if __name__ == "__main__":
    main()


