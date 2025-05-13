import os
import csv



class MissingElements:

    def __init__(self, file):

        self.file_path = file
        if(self.file_path==None):
            SystemError("File Not Found")
        file_ext = os.path.splitext(self.file_path)[1]


        if (file_ext not in ['.xlsx', '.xls', '.csv']):
            SystemError("FileType not Accepted")


    def findMissingElements(self):
        missing_elements_rows = []


        if(self.file_path==None):
            SystemError("File Not Found")
        file_ext = os.path.splitext(self.file_path)[1]


        if (file_ext not in ['.xlsx', '.xls', '.csv']):
            SystemError("FileType not Accepted")

        with open(self.file_path, 'r') as data:
            dataFile  = csv.reader(data)
            row_count=0
            for row in dataFile:
                if row_count==0:
                    missing_elements_rows.append(row)
                for element in row:
                    if element == "":
                        missing_elements_rows.append(row)


            if(len(missing_elements_rows)>0):
                return missing_elements_rows
            else:
                return []


    def replaceMissingElements(self,filler=None):
        with open(self.file_path, 'r') as data:
            dataFile = csv.reader(data)

            rows = list(dataFile)
            for row in rows:
                for element in range(len(row)):
                    if row[element]=="":
                        if filler is None:
                            row[element]="NAE"
                        else:
                            row[element]=filler
        data.close()

        with open(self.file_path, 'w',newline='') as data:
            dataEditor = csv.writer(data)
            dataEditor.writerows(rows)
            data.close()
        return None

    def CustomreplaceMissingElements(self):
        with open(self.file_path, 'r') as data:
            dataFile = csv.reader(data)

            rows = list(dataFile)
            for row in rows:
                for element in range(len(row)):
                    if row[element] == "":
                        print(row)
                        print("Enter replacement:")
                        userInput = input()
                        if userInput is None:
                            print("Nothing Entered will put \"NAE\"")
                            row[element] = "NAE"
                        else:
                            row[element] = userInput
        data.close()


    def deleteEmptyElementRows(self):
        rows_to_write= []
        with open(self.file_path, 'r') as data:
            dataFile = csv.reader(data)
            rows = list(dataFile)
            for row in rows:
                does_not_have_empty_element=True
                for element in range(len(row)):
                    if row[element]=="":
                        does_not_have_empty_element=False
                if does_not_have_empty_element:
                    rows_to_write.append(row)
            data.close()


        with open(self.file_path, 'w',newline='') as data:
            dataEditor = csv.writer(data)
            dataEditor.writerows(rows_to_write)
            data.close()

        return None









class FinanceAnthology:
    def __init__(self):
        pass

    @staticmethod
    def PV(futureValue, discountRate=None, time = None):

        if discountRate is None:
            discountRate=.02
        if time is None:
            time=1
        if discountRate == -1:
           raise ZeroDivisionError("Discount Rate cannot be -1")
        return (futureValue/ ((1+ discountRate) ** time))

    @staticmethod
    def FV( presentValue, discountRate=None, time = None):
        if discountRate is None:
            discountRate=.02
        if time is None:
            time=1
        if discountRate == -1 and time == 0:
            raise ArithmeticError("No FV, discount cannot be -1 and time cannot be 0 at the same time")
        return presentValue * ((1+discountRate)**time)

    @staticmethod
    def SimpleDoubleTime( simple_interest_rate):

        if simple_interest_rate ==0:
            raise ZeroDivisionError("Rate cannot be 0. You will never double it.")
        return 1/simple_interest_rate

    @staticmethod
    def GrossProfit( netSales, COGS):
        return netSales - COGS

    @staticmethod
    def GrossProfitMargin( netSales, COGS):
        if netSales == 0:
            return ZeroDivisionError
        return (netSales - COGS)/netSales

    @staticmethod
    def EBIT_NetSales( netSales, COGS, operatingExpenses):
        return netSales - COGS - operatingExpenses

    @staticmethod
    def EBIT_GrossProfit( grossProfit, operatingExpenses):
        return grossProfit - operatingExpenses

    @staticmethod
    def NOPAT_EBIT( EBIT, tax_rate_decimal):
        return EBIT*(1-tax_rate_decimal)

    @staticmethod
    def NOPAT_GrossProfit( grossProfit,operatingExpenses, tax_rate_decimal):
        return (grossProfit-operatingExpenses)*(1-tax_rate_decimal)

    @staticmethod
    def FreeCashFlowNOPAT ( change_in_Operating_capital,NOPAT):
        return NOPAT - change_in_Operating_capital

    @staticmethod
    def FreeCashFlowEBIT( change_in_Operating_capital,EBIT, tax_rate_decimal):
        return (EBIT*(1-tax_rate_decimal))- change_in_Operating_capital

    @staticmethod
    def ApproxNominalRealRate( inflation_rate, real_rate):
        return inflation_rate + real_rate

    @staticmethod
    def NominalRealRate( inflation_rate, real_rate):
        return round(((1+inflation_rate)*(1-real_rate))-1,2)

    @staticmethod
    def PremiumRequiredrateOfReturn( credit_premium, liquidity_premium, maturity_premium, inflation_rate=None, real_rate=None, Nominal_real_rate=None):
        if inflation_rate & real_rate & Nominal_real_rate is None:
            return ArithmeticError("Inflation rate, Real rate, and Nominal Real Rate cannot be all None")
        elif inflation_rate & real_rate is None:
            return Nominal_real_rate+ maturity_premium+credit_premium+liquidity_premium
        elif Nominal_real_rate is None:
            return FinanceAnthology.NominalRealRate(inflation_rate, real_rate) +  maturity_premium+credit_premium+liquidity_premium
        else:
            return ArithmeticError

    @staticmethod
    def AfterTaxCashFlows(beforeTaxCashFlows:list[float],taxRate_decimal):
        for i in range(len(beforeTaxCashFlows)):
            beforeTaxCashFlows[i] = round(beforeTaxCashFlows[i]*(1-taxRate_decimal),2)
        return beforeTaxCashFlows

#cashflows are after tax
    @staticmethod
    def NPV( initial_investment, discount_rate, cashflows:list[float] ):
        if discount_rate == -1:
            return ZeroDivisionError("Discount Rate cannot be -1")
        npv = -1 *initial_investment
        for i in range(len(cashflows)):
            npv += cashflows[i]/((1+discount_rate)**(i+1))
        return round(npv,2)

    @staticmethod
    def PaybackPeriod(cashflows:list[float],initial_investment):
        if initial_investment == 0:
            return ZeroDivisionError("Initial Investment cannot be 0")
        return (initial_investment/(1+cashflows[-1]))

    @staticmethod
    def ProfitabilityIndex(cashflows:list[float],initial_investment,discount_rate = None):
        #Free Project?
        if initial_investment == 0:
            return ZeroDivisionError("Initial Investment cannot be 0")
        #discount everything?
        if discount_rate == -1:
            return ZeroDivisionError("Discount Rate cannot be -1")

        #this step assumes cashflows are already PV
        if discount_rate is  None:
            return sum(cashflows)/initial_investment
        #if not PV
        sumOfPVCashFlows =0
        for i in range(len(cashflows)):
            sumOfPVCashFlows += FinanceAnthology.PV(cashflows[i], discount_rate,i+1)
        return sumOfPVCashFlows/initial_investment


class FinancialStatements:
    def __init__(self):
        pass

    @staticmethod
    def SimpleIncomeStatement(self, netSales, COGS, Operating_Expenses, ):
        return (f"Revenue:{netSales}\\COGS:{COGS}\\Gross Profit:{netSales-COGS}\\"
                f"Operating Expenses:{Operating_Expenses}")