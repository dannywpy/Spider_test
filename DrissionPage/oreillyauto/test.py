text = {"compatibleModels":{"Chevette Base with engine L4 - 1.4L 1393cc 85ci GAS 1BBL vin I - 2 valve SOHC":[1977],"Chevette Base with engine L4 - 1.6L 98ci GAS 1BBL vin E - 2 valve SOHC":[1977,1978],"Chevette Base with engine L4 - 1.6L 98ci GAS 1BBL vin J - 2 valve SOHC":[1978],"Chevette Base with engine L4 - 1.6L 98ci GAS 2BBL vin 0 - 2 valve SOHC":[1979,1980],"Chevette Base with engine L4 - 1.6L 98ci GAS 2BBL vin 9 - 2 valve SOHC":[1980,1981],"Chevette Base with engine L4 - 1.6L 98ci GAS 2BBL vin E - 2 valve SOHC":[1979],"Chevette Rally Sport with engine L4 - 1.4L 1393cc 85ci GAS 1BBL vin I - 2 valve SOHC":[1977],"Chevette Rally Sport with engine L4 - 1.6L 98ci GAS 1BBL vin E - 2 valve SOHC":[1977],"Chevette Sandpiper with engine L4 - 1.4L 1393cc 85ci GAS 1BBL vin I - 2 valve SOHC":[1977],"Chevette Sandpiper with engine L4 - 1.6L 98ci GAS 1BBL vin E - 2 valve SOHC":[1977],"Chevette Scooter with engine L4 - 1.4L 1393cc 85ci GAS 1BBL vin I - 2 valve SOHC":[1977],"Chevette Scooter with engine L4 - 1.6L 98ci GAS 1BBL vin E - 2 valve SOHC":[1977,1978],"Chevette Scooter with engine L4 - 1.6L 98ci GAS 1BBL vin J - 2 valve SOHC":[1978],"Chevette Scooter with engine L4 - 1.6L 98ci GAS 2BBL vin 0 - 2 valve SOHC":[1979,1980],"Chevette Scooter with engine L4 - 1.6L 98ci GAS 2BBL vin 9 - 2 valve SOHC":[1980,1981],"Chevette Scooter with engine L4 - 1.6L 98ci GAS 2BBL vin E - 2 valve SOHC":[1979]}}

details = text["compatibleModels"]

for models in details:
    years = details[models]
    for year in years:
        print(year,models)






