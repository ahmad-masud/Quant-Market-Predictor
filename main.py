import yfinance as yf
from modules import predict_future_price, risk_score, plot_data

popular_ticker_symbols = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "GOOGL": "Alphabet Inc. (Google)",
    "FB": "Meta Platforms, Inc. (formerly Facebook, Inc.)",
    "BRK.A": "Berkshire Hathaway Inc.",
    "JNJ": "Johnson & Johnson",
    "V": "Visa Inc.",
    "WMT": "Walmart Inc.",
    "TSLA": "Tesla, Inc.",
}

print('''
  /$$$$$$  /$$      /$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$| $$__  $$
| $$  \ $$| $$$$  /$$$$| $$  \ $$
| $$  | $$| $$ $$/$$ $$| $$$$$$$/
| $$  | $$| $$  $$$| $$| $$____/ 
| $$/$$ $$| $$\  $ | $$| $$      
|  $$$$$$/| $$ \/  | $$| $$      
 \____ $$$|__/     |__/|__/      
      \__/                       
''')                                                                                                            
                                                                                                            

# Display the list of popular ticker symbols to the user.
print('Popular Ticker Symbols:\n')
for symbol, company in popular_ticker_symbols.items():
    # Iterate through the dictionary of ticker symbols and print each one with its corresponding company name.
    print(f"{symbol} - {company}")

# Prompt to guide users where they can find more ticker symbols.
print('\nFind more ticker symbols at https://stockanalysis.com/stocks/\n')

while (True):
    # Request user input for the ticker symbol they're interested in.
    ticker_symbol = input('Enter the ticker symbol: ')
    if yf.Ticker(ticker_symbol).history(period='20y').empty: # Check if the ticker symbol is invalid
        continue

    # Request user input for the period in years for which they want the data, with a constraint between 1 and 20 years.
    period = input('How far back do you want data from, choose a period in years from 1 to 20: ')

    # Validate the period input to ensure it's a digit, and within the allowed range (1 to 20 years).
    if (period.isdigit() == False) or (int(period) < 1) or (int(period) > 20):
        # If the input is invalid, notify the user and terminate the program.
        print('Invalid period')
        continue

    while (True):
        # Present the user with options for the functionality they wish to use.
        print('1. Predict the future stock price')
        print('2. Measure Stock Risk in Volatility')
        print('3. Plot the historical stock data')
        print('4. Change Ticker Symbol and/or Period')
        print('5. Exit')

        # Capture the user's choice.
        option = input('Choose an option: ')

        # Based on the user's choice, either predict future stock prices or plot historical data.
        if option == '1':
            # If option 1, request the number of days into the future for which the prediction is desired.
            x_days = int(input('Enter the number of days into the future for the prediction: '))
            # Call the function to predict future price based on the inputs.
            predict_future_price(ticker_symbol, x_days, period)
        elif option == '2':
            # If option 2, call the function to measure stock risk based on the ticker symbol and period.
            risk_score(ticker_symbol, period)
        elif option == '3':
            # If option 2, call the function to plot historical data based on the ticker symbol and period.
            plot_data(ticker_symbol, period)
        elif option == '4':
            # If option 3, break out of the current loop and prompt the user for a new ticker symbol and period.
            break
        elif option == '5':
            # If option 4, terminate the program.
            exit()
        else:
            # If the user enters an invalid option, notify them.
            print('Invalid option')
