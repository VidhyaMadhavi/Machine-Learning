#---------------------------------------------------------------------#
#Program Name: clean_data.py
#Description: List the frequency counts of the columns and then
# removing the un-necessary columns
#---------------------------------------------------------------------#

def display_frequency_counts(data):
    print("\n\nCleaning the data: Displaying the Frequency Counts")
    print("#-----------------------------------------------------------#")
    # seller column:
    print("\n\n Seller column Frequency Counts")
    print (data["seller"].value_counts())

    # offerType column
    print("\n\n offerType column Frequency Counts")
    print (data["offerType"].value_counts())

    # nrOfPictures column
    print("\n\n nrOfPictures column Frequency Counts")
    print (data["nrOfPictures"].value_counts())

    # abtest column
    print("\n\n abtest column Frequency Counts")
    print (data["abtest"].value_counts())

    # vehicle Type
    print("\n\n vehicle Type column Frequency Counts")
    print(data["vehicleType"].value_counts())

    # gearbox
    print("\n\n gearbox column Frequency Counts")
    print(data["gearbox"].value_counts())

    # monthOfRegistration
    print("\n\n monthOfRegistration column Frequency Counts")
    print(data["monthOfRegistration"].value_counts())

    # notRepairedDamage
    print("\n\n notRepairedDamage column Frequency Counts")
    print(data['notRepairedDamage'].value_counts())

    # name
    print("\n\n notRepairedDamage column Frequency Counts")
    print(data['name'].value_counts())

def remove_unwanted_columns(data):
    pass
    #seller column:
    #Only 3 records belong to second seller ,
    #privat        371525
    #gewerblich         3
    # so this column dont have significant data and it can be removed.
    print ("\n\n Removing Unwanted Columns")
    print("#-----------------------------------------------------------#")
    print("\n Removed Column: seller")
    del data["seller"]

    #offerType column
    #Angebot   371516
    #Gesuch    12
    print("\n Removed Column: offerType")
    del data["offerType"]

    # nrOfPictures column
    #this column only take one value i.e., 0 , so there is no advantage of consider this column in our dataset
    print("\n Removed Column: nrOfPictures")
    del data["nrOfPictures"]

    print("\n Removed Column: name (as the names would not help much to the modelling)")
    del data["name"]

    print("\nThe dates \"dateCrawled\",\"dateCreated\",\"lastSeen\" represents when was the ads crawled , or time of lastseen of these ads.")
    print("we will not able to collect much information from these dates so we can remove them")
    print(" Removed Columns: \"dateCrawled\",\"dateCreated\",\"lastSeen\"  ")
    updated_data = data.drop(["dateCrawled", "dateCreated", "lastSeen"], axis=1)

    return updated_data



