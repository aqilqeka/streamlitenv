import streamlit as st

# Function to calculate monthly mortgage payment
def calculate_monthly_mortgage(principal, annual_interest, loan_term_years):
    if loan_term_years == 0:
        return float('inf')  # Handle division by zero error gracefully
    
    monthly_interest_rate = annual_interest / 12 / 100
    num_payments = loan_term_years * 12
    denominator = ((1 + monthly_interest_rate)**num_payments - 1)
    if denominator == 0:
        return float('inf')  # Handle division by zero error
    monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate)**num_payments / denominator
    return monthly_payment


st.title('Rental Real Estate Calculator')

# Input fields 
st.sidebar.header('Input Information')
house_price = st.sidebar.number_input('House Price:', min_value=1.0, value=265000.00)
monthly_rent = st.sidebar.number_input('Monthly Rent:', min_value=1.0)
down_payment = st.sidebar.number_input('Down Payment:', min_value=1.0, max_value=house_price)
loan_term_years = st.sidebar.number_input('Loan Term in Years:', min_value=1)
annual_interest = st.sidebar.number_input('Annual Interest (%):', min_value=0.0)
monthly_taxes = st.sidebar.number_input('Monthly Taxes:', min_value=0.0)

# Calculate outputs
principle = house_price - down_payment
monthly_rent_to_value = (monthly_rent / house_price) * 100
annual_gross_rental = monthly_rent * 12
monthly_mortgage = calculate_monthly_mortgage(principle, annual_interest, loan_term_years)
annual_profit = annual_gross_rental - ((monthly_mortgage + monthly_taxes) * 12)

# Output fields
st.header('Output Information')
st.write(f'House Price: ${house_price}')
st.write(f'Down Payment: ${down_payment} ({down_payment / house_price * 100:.2f}%)')
st.write(f'Principle: ${principle}')
st.write(f'Monthly Rent-to-Value: {monthly_rent_to_value:.2f}%')
st.write(f'Annual Gross Rental: ${annual_gross_rental}')
st.write(f'Monthly Mortgage: ${monthly_mortgage:.2f}')
st.write(f'Annual Profit: ${annual_profit:.2f}')
