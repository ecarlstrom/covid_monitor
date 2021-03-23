# from covid19_data import JHU

# print("Recovered: " + str(JHU.US.recovered))
# print("Confirmed: " + str(JHU.US.confirmed))

# print("California deaths: " + str(JHU.California.deaths))
# print("California confirmed: " + str(JHU.California.confirmed))

# print("\n")
# print("UK confirmed: " + str(JHU.UnitedKingdom.confirmed))

# JSON data

# import covid19_data as COVID
# total = COVID.jsonByName("Total")
# India = COVID.jsonByName("India")

# print("Total deaths: " + str(total) + "\n")
# print("India confirmed: " + str(India))
# print("India deaths: " + str(India))

# next data module

from covid import Covid

covid = Covid()

# print(covid.get_data())

# place = covid.list_countries()
# print(place)

# italy_cases = covid.get_status_by_country_name("Italy")
# print(italy_cases)

# active = covid.get_total_active_cases()
# print(active)

# different data source, can switch within the covid module
covid2 = Covid(source="worldometers")
confirmed1 = covid.get_total_confirmed_cases()
print("Worldometers: " + str(confirmed1))
covid3 = Covid(source="john_hopkins")
confirmed2 = covid3.get_total_confirmed_cases()
print("JHU: " + str(confirmed2))
