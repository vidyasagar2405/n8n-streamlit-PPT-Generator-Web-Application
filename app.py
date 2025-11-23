import streamlit as st
import requests
import subprocess
#import os

st.title(":rainbow[PPT GENERATOR]")
st.subheader("Can generate your PPT easily using Prompt")


prompt = st.text_area(
    "Please write the details about the ppt in the text box area",
    placeholder="'Describe what your PPT should contain' and 'how the format should look' for better results."
)

url = "https://sagardesktopn8n.app.n8n.cloud/webhook-test/d8cbac37-740a-464b-82a4-0066afa8b0eb"

ppt_path = "/Users/vidyasagar/Desktop/DataScience/INNOMATICS/vs code/PowerPoint project using n8n+streamlit+vscode/powerpoint/new_ppt.pptx"

if st.button(":blue[Generate PPT]") :
    if prompt :
        response = requests.post(url,
         json = {"prompt" : prompt})

        if response.status_code == 200:
            st.write("Success")

            with open("ppt_code.py","w") as file :
                file.write(response.json()[0]["output"].strip("```python"))

            subprocess.run(["python","ppt_code.py"])


#if os.path.exists(ppt_path) :
            with open(ppt_path,"rb") as ppt:
                    st.download_button(
                    label=":blue[⏬ Download PPT]",
                    data = ppt,
                    file_name="New ppt.pptx",
                    )