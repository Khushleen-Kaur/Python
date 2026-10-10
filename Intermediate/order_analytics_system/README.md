# Order Analytics System

A command-line Python project for  analysing e-commerce order data. It uses a JSON file as its data source and the [Rich](https://github.com/Textualize/rich) library to display styled output in the terminal.

## Features

- **Sales analysis** — view order counts by status, order-value summaries, and product-related statistics.
- **Category analysis** — inspect revenue and quantities by product category.
- **Customer analysis** — view customer order details and ranked customer reports.
- **Time-based analysis** — view today's orders, this month's orders, or orders within a selected date range.
- **Search and filtering** — browse orders by status, view order counts by customer, and filter orders by amount.
- **Order listing** — display order details, including the order ID, customer, amount, items, date, and status.
- **Styled terminal interface** — use Rich markup for coloured headings and readable console output.

## Tech Stack

- **Python 3.10+** (Python 3.10 or later is recommended because the project uses `match` / `case` syntax)
- **JSON** for storing sample order data
- **Rich** for terminal formatting

## Project Structure

```text
order_analytics_system/
├── main.py                  # Main menu and application entry point
├── requirements.txt         # Python dependencies
├── data/
│   └── orders.json          # Sample order dataset
└── utils/
    ├── analysis.py          # Sales, category, and report navigation
    ├── customer_analysis.py # Customer-related reports
    ├── data_analysis.py     # Date-based order reports
    ├── helper.py            # Shared data-loading and calculation helpers
    └── search.py            # Order search and filtering options
```

## Getting Started

### 1. Prerequisites

Install Python 3.10 or later. You can check your version with:

```bash
python --version
```

### 2. Get the project

Clone the repository or download and extract the project folder. Open a terminal in the `order_analytics_system` project root — the directory containing `main.py`.

### 3. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
```

On Windows Command Prompt:

```bat
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install the dependency

The application uses Rich for its terminal interface:

```bash
python -m pip install rich
```

If you use `requirements.txt`, make sure it is saved as a normal UTF-8 text file before installing from it.

### 5. Run the application

From the project root, run:

```bash
python main.py
```

Use the numbered menu options to navigate through the available reports and filters. Choose the exit option to close the application.


## Concepts Practised

This project is a hands-on way to practise:

- Reading structured data from JSON
- Working with lists, dictionaries, and nested records
- Writing and reusing functions across Python modules
- Filtering and sorting collections
- Using `lambda` functions and date-based filtering
- Handling user input and exceptions
- Formatting terminal output with Rich

## Current Scope

This is a local, menu-driven command-line application. It reads data from a JSON file; it does not currently provide a web API, database integration, authentication, or a graphical interface.

## Future Improvements

Possible next steps include improving input validation and error messages, adding automated tests, refining customer-level aggregations, separating completed revenue from other order values, and eventually moving the data layer to a database or exposing reports through a REST API.

## Author

**Khushleen Kaur**

---

Built as a Python learning project to practise working with structured order data and generating useful reports from it.
