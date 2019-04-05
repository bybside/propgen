import random
from models.singlefamily import Singlefamily
from models.multifamily import Multifamily

class Propgen():
    """This class generates n number of properties based on predefined constant attributes"""

    # double underscore in attribute name denotes a private attribute
    # uppercase attribute names denote constants
    __SQFTS = [random.randint(1000, 2999) for i in range(10)]
    __LOTSIZES = [random.randint(3000, 10000) for i in range(10)]
    __ASKING_PRICES = [random.randint(200000, 600000) for i in range(10)]
    __APPRAISAL_VALUES = [random.randint(200000, 600000) for i in range(10)]
    __SFH_DESCRIPTIONS = ["SFH in West Austin", "SFH in East Austin", "SFH in North Austin", "SFH in South Austin"]
    __MFH_DESCRIPTIONS = ["MFH in West Austin", "MFH in East Austin", "MFH in North Austin", "MFH in South Austin"]
    __BEDS = [1, 2, 3, 4]
    __BATHS = [1, 2, 3]
    __UNITS = [2, 3, 4]

    def __init__(self):
        self.properties = []
        self.num_of_properties = 0

    # generate a list of random properties
    def generate_properties(self, num_of_properties):
        self.num_of_properties = num_of_properties
        for i in range(num_of_properties):
            if random.randint(0, 1):
                self.properties.append(Singlefamily(sqft=random.choice(self.__SQFTS),
                                                    lotSize=random.choice(self.__LOTSIZES),
                                                    askingPrice=random.choice(self.__ASKING_PRICES),
                                                    appraisalValue=random.choice(self.__APPRAISAL_VALUES),
                                                    description=random.choice(self.__SFH_DESCRIPTIONS),
                                                    beds=random.choice(self.__BEDS),
                                                    baths=random.choice(self.__BATHS)))
            else:
                self.properties.append(Multifamily(sqft=random.choice(self.__SQFTS),
                                                   lotSize=random.choice(self.__LOTSIZES),
                                                   askingPrice=random.choice(self.__ASKING_PRICES),
                                                   appraisalValue=random.choice(self.__APPRAISAL_VALUES),
                                                   description=random.choice(self.__MFH_DESCRIPTIONS),
                                                   beds=random.choice(self.__BEDS),
                                                   baths=random.choice(self.__BATHS),
                                                   units=random.choice(self.__UNITS)))
