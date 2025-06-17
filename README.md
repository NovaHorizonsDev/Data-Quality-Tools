*As of June 17th: This project is no longer open source and is under copyright*

Finance & Data Cleaning Toolkit<br>
This Python module provides a set of tools for handling financial analysis and data preprocessing, especially focused on identifying and processing missing elements in CSV files, and computing core corporate finance formulas. Designed for students, analysts, or developers working with finance datasets or time value of money problems.


NEW UPDATE: Ratio_ed: 
Integrate common liquidity, leverage, and other catagories (future update) ratios in you workflow! Try as well the preprogrammed informatrion getters to get all ratios at once! (more ratios and preprogrammed getters in future updates)



Project Structure
The module is organized into three main classes:

1. MissingElements
A utility class for detecting and managing missing elements in CSV files.

Key Features:
findMissingElements() – Scans for rows containing missing elements and returns them.

replaceMissingElements(filler) – Replaces missing elements with a given value or default "NAE".

CustomreplaceMissingElements() – Interactively replaces missing entries based on user input.

deleteEmptyElementRows() – Removes any rows that contain missing (empty) entries.

Supported file types: .csv
Note: While .xls and .xlsx are checked, they are not yet supported for reading/writing.


2.) Ratio_ed: 
A class full of accounting and financial ratios
*see class for uptodate ratios




3. FinanceAnthology
A static-method-based class containing formulas used in corporate finance, valuation, and time value of money.

Highlights:
Profitability & Margin Metrics:

GrossProfit, GrossProfitMargin, EBIT, NOPAT

Free Cash Flow Calculations:

FreeCashFlowNOPAT, FreeCashFlowEBIT

Interest & Time Value Calculations:

TimeValueSolver, SimpleDoubleTime, EffectiveAnnualRate, Annuity Calculations

Capital Budgeting Metrics:

NPV, PaybackPeriod, ProfitabilityIndex

Inflation & Nominal Rates:

NominalRealRate, ApproxNominalRealRate, PremiumRequiredrateOfReturn

Designed with flexibility and modularity for solving finance homework, business valuation, or applied modeling tasks.
