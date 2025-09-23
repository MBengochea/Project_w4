import streamlit as st
import pandas as pd
boardgames_df = pd.read_csv("../data/clean/boardgames_df_cleaned.csv")



def recommendation_boardgames(boardgames_df):
    # Get user preferences and convert to integers
    playtime = int(input('Please enter the number of minutes you wish to play: '))
    number_players = int(input('Please enter the number of players: '))
    min_age = int(input('Please enter the age of the youngest player: '))
    complexity = float(int(input('Please enter the difficulty level you wish for the game from 1 to 4 (1 - Easy; 2 - Medium; 3 - Hard; 4 - Very Hard): ')))

    # Filter the dataframe using conditions
    filtered_df = boardgames_df[
        (boardgames_df['min_playtime'] <= playtime) &
        (boardgames_df['max_playtime'] <= playtime) &
        (boardgames_df['min_players'] <= number_players) &
        (boardgames_df['max_players'] >= number_players) &
        (boardgames_df['minimum_age'] <= min_age) &
        (boardgames_df['complexity'] <= complexity+1) &
        (boardgames_df['complexity'] >= complexity)
    ]

    filtered_df_ranked = filtered_df.sort_values(by="avg_rating", ascending=False, inplace=False)

    result = filtered_df_ranked.head(5)
    
    return result

recommendation_boardgames(boardgames_df)

