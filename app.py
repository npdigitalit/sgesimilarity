import streamlit as st
from rouge import Rouge

def compute_similarity_score(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference, avg=True)
    # Extracting the F1 score of ROUGE-L for similarity
    similarity_score = scores['rouge-l']['f']
    return similarity_score

# Streamlit UI
st.title('SGE Similarity calculator')
st.write('This app calculates similarity score between two pieces of text.')

# Textarea for input
hypothesis = st.text_area("Enter Ai Result")
reference = st.text_area("Enter Your Content")

# Compute and display the similarity score
if st.button('Compute Similarity'):
    similarity = compute_similarity_score(hypothesis, reference)
    st.write(f"Similarity Score: {similarity:.2f}")

