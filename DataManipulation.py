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
    def PV(self, futureValue, discountRate=None, time = None):

        if discountRate is None:
            discountRate=.02
        if time is None:
            time=1
        if discountRate == -1:
           raise ZeroDivisionError("Discount Rate cannot be -1")
        return (futureValue/ ((1+ discountRate) ** time))


    def FV(self, presentValue, discountRate=None, time = None):
        if discountRate is None:
            discountRate=.02
        if time is None:
            time=1
        if discountRate == -1 and time == 0:
            raise ArithmeticError("No FV, discount cannot be -1 and time cannot be 0 at the same time")
        return presentValue * ((1+discountRate)**time)

    def SimpleDoubleTime(self, simple_interest_rate):

        if simple_interest_rate ==0:
            raise ZeroDivisionError("Rate cannot be 0. You will never double it.")
        return 1/simple_interest_rate


    def GrossProfit(self, netSales, COGS):
        return netSales - COGS

    def GrossProfitMargin(self, netSales, COGS):
        if netSales == 0:
            return ZeroDivisionError
        return (netSales - COGS)/netSales

    def EBIT_NetSales(self, netSales, COGS, operatingExpenses):
        return netSales - COGS - operatingExpenses

    def EBIT_GrossProfit(self, grossProfit, operatingExpenses):
        return grossProfit - operatingExpenses

    def NOPAT_EBIT(self, EBIT, tax_rate_decimal):
        return EBIT*(1-tax_rate_decimal)

    def NOPAT_GrossProfit(self, grossProfit,operatingExpenses, tax_rate_decimal):
        return (grossProfit-operatingExpenses)*(1-tax_rate_decimal)

    def FreeCashFlowNOPAT (self, change_in_Operating_capital,NOPAT):
        return NOPAT - change_in_Operating_capital

    def FreeCashFlowEBIT(self, change_in_Operating_capital,EBIT, tax_rate_decimal):
        return (EBIT*(1-tax_rate_decimal))- change_in_Operating_capital

    def ApproxNominalRealRate(self, inflation_rate, real_rate):
        return inflation_rate + real_rate

    def NominalRealRate(self, inflation_rate, real_rate):
        return ((1+inflation_rate)*(1-real_rate))-1

    def PremiumRequiredrateOfReturn(self, credit_premium, liquidity_premium, maturity_premium, inflation_rate=None, real_rate=None, Nominal_real_rate=None):
        if inflation_rate & real_rate & Nominal_real_rate is None:
            return ArithmeticError("Inflation rate, Real rate, and Nominal Real Rate cannot be all None")
        elif inflation_rate & real_rate is None:
            return Nominal_real_rate+ maturity_premium+credit_premium+liquidity_premium
        elif Nominal_real_rate is None:
            return self.NominalRealRate(inflation_rate, real_rate) +  maturity_premium+credit_premium+liquidity_premium
        else:
            return ArithmeticError



