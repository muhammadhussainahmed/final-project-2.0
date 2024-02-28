import streamlit as st

# Function to simulate patient registration
def register_patient(name, age, gender):
    # In a real-world scenario, you would save this information to a database
    patient_data = {
        "Name": name,
        "Age": age,
        "Gender": gender
    }
    return patient_data

# Function to display patient information
def display_patient_info(patient):
    st.write("Patient Information:")
    st.write(f"Name: {patient['Name']}")
    st.write(f"Age: {patient['Age']}")
    st.write(f"Gender: {patient['Gender']}")

# Main streamlit app
def main():
    st.title("Hospital Management System")

    # Sidebar for user input
    st.sidebar.header("User Input")
    patient_name = st.sidebar.text_input("Enter patient name:")
    patient_age = st.sidebar.number_input("Enter patient age:", min_value=0, max_value=150, value=0)
    patient_gender = st.sidebar.selectbox("Select patient gender:", ["Male", "Female", "Other"])

    # Register button
    if st.sidebar.button("Register Patient"):
        patient = register_patient(patient_name, patient_age, patient_gender)
        display_patient_info(patient)

if __name__ == "__main__":
    main()