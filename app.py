import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="CollegeBot Basic",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 CollegeBot Basic")
st.write("A simple keyword-based college inquiry bot. Ask me anything!")

# 2. Keyword-to-Response Matching
def get_response(user_input: str) -> str:
    """
    Matches user input against predefined keywords and returns the corresponding response.
    """
    text = user_input.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return "Hello! Welcome to CollegeBot. How can I help you?"

    elif "how are you" in text:
        return "I'm doing great, thanks for asking! 😊"

    elif "course" in text:
        return "We offer BCA, BSc Computer Science, BCom, MBA, and MSc Data Science."

    elif "fee" in text:
        return "Please contact the accounts office for detailed fee information."

    elif "admission" in text:
        return "Admissions are currently open. You can apply online or visit the admission office."

    elif "contact" in text:
        return "You can contact us at 9876543210 or email us at info@college.edu"

    elif "library" in text:
        return "The library is open from 9 AM to 5 PM on working days."

    elif "hostel" in text:
        return "Hostel facilities are available for both boys and girls."

    elif "placement" in text:
        return "Our placement cell conducts training and campus recruitment drives regularly."

    elif "scholarship" in text:
        return "Scholarships are available based on merit and eligibility criteria."

    elif "thank" in text:
        return "You're welcome! 😊"

    elif text == "bye":
        return "Goodbye! Have a great day. 👋"

    else:
        return "Sorry, I don't understand that. For more info, please contact the admission office."


# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 5. Handle User Input
if prompt := st.chat_input("Type your message here..."):

    # Show and store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate and store bot response
    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
