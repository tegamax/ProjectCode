def make_car(car_manufacturer,car_model,**Other_attributes):
    Other_attributes['car_model']=car_model
    Other_attributes['car_manufacturer']=car_manufacturer

    return Other_attributes


print(make_car('Toyota','Rav 4',color='blue'))