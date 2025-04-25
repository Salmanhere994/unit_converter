import streamlit as st
import random

def evaluate_password_strength(password):
    """
    Evaluates the strength of a password based on defined criteria.
    
    Args:
        password (str): The password to evaluate.
    
    Returns:
        tuple: (score, strength, message) where score is an integer (0-5),
               strength is "Weak", "Moderate", or "Strong", and message is feedback.
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Make it at least 8 characters long.")
    
    # Check for uppercase and lowercase
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    if has_upper and has_lower:
        score += 1
    else:
        if not has_upper:
            feedback.append("Include at least one uppercase letter.")
        if not has_lower:
            feedback.append("Include at least one lowercase letter.")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Check for special characters
    special_chars = "!@#$%^&*"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    # Generate feedback message
    if len(password) == 0:
        message = "Password cannot be empty."
    elif strength == "Strong":
        message = "Your password is strong."
    else:
        message = f"Your password is {strength}. " + " ".join(feedback)
    
    return score, strength, message

def generate_strong_password(length=12):
    """
    Generates a strong random password meeting all criteria.
    
    Args:
        length (int): Desired password length (minimum 4).
    
    Returns:
        str: A strong password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Define character sets
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^&*'
    
    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill remaining length with random characters
    all_chars = uppercase + lowercase + digits + special
    password += [random.choice(all_chars) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# Streamlit Application
st.title("Password Strength Meter")
st.write("Check the strength of your password or generate a strong one.")

# Password input
password = st.text_input("Enter your password:", type="password")

# Evaluate and display strength
if password:
    score, strength, message = evaluate_password_strength(password)
    if strength == "Strong":
        st.success(f"Strength: {strength}")
    elif strength == "Moderate":
        st.warning(f"Strength: {strength}")
    else:
        st.error(f"Strength: {strength}")
    st.write(message)
else:
    st.write("Please enter a password.")

# Generate strong password button
if st.button("Generate Strong Password"):
    suggested_password = generate_strong_password()
    st.write("Suggested Strong Password:")
    st.code(suggested_password)