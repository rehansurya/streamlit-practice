import streamlit as st
import sqlite3
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Setup database connection
engine = create_engine('sqlite:///blog_questionnaire.db')
meta = MetaData()

# Define the table structure
questionnaire = Table(
    'questionnaire', meta,
    Column('id', Integer, primary_key=True),
    Column('question', String),
    Column('answer', String),
)

# Create the table if it doesn't exist
meta.create_all(engine)

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

# Store the answers in a dictionary
answers = {}

# Create input fields for each question
for i, question in enumerate(questions):
    answers[i] = st.text_area(question)

# Submit button
if st.button("Submit"):
    # Validate that all questions are answered
    if all(answers[i] for i in range(len(questions))):
        # Connect to the database
        with engine.connect() as connection:
            # Insert each question and answer into the database
            for i in range(len(questions)):
                ins = questionnaire.insert().values(question=questions[i], answer=answers[i])
                connection.execute(ins)
        
        st.success("Answers submitted successfully and stored in the database!")
    else:
        st.warning("Please answer all the questions before submitting.")
