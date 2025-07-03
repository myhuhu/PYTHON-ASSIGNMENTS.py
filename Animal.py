class Patient:
    def __init__(self):
        self.total=0.0

    def details(self):
        self.no=input("Enter Patient number:")
        print.name=input("Enter Patient name:")
        print("\n========\n")
        print("Patient Number:",self.no)
        print("Patient Name:",self.name)

    def billing(self,regfee=0.0, cons=0.0,labchar=0.0,phar=0.0):
        return regfee+cons+labchar+phar

    def billing(self, regfee=0.0,cons=0.0,labchar=0.0,phar=0.0,
                days=0.0,rates=0.0):
        return regfee+cons+labchar+phar+(days*rates)

    p1 = Patient()
    p1.details()

    option=input("is Patient out-Patient(Y/N):")
    option=option.upper()
    if option!='Y' and option !='N':
        option=input("is Patient out-Patient(Y/N):")

    if option=='Y':
        regfee=float(input("Enter registration fee:"))
        cons=float(input("Enter consulation  fee:"))
        labchar=float(input("Enter lab charges fee:"))
        phar=float(input("Enter pharmacy charges:"))
        print("Total charges:",p1.billing(regfee,cons,labchar,phar))


    if option=='N':
        regfee=float(input("Enter registration  fee:"))
        cons=float(input("Enter consulation  fee:"))
        phar=float(input("Enter pharmacy  charges:"))
        days=float(input("Enter Number of days:"))
        rates=float(input("Enter daily rates:"))

        print("Total charges:",p1.billing(regfee,cons,labchar,phar,days,rates))




                
        
        
        
        
        
        
    
        
        
        
    
