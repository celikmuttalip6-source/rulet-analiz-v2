import streamlit as st
import random
from collections import Counter

st.title("🎰 Rulet Analiz Uygulaması")

st.markdown("Son çıkan sayıları gir (virgülle ayır, örn: `10, 23, 7, 0, 15`)")

# Kullanıcıdan sayılar al
user_input = st.text_input("Son çıkan sayılar:")

if user_input:
    try:
        # Sayıları listeye çevir
        numbers = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]
        
        if numbers:
            st.success(f"Girilen {len(numbers)} sayı: {numbers}")

            # En çok çıkan sayılar
            counts = Counter(numbers)
            most_common = counts.most_common(5)

            st.subheader("📊 En çok çıkan sayılar")
            for num, cnt in most_common:
                st.write(f"🎲 {num}: {cnt} kez")

            # Tahmin: en çok çıkan 3 sayı
            predictions = [num for num, _ in most_common[:3]]
            st.subheader("🔮 Tahmin Edilen Sayılar")
            st.write(", ".join(map(str, predictions)))
        else:
            st.warning("Geçerli sayı girilmedi.")
    except Exception as e:
        st.error(f"Hata: {e}")

st.markdown("---")
st.caption("Bu sadece istatistik analizdir, kesin sonuç vermez ⚠️")
