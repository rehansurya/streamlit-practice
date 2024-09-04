import streamlit as st
from email.mime.text import MIMEText
import smtplib
    
logo_url = "https://cdn.prod.website-files.com/654cf378c048081b445dcc67/6561f93907af8a7a9a45df15_logo-white.svg"  # Replace with the actual URL or file path of your logo
st.image(logo_url, width=220)
        
st.title('Blog Questionnaire for SEO')

# List of predefined questions
questions = [
    "What is the name of the blog and short description about the context of the blog's topic?",
    "What is the primary goal and KPIs that you hope to achieve after publishing this blog?",
    "Who is your target audience, and what are their key demographics?",
    "How do you want your brand to be perceived by your audience?",
    "What are the unique selling points (USPs) of your products or services?",
    "What keywords or phrases do you want to target for SEO?",
    "Who are your main competitors in the industry?",
    "Do you have any specific content ideas or angles you want to explore?",
    "What tone or voice should the blog have?",
    "Are there any specific calls to action (CTAs) you want to include?",
]

# Store the answers in a dictionary
answers = {}

# Create input fields for each question
for i, question in enumerate(questions):
    answers[i] = st.text_area(question)

# Submit button
if st.button("Submit"):
    # Validate that all questions are answered
    if all(answers[i] for i in range(len(questions))):
        # Prepare email content
        email_content = "\n".join([f"{questions[i]}: {answers[i]}" for i in range(len(questions))])
        msg = MIMEText(email_content)
        msg["Subject"] = "Tericsoft Blog Questionnaire Submitted Answers"
        msg["From"] = "abdulrahmanjanoo@gmail.com"
        msg["To"] = "rehansurya111@gmail.com"

        # Mailchimp SMTP server details
        smtp_server = "smtp.gmail.com"
        smtp_port = 465
        smtp_user = "rehansurya111@gmail.com"
        smtp_password = "pnczdvfhpsslazpw"  # Replace with your actual Mailchimp SMTP password

        # Send email
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            st.success("Answers submitted successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.warning("Please answer all the questions before submitting.")
