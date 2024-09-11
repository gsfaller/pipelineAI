import streamlit as st
import contrato
from datetime import datetime, time
def main():
    
    st.title("CRM System and Sales - (Simple Front-end project)")

    email = st.text_input("Insert your e-mail:")
    date = st.date_input("Please, insert the date of the sale:", datetime.now())
    time_hours = st.time_input("Insert the time of the sale:", value=time(9, 0)) # Standard Value: 09:00
    quantity = st.number_input("Insert the quantity sold:", min_value=1, step=1)
    gross_sale = st.number_input("Insert the sales total value:", min_value=0.0, format="%.2f")
    product = st.selectbox("Select box to choose the product sold.", options=["Boots", "Sandal", "Sneaker"])

    if st.button("Salvar"):
        data_hora = datetime.combine(date, time)
        st.write("**Sales Info:**")
        st.write(f"Staff Email:**")
        st.write("**Sales Info:**")
        st.write("**Sales Info:**")
        st.write("**Sales Info:**")



if __name__ == "__main__":
    main()


