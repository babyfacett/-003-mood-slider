import streamlit as st


def main():
    """App that uses a slider to display a message based on the user's mood."""
    st.title("今日の気分スライダー")
    st.write("スライダーを動かして今の気分を教えてください（1: 悪い〜5: とても良い）。")

    # Slider to capture mood between 1 and 5
    mood = st.slider("今日の気分を選んでください", 1, 5, 3)

    # Determine message based on mood value
    if mood <= 2:
        message = "お疲れですね。ゆっくり休みましょう。"
    elif mood == 3 or mood == 4:
        message = "ほどほどの気分ですね。今日も頑張りましょう！"
    else:
        message = "最高の気分ですね！その調子をキープしましょう！"

    # Display current mood and message
    st.write(f"あなたの気分：{mood}")
    st.success(message)


if __name__ == "__main__":
    main()