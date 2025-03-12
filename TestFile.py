
from DataManipulation import MissingElements


ME= MissingElements('C:/Users/trevo/PycharmProjects/DataQualityTools/uncleaned_data.csv')

rows = ME.findMissingElements()


ME.deleteEmptyElementRows()
