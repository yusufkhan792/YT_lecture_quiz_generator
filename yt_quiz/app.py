import streamlit as st
from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.quizgen import generate_quiz
from utils.summarizer import summarize_text

st.set_page_config(page_title="YouTube Lecture Quiz Generator", layout="wide")
st.title("🎥 YouTube Lecture → Transcript & Quiz Generator")

# Cache transcription results
@st.cache_data
def get_transcript(youtube_url):
    audio_file = download_audio(youtube_url)
    transcript = transcribe_audio(audio_file)
    return transcript

youtube_url = st.text_input("Enter YouTube video link:")

if st.button("Process"):
    if not youtube_url:
        st.error("Please enter a valid YouTube link.")
    else:
        with st.spinner("Processing..."):
            transcript = get_transcript(youtube_url)

        st.session_state.transcript = transcript
        st.session_state.summary = summarize_text(transcript)
        st.session_state.quiz = generate_quiz(transcript, num_questions=5)

# Show results if they exist
if "transcript" in st.session_state:
    st.subheader("Transcript")
    st.write(st.session_state.transcript[:1000] + "...")

    st.subheader("Summary")
    st.write(st.session_state.summary)

    st.subheader("Quiz")
    if "quiz" in st.session_state:
        for i, q in enumerate(st.session_state.quiz):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.radio(
                f"Select answer for Q{i+1}",
                q["options"],
                key=f"q{i}"  # stored in session_state
            )

        # Final submit button
        if st.button("Submit Quiz"):
            score = 0
            for i, q in enumerate(st.session_state.quiz):
                if st.session_state.get(f"q{i}") == q["answer"]:
                    score += 1
            st.success(f"✅ Your Score: {score}/{len(st.session_state.quiz)}")