import streamlit as st
import requests
import pandas as pd

# Function to upload file to FastAPI backend
def upload_file_to_fastapi(file):
    url = 'https://apnairesume.onrender.com/upload'
    files = {'resume': file}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error uploading file: {response.text}")
    except Exception as e:
        st.error(f"Error uploading file: {str(e)}")

def display_results_table(results):
    df = pd.DataFrame(results, columns=['Rank', 'Job Title', 'Company'])
    df_sorted = df.sort_values(by='Rank')
    st.write(df_sorted, index=False)

def main():
    st.title('Get your Resume Rank')
    st.write('Upload your resume in PDF format to get the score')

    uploaded_file = st.file_uploader("Choose a file", type=['pdf'])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write("Filename:", uploaded_file.name)

        if st.button('Get Ranks'):
            result = upload_file_to_fastapi(uploaded_file)
            res = []
            x = result['score']
            for i in x:
                temp = []
                temp.append(i['Rank'])
                temp.append(i['Role'])
                temp.append(i['Company'])
                res.append(temp)
            result = res
            print(result)
            if result:
                st.write("Result:")
                display_results_table(result)
            else:
                st.error("Failed to get score from server")

if __name__ == '__main__':
    main()
