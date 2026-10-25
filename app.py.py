import streamlit as st
import datetime

st.set_page_config(page_title="تتبع المزاج والإنتاجية", page_icon="🌟", layout="centered")

st.title("🌟 يومياتي: المزاج والإنتاجية")
st.write("سجل تفاصيل يومك، مزاجك، ومهامك اليومية لتبقى منظماً ومنتجاً!")

# تاريخ اليوم
today = datetime.date.today()
st.info(f"📅 تاريخ اليوم: {today}")

# 1. قسم تتبع المزاج
st.subheader("😊 كيف تشعر اليوم؟")
mood = st.selectbox("اختر حالتك المزاجية:", ["سعيد ورايق 🤩", "منجز ونشيط 💪", "هادي وعادي 😌", "متوتر أو مشغول 🫨", "مرهق وتعبان 😴"])

# 2. قسم تتبع المهام (Todo List)
st.subheader("✅ مهام اليوم")
task_1 = st.checkbox("إنجاز مهام العمل أو الدراسة الرئيسية")
task_2 = st.checkbox("ممارسة الرياضة أو المشي")
task_3 = st.checkbox("قراءة صفحة أو كتاب")
task_4 = st.checkbox("شرب كمية كافية من الماء")

# 3. ملاحظات اليوم
st.subheader("📝 ملاحظات أو خواطر سريعة")
notes = st.text_area("اكتب أي شي خطر ببالك اليوم:", placeholder="اكتب هنا...")

# زر الحفظ
if st.button("حفظ بيانات اليوم 💾"):
    st.success("تم تسجيل بيانات يومك بنجاح! بطل استمر كذا ✨")
    if notes:
        st.write(f"**ملاحظتك المحفوظة:** {notes}")