import streamlit as st

# Page 1: Blog Questionnaire
def questionnaire_page():
    st.title('Blog Questionnaire for SEO')
    st.markdown('#### Understanding the Company’s Vision and Goals')

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

    # Store the answers in session state
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    # Create input fields for each question
    for i, question in enumerate(questions):
        st.session_state.answers[i] = st.text_area(question, value=st.session_state.answers.get(i, ""))

    # Submit button
    if st.button("Submit"):
        # Validate that all questions are answered
        if all(st.session_state.answers[i] for i in range(len(questions))):
            st.success("Answers submitted successfully! You can view them on the 'View Submissions' page.")
        else:
            st.warning("Please answer all the questions before submitting.")

# Page 2: View Submissions
def view_submissions_page():
    st.title("View Submitted Answers")

    if 'answers' not in st.session_state or not st.session_state.answers:
        st.warning("No answers have been submitted yet.")
    else:
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

        for i, question in enumerate(questions):
            st.markdown(f"**{question}**")
            st.markdown(f"{st.session_state.answers.get(i, 'No answer provided')}")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Questionnaire", "View Submissions"])

if page == "Questionnaire":
    questionnaire_page()
elif page == "View Submissions":
    view_submissions_page()
