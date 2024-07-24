import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
data_path = '/mnt/data/202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(data_path, encoding='cp949')  # Adjust encoding if necessary
# Assuming middle school age group is 13-15 years old (modify as necessary based on actual data)
middle_school_age = ['13세', '14세', '15세']
def prepare_data(region):
    region_data = data[data['행정구역'] == region]
    middle_school_data = region_data[middle_school_age].sum()
    total_population = region_data.drop(columns=['행정구역']).sum()
    other_population = total_population - middle_school_data.sum()
    
    return middle_school_data, other_population
st.title('중학생 인구 비율')
regions = data['행정구역'].unique()
selected_region = st.selectbox('지역을 선택하세요:', regions)
middle_school_data, other_population = prepare_data(selected_region)

# Data for pie chart
labels = middle_school_age + ['기타']
sizes = middle_school_data.tolist() + [other_population]

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display chart
st.pyplot(fig)
