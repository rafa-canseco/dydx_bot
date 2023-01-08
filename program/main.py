from constants import ABORT_ALL_POSITIONS , FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices

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