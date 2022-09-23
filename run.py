from booking.booking import Booking 

try: 
    with Booking() as bot : # Context manager 
        bot.land_first_page() 
        bot.change_currency('USD')
        bot.select_place_to_go(input("Enter Location "))
        bot.select_dates(check_in_date=input("Enter check in date "), check_out_date=input("Enter check out date "))
        bot.select_adults(int(input("Enter the number of people ")))
        bot.click_search()
        bot.apply_filtrations() 
        bot.refresh() # A workaround to let bot to grab data properly
        bot.report_results() 

except Exception as e: 
    if "in PATH" in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        ) 
    else: 
        raise 
