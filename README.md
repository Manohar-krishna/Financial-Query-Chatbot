# Financial Query Chatbot

*A rule-based conversational interface for financial data analysis, developed during the BCG Virtual Internship Program*

## Overview

This Financial Query Chatbot was developed as part of the Boston Consulting Group (BCG) Virtual Internship training program. The project demonstrates fundamental skills in data analysis automation, Python programming, and building interactive query systems for business intelligence.

The chatbot serves as an automated financial analyst assistant, enabling users to quickly retrieve key financial metrics through conversational queries. It showcases the practical application of data manipulation and rule-based natural language processing for business decision-making support.

### Project Context

Built as part of BCG's virtual internship curriculum, this project addresses the real-world challenge of making financial data more accessible to stakeholders who need quick insights without diving into complex spreadsheets or databases. The chatbot exemplifies how consultants can leverage technology to streamline data analysis and improve client communication.

## Features

- **Revenue Query**: Get total revenue for specific years
- **Net Income Analysis**: Calculate and report changes in net income between years
- **Expense Tracking**: Retrieve expense data for specific years
- **Interactive CLI**: User-friendly command-line interface for continuous interaction

## Dataset

The chatbot currently uses sample financial data for analysis:

| Year | Total Revenue ($M) | Net Income ($M) | Expenses ($M) |
|------|-------------------|-----------------|---------------|
| 2023 | 120               | 25              | 95            |
| 2024 | 150               | 35              | 115           |

## Prerequisites

- Python 3.x
- pandas library

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install required dependencies:
```bash
pip install pandas
```

## Usage

Run the chatbot from the command line:

```bash
python bcg_chatbot.py
```

### Sample Queries

The chatbot can answer the following types of questions:

- "What was the total revenue in 2024?"
- "How has net income changed from 2023 to 2024?"
- "What were the expenses in 2023?"

### Example Interaction

```
Welcome to the Financial Analysis Chatbot! Type 'exit' to quit.

You: What was the total revenue in 2024?
Chatbot: The total revenue in 2024 was $150 million.

You: How has net income changed from 2023 to 2024?
Chatbot: Net income increased by $10 million from 2023 to 2024.

You: exit
Chatbot: Goodbye!
```

## Code Structure

### Key Functions

- **`get_revenue_for_year(year)`**: Fetches total revenue for a specified year
- **`get_net_income_change()`**: Calculates the difference in net income between 2023 and 2024
- **`get_expenses_for_year(year)`**: Retrieves expense data for a specified year
- **`financial_chatbot(user_query)`**: Main logic that matches user queries to appropriate functions

## Customization

### Adding New Data

To update or expand the financial data, modify the `data` dictionary:

```python
data = {
    'Year': [2023, 2024, 2025],  # Add more years
    'Total Revenue ($M)': [120, 150, 180],
    'Net Income ($M)': [25, 35, 45],
    'Expenses ($M)': [95, 115, 135]
}
```

### Adding New Query Types

To add new question patterns:

1. Create a new function to handle the data retrieval
2. Add a new condition in the `financial_chatbot()` function
3. Update the help message with the new query type

## Limitations

- Currently supports only predefined query patterns
- Limited to years 2023 and 2024 in the sample dataset
- Requires exact or similar phrasing for query matching

## Future Enhancements

- Implement natural language processing (NLP) for more flexible query understanding
- Add support for additional financial metrics (ROI, profit margins, growth rates)
- Expand dataset to include multiple years and categories
- Create a web-based interface using Flask or Streamlit
- Add data visualization capabilities

## Acknowledgments

Developed as part of the BCG financial analysis project.
