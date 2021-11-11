# import the streamlit library
import streamlit as st
import pandas as pd
#set background
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://previews.123rf.com/images/maximillion/maximillion1403/maximillion140300032/26351019-background-abstract-triangle-geometry-pattern-cloud-application.jpg");
  background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
#read excel file
df = pd.read_excel('Random.xlsx')
df.drop_duplicates(subset ="METER_NUMBER", inplace = True)
df = df.rename(columns={"LAT":"lat", "LON":"lon"})
# give a title to our app
st.title('Welcome to Meter Locator')
# take meter number
mtr_no = st.text_input("Enter the meter number:")
# search button
if(st.button('Search')):
    if df["METER_NUMBER"].str.contains(mtr_no).any():
        lat_lon = df[['lat','lon']][(df["METER_NUMBER"] == mtr_no)]
        plus_code = df['PLUS_CODE'][(df["METER_NUMBER"] == mtr_no)]
        plus_code = plus_code.to_string()
        # print the meter number
        st.write("The location of meter number", mtr_no, "is at the plus code", plus_code[5:],"given in the map below.")
        map_data = lat_lon[["lat", "lon"]]
        st.map(map_data)
    elif mtr_no == '':
        st.write("Blank meter number is not allowed. Kindly provide valid meter number.")
    else:
        st.write("The meter number", mtr_no,"is invalid or currently not available in the latest database. Kindly provide valid meter number.")
