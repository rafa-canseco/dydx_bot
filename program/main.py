from constants import ABORT_ALL_POSITIONS , FIND_COINTEGRATED , PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits


if __name__ == "__main__":
    
    #Connect to client
    try:
        print("Conectando al cliente")
        client = connect_dydx()
    except Exception as e:
        print("error conectándose al cliente", e)
        exit(1)

    #Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Cerrando todas las posiciones")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("error closing all positions", e)
            exit(1)

    #Find Cointegrated pairs
    if FIND_COINTEGRATED:

        #Construct market prices:
        try:
            print("Fetching market prices, please allow 3 mins..")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("error constructing market prices", e)
            exit(1)

     #Store cointegrated pairs:
        try:
            print("Storing cointegrated pairs")
            stores_result = store_cointegration_results(df_market_prices)
            if stores_result != "saved":
                print("error saving cointegrated pairs")
                exit(1)
        except Exception as e:
            print("error saving cointegrated pairs: ", e)
            exit(1) 
   
   #Run as always on
    while True:

        #Place trades for opening positions
        if MANAGE_EXITS:
            try:
                print("managing exits")
                manage_trade_exits(client)
            except Exception as e:
                print("Error managing positions", e)
                exit(1) 


            
            
            
        #Place trades for opening positions
        if PLACE_TRADES:
            try:
                print("finding trading oportunities")
                open_positions(client)
            except Exception as e:
                print("Error trading pairs", e)
                exit(1) 