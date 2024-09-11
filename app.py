import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():
    
    st.title("CRM System and Sales - (Simple Front-end project)")

    email = st.text_input("Insert your e-mail:")
    dt_sale = st.date_input("Please, insert the date of the sale:", datetime.now())
    time_hours = st.time_input("Insert the time of the sale:", value=time(9, 0)) # Standard Value: 09:00
    quantity = st.number_input("Insert the quantity sold:", min_value=1, step=1)
    gross_sale = st.number_input("Insert the sales total value:", min_value=0.0, format="%.2f")
    product = st.selectbox("Select box to choose the product sold.", options=["Boots", "Sandal", "Sneaker"])

    if st.button("Salvar"):
        try:
            # Vendas(email, dt_sale, time_hours, quantity, gross_sale, product)

            date_time = datetime.combine(dt_sale, time_hours)

            venda = Vendas(
                email=email,
                dt_sale=date_time,
                time_hours=time_hours,
                quantity=quantity,
                gross_sale=gross_sale,
                product=product
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro: {e}")


if __name__ == "__main__":
    main()


