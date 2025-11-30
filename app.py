import streamlit as st

st.set_page_config(page_title="Тест подключения", layout="centered")

st.title("✅ Streamlit работает!")
st.success("Поздравляем! Приложение успешно запущено на Streamlit Cloud.")

st.markdown("""
### Что дальше?
1. Убедись, что файлы `app.py` и `requirements.txt` лежат в корне репозитория.
2. Убедись, что в `requirements.txt` указано:
