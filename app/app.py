import streamlit as st
import pandas as pd

# --- Load your dataset ---
boardgames_df = pd.read_csv("boardgames_df_cleaned.csv")

# --- Streamlit UI ---
st.title("🎲 Board Game Recommender")
st.write("Find the best board games for your session based on your preferences.")

# --- User Inputs ---
playtime = st.slider("⏱️ Desired playtime (minutes)", 15, 180, 45)
number_players = st.slider("👥 Number of players", 1, 10, 3)
min_age = st.slider("🧒 Age of youngest player", 5, 18, 10)
difficulty_level = st.selectbox("🧠 Desired difficulty level", [1, 2, 3, 4], format_func=lambda x: ["Easy", "Medium", "Hard", "Very Hard"][x-1])
complexity = float(difficulty_level)

# --- Filter Logic ---
filtered_df = boardgames_df[
    (boardgames_df['min_playtime'] <= playtime) &
    (boardgames_df['max_playtime'] <= playtime) &
    (boardgames_df['min_players'] <= number_players) &
    (boardgames_df['max_players'] >= number_players) &
    (boardgames_df['minimum_age'] <= min_age) &
    (boardgames_df['complexity'] <= complexity + 1) &
    (boardgames_df['complexity'] >= complexity)
]

filtered_df_ranked = filtered_df.sort_values(by="avg_rating", ascending=False)

# --- Display Results ---
if filtered_df_ranked.empty:
    st.warning("⚠️ No games match all criteria. Try relaxing one or more inputs.")
else:
    st.subheader("🔥 Top 5 Matching Games")
    st.dataframe(filtered_df_ranked[['boardgame', 'avg_rating', 'min_players', 'max_players', 'min_playtime', 'max_playtime', 'minimum_age', 'complexity']].head(5))
