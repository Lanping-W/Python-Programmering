import datehantering 

def main():
    col_to_del=["people_vaccinated","daily_vaccinations_raw","daily_vaccinations","people_vaccinated_per_hundred","daily_vaccinations_per_million","vaccines","source_name","source_website"]
    data = datehantering.Datahantering("vaccin_covid.csv","vaccin.db")
    data.read_csv()
    data.create_database()
    data.seed_database("vaccin_table")
    data.clear_database(col_to_del)

  
if __name__=="__main__":
    main()

