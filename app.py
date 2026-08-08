import streamlit as st

# Configure page layout for mobile scanning
st.set_page_config(page_title="UK49s Code Matrix", page_icon="🎰", layout="centered")

st.title("🎰 UK49s Matrix System")
st.caption("Algorithmically generated lines optimized for mobile screens.")

# User Input Form
user_code = st.text_input("📱 Enter 4-Digit Code:", max_chars=4, placeholder="e.g., 6664")

if user_code and len(user_code) == 4 and user_code.isdigit():
    # Parse individual digits
    d1, d2, d3, d4 = map(int, user_code)
    code_sum = d1 + d2 + d3 + d4
    
    # Mathematical Pair Variables
    pair1 = int(user_code[0:2])  # e.g., 66 or 94
    pair2 = int(user_code[2:4])  # e.g., 64 or 13
    pair3 = int(user_code[1:3])  # e.g., 66 or 41

    # Apply Matrix Subtraction Rule if pairs exceed lottery cap (49)
    p1_reduced = pair1 - 49 if pair1 > 49 else pair1
    p2_reduced = pair2 - 49 if pair2 > 49 else pair2
    p3_reduced = pair3 - 49 if pair3 > 49 else pair3

    # Multipliers
    m1 = (d1 * d2) if (d1 * d2) <= 49 else (d1 * d2) - 49
    m2 = (d3 * d4) if (d3 * d4) <= 49 else (d3 * d4) - 49
    m3 = (d1 * d4) if (d1 * d4) <= 49 else (d1 * d4) - 49

    st.success(f"✅ Code Processed. Root Sum Vector: {code_sum}")

    # Tabs for clean mobile navigation
    tab1, tab2, tab3 = st.tabs(["🔢 4-Ball Lines", "☘️ 3-Ball Triplets", "✌️ 2-Ball Pairs"])

    with tab1:
        st.subheader("Optimized 4-Number Slips")
        # Line 1: Family Split Strategy
        line1 = sorted(list(set([d1 if d1>0 else 49, d1+10, d2+20, d4+40 if d4+40<=49 else 46])))
        # Line 2: Grid Reduction Strategy
        line2 = sorted(list(set([abs(pair1-pair2) if abs(pair1-pair2)>0 else 2, p2_reduced, p1_reduced, code_sum])))
        # Line 3: Cross Product Strategy
        line3 = sorted(list(set([m1 if m1>0 else 6, m2 if m2>0 else 18, m3 if m3>0 else 24, 40])))
        
        st.code(f"Line 1: {line1}")
        st.code(f"Line 2: {line2}")
        st.code(f"Line 3: {line3}")

    with tab2:
        st.subheader("Optimized 3-Number Slips")
        st.code(f"Triplet 1: {[d1 if d1>0 else 7, p2_reduced, m1 if m1>0 else 27]}")
        st.code(f"Triplet 2: {[d2 if d2>0 else 9, d3+10, 40]}")
        st.code(f"Triplet 3: {[p3_reduced if p3_reduced > 0 else 14, d4+20, 41]}")

    with tab3:
        st.subheader("High-Probability 2-Ball Pairs")
        st.write(f"**Base Twin:** {d1 if d1>0 else 9} – {p2_reduced}")
        st.write(f"**Mirror Twin:** {p3_reduced if p3_reduced>0 else 14} – 41")
        st.write(f"**Boundary Split:** {m1 if m1>0 else 4} – 39")
        st.write(f"**Booster Tracker:** 08 – 28")

elif user_code:
    st.error("Please enter numbers only (4 digits).")
