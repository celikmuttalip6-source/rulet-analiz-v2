import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Rulet Analiz", layout="centered")

st.title("🎰 Rulet Analiz Uygulaması")

st.write("Çıkan sayıları buraya gir, sistem analiz etsin.")

# Girilen sayılar bellekte tutulsun
if "results" not in st.session_state:
    st.session_state["results"] = []

# Yeni sayı girme alanı
new_num = st.number_input("Yeni çıkan sayıyı gir (0-36)", min_value=0, max_value=36, step=1)

if st.button("➕ Ekle"):
    st.session_state["results"].append(new_num)
    st.success(f"{new_num} listeye eklendi!")

# Liste boş değilse analiz yap
if st.session_state["results"]:
    results = st.session_state["results"]

    st.subheader("Girilen Sayılar:")
    st.write(results)

    # Frekans hesapla
    counts = {i: results.count(i) for i in range(37)}
    top_numbers = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]

    st.subheader("En çok çıkan 5 sayı:")
    for num, freq in top_numbers:
        st.write(f"🎲 {num}: {freq} kez")

    # Histogram çiz
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values())
    ax.set_xlabel("Sayı")
    ax.set_ylabel("Frekans")
    ax.set_title("Rulet Sonuç Dağılımı")
    st.pyplot(fig)

