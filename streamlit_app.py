import streamlit as st

st.title('Blog Questionnaire for SEO')

st.markdown('Understanding the Company’s Vision and Goals')

# List of predefined questions
questions = [
    "Question 1: What is the name of the blog and short description about the context of the blog's topic?",
    "Question 2: What is the primary goal and KPIs that you hope to achieve after publishing this blog?",
    "Question 3: Who is your target audience, and what are their key demographics?",
    "Question 4: How do you want your brand to be perceived by your audience?",
    "Question 5: What are the unique selling points (USPs) of your products or services?",
]

# Store the answers in a dictionary
answers = {}

# Create input fields for each question
for i, question in enumerate(questions):
    answers[i] = st.text_area(question)


st.markdown('Content Focus and SEO Strategy')

# List of predefined questions
questions = [
    "Question 6: What is the name of the blog and short description about the context of the blog's topic?",
    "Question 7: What is the primary goal and KPIs that you hope to achieve after publishing this blog?",
    "Question 8: Who is your target audience, and what are their key demographics?",
    "Question 9: How do you want your brand to be perceived by your audience?",
    "Question 10: What are the unique selling points (USPs) of your products or services?",
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
        email_content = "\n".join([f"{questions[i]} {answers[i]}" for i in range(len(questions))])
        msg = MIMEText(email_content)
        msg["Subject"] = "Submitted Answers"
        msg["From"] = "abdulrahmanjanoo@gmail.com"
        msg["To"] = "rehansurya111@gmail.com"

        # Mailchimp SMTP server details
        smtp_server = "smtp.mandrillapp.com"
        smtp_port = 587
        smtp_user = "rehansurya"
        smtp_password = "md-SPlEbWybdGKJETx6--60OA"

        # Send email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            st.success("Answers submitted successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.warning("Please answer all the questions before submitting.")
