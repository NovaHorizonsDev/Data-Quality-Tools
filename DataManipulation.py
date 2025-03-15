import os
import csv

from jinja2 import UndefinedError


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


class FinanceBro:
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