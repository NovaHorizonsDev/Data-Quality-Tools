The goal of this project is to create alternative .csv and Excel data tools. 

<br>
Current Methods: <br>
1.) findMissingElements: returns rows with missing elements.<br>
2.) replaceMissingElements: fills empty elements with a custom entry (or "NAE" is none given).<br>
3.) deleteEmptyElementRows: deletes rows with empty data. <br>

<br>



3/14/2025: Update 1.2: The FinanceBro Update: 
<br>
What's new: <br>
-Present Value function:  .PV(FutureValue, discountRate= None, time =None). Default discount Rate is .02, default time is 1 year. <br>
Note: discount rate != -1 otherwise a divide by zero error is raised. 
<br>
-Future Value function: .FV(PresentValue, discountRate= None, time =None). Default discount Rate is .02, default time is 1 year. <br>
Note: discount rate != -1  and time != 0 at the same time otherwise an arithmatic error is raised. (You get 0 to the power of 0). <br>
<br>Both are non-annuity. 
<br>
-Simple Interest (non-Compounding) Doubling Time: .SimpleDoubleTime(simple_interest_rate). Entering 0 will raise a Divide by Zero Error. You will never double with 0 interest rate.
<br>
