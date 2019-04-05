class Property():
    # the docstring below can be accessed via the static class variable "__doc__"
    """This parent class stores generic property related information"""

    def __init__(self, sqft, lotSize, askingPrice, appraisalValue, description):
        self.sqft = sqft
        self.lotSize = lotSize
        self.askingPrice = askingPrice
        self.appraisalValue = appraisalValue
        self.description = description
    
    def __str__(self):
        return f"""{self.description}
                          sqft: {self.sqft}
                       lotSize: {self.lotSize}
                   askingPrice: {self.askingPrice}
                appraisalValue: {self.appraisalValue}"""
    
    def price_v_appraisal(self):
        return self.appraisalValue - self.askingPrice

    def price_per_sqft(self):
        return self.askingPrice // self.sqft

    def flex_room(self):
        return self.lotSize - self.sqft

    def is_positive(self, value):
        if value <= 0:
            return False
        return True
        