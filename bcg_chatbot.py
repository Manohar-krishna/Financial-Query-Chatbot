
import pandas as pd

# Sample financial data representing your analysis from Task 1
data = {
    'Year': [2023, 2024],
    'Total Revenue ($M)': [120, 150],
    'Net Income ($M)': [25, 35],
    'Expenses ($M)': [95, 115]
}
financial_df = pd.DataFrame(data)

print("Financial Data Ready:")
print(financial_df)

import pandas as pd

# --- Data Preparation (from Step 2) ---
data = {
    'Year': [2023, 2024],
    'Total Revenue ($M)': [120, 150],
    'Net Income ($M)': [25, 35],
    'Expenses ($M)': [95, 115]
}
financial_df = pd.DataFrame(data)

# --- Functions to get answers from the DataFrame ---

def get_revenue_for_year(year):
    """Fetches the total revenue for a specific year."""
    try:
        revenue = financial_df[financial_df['Year'] == year]['Total Revenue ($M)'].iloc[0]
        return f"The total revenue in {year} was ${revenue} million."
    except IndexError:
        return f"Sorry, I don't have revenue data for the year {year}."

def get_net_income_change():
    """Calculates the change in net income between 2023 and 2024."""
    try:
        income_2023 = financial_df[financial_df['Year'] == 2023]['Net Income ($M)'].iloc[0]
        income_2024 = financial_df[financial_df['Year'] == 2024]['Net Income ($M)'].iloc[0]

        change = income_2024 - income_2023

        if change > 0:
            return f"Net income increased by ${change} million from 2023 to 2024."
        else:
            return f"Net income decreased by ${abs(change)} million from 2023 to 2024."
    except IndexError:
        return "Sorry, I need data for both 2023 and 2024 to calculate the change."

def get_expenses_for_year(year):
    """Fetches the expenses for a specific year."""
    try:
        expenses = financial_df[financial_df['Year'] == year]['Expenses ($M)'].iloc[0]
        return f"The expenses in {year} were ${expenses} million."
    except IndexError:
        return f"Sorry, I don't have expense data for the year {year}."

# --- Main Chatbot Logic ---

def financial_chatbot(user_query):
    """Matches user query to the correct data function."""
    query = user_query.lower().strip() # Normalize input for better matching

    if "total revenue in 2024" in query:
        return get_revenue_for_year(2024)

    elif "net income changed" in query:
        return get_net_income_change()

    elif "expenses in 2023" in query:
        return get_expenses_for_year(2023)

    else:
        return "Sorry, I can only answer predefined questions. Please try one of the following:\n" \
               "- What was the total revenue in 2024?\n" \
               "- How has net income changed from 2023 to 2024?\n" \
               "- What were the expenses in 2023?"

# --- Interactive Session ---

if __name__ == "__main__":
    print("Welcome to the Financial Analysis Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = financial_chatbot(user_input)
        print(f"Chatbot: {response}")
