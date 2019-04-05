from models.property import Property

class Singlefamily(Property):
    """This child class (parent: Property) stores single-family property related information"""

    def __init__(self, sqft, lotSize, askingPrice, appraisalValue, description, beds, baths):
        Property.__init__(self, sqft, lotSize, askingPrice, appraisalValue, description)
        self.beds = beds
        self.baths = baths
    
    # overriding parent __str__
    def __str__(self):
        return f"""{self.description}
                          sqft: {self.sqft}
                       lotSize: {self.lotSize}
                          beds: {self.beds}
                         baths: {self.baths}
                   askingPrice: {self.askingPrice}
                appraisalValue: {self.appraisalValue}"""
    
    def price_per_bedroom(self):
        return self.askingPrice // self.beds
