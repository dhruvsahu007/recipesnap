import streamlit as st
from PIL import Image
from detection import detect_with_caption
from recipe_generator import generate_recipe

st.set_page_config(page_title="RecipeSnap – AI Cooking Assistant", page_icon="📸")

st.title("📸 RecipeSnap – AI Cooking Assistant")
st.write("Snap a picture of your fridge or ingredients and get a recipe!")

# Upload image
uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Detect ingredients
    if 'ingredients' not in st.session_state:
        with st.spinner("Detecting ingredients..."):
            try:
                labels, caption = detect_with_caption(image)
                st.session_state.ingredients = labels
                st.session_state.caption = caption
                st.success("Detection complete!")
            except Exception as e:
                st.error(f"Detection failed: {e}")
                st.stop()

    st.write("🧾 **Caption:**", st.session_state.caption)
    st.write("🍅 **Detected Ingredients:**", ", ".join(st.session_state.ingredients))

    # Generate recipe
    if st.button("Generate Recipe"):
        with st.spinner("Generating recipe using Mistral..."):
            try:
                recipe = generate_recipe(st.session_state.ingredients)
                st.markdown("## 🥘 Suggested Recipe")
                st.markdown(f"```\n{recipe}\n```")
            except Exception as e:
                st.error(f"Recipe generation failed: {e}")
