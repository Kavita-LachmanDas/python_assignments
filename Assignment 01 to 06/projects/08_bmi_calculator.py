import streamlit as st
import numpy as np



def calculate_bmi(weight, height):
    """
    Calculate BMI and return category
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        tuple: (BMI value, BMI category)
    """

    bmi = weight / (height ** 2)
    
   
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 2), category

def main():
    # Set page configuration
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon=":hospital:",
        layout="centered"
    )
    
   
    st.title("🏋️ BMI Calculator")
    st.markdown("Calculate your Body Mass Index (BMI) quickly and easily!")
    

    st.sidebar.header("Personal Details")
    

    weight = st.sidebar.number_input(
        "Weight (kg)", 
        min_value=1.0, 
        max_value=300.0, 
        value=70.0, 
        step=0.1
    )
    
    height = st.sidebar.number_input(
        "Height (m)", 
        min_value=0.5, 
        max_value=2.5, 
        value=1.75, 
        step=0.01
    )
    
    
    if st.sidebar.button("Calculate BMI"):
        
        bmi, category = calculate_bmi(weight, height)
        
     
        st.header("📊 Your BMI Results")
        
       
        if category == "Underweight":
            color = "blue"
        elif category == "Normal Weight":
            color = "green"
        elif category == "Overweight":
            color = "orange"
        else:
            color = "red"
        
        
        st.markdown(f"""
        <div style='background-color:{color}; color:white; padding:10px; border-radius:10px;'>
        <h3>BMI: {bmi}</h3>
        <h4>Category: {category}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        
        st.subheader("Health Recommendations")
        if category == "Underweight":
            st.info("Consider consulting a nutritionist to develop a healthy weight gain plan.")
        elif category == "Normal Weight":
            st.success("Great job maintaining a healthy weight! Continue your balanced lifestyle.")
        elif category == "Overweight":
            st.warning("Consider consulting a healthcare professional about diet and exercise.")
        else:
            st.error("Consult a healthcare professional for personalized weight management advice.")

    
    st.sidebar.markdown("---")
    st.sidebar.markdown("🩺 BMI is a screening tool, not a diagnostic test.")


if __name__ == "__main__":
    main()