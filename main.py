import streamlit as st
from PIL import Image
import io
import base64

# Title of the page
st.title("GPTCache multi-modality demo")

# File uploader widget to upload an image
file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image with a specific width
if file is not None:
    # Open the image using PIL
    image = Image.open(file)

    # Get the width of the uploaded image
    width, height = image.size

    # Specify the desired width for the displayed image
    desired_width = 500

    # Calculate the height of the displayed image based on the desired width
    desired_height = int(height * desired_width / width)

    # Resize the image to the desired size
    resized_image = image.resize((desired_width, desired_height))

    img_bytes = io.BytesIO()
    resized_image.save(img_bytes, format='PNG')
    img_str = base64.b64encode(img_bytes.getvalue()).decode()

    # Center the image horizontally using CSS styling
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{img_str}" alt="Uploaded Image" width="{desired_width}"></div>',
        unsafe_allow_html=True
    )
    # Center the image horizontally using CSS styling
    
    # Add a text input widget below the image
    text_input = st.text_input("question:")

    # Show the input text below the image
    st.write("answer:", text_input)
