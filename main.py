import gradio as gr
import difflib

# Predefined Q&A knowledge base
qa_data = {
    "What does the eligibility verification agent (EVA) do?": 
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?": 
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?": 
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.": 
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?": 
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

def thoughtful_agent(user_input):
    questions = list(qa_data.keys())
    # Match the user input to the closest known question
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if match:
        return qa_data[match[0]]
    else:
        # Fallback generic response
        return "I'm still learning! For now, I can answer questions about Thoughtful AI's agents. Please ask me something related to EVA, CAM, or PHIL."

# Gradio UI
gr.Interface(
    fn=thoughtful_agent,
    inputs=gr.Textbox(lines=2, placeholder="Ask me about Thoughtful AI..."),
    outputs="text",
    title="Thoughtful AI Support Agent"
).launch()
