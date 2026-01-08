# Se define la clase Portafolio
class Portafolio:
    # Constructor de la clase Portafolio
    def __init__(self, stocks=None):
        # Si no se proporcionan acciones, se inicializa con valores predeterminados
        if stocks is None:
            self.tickers = ['S1', 'S2', 'S3']
            self.shares = [100, 150, 200]
            self.prices = [10.0, 20.0, 30.0]
            self.target_weights = [0.2, 0.5, 0.3]
        # Si se proporcionan acciones, se inicializa con los valores dados    
        else:   
            self.tickers = [x[0] for x in stocks] 
            self.shares = [x[1] for x in stocks]
            self.prices = [x[2] for x in stocks]
            self.target_weights = [x[3] for x in stocks]   

    # Método para actualizar los precios de las acciones
    def currentPrice(self, last_prices):
        
            # Se verifica que el número de precios ingresados sea igual al número de acciones en el portafolio
            if not (len(self.prices)==len(last_prices))==True:
                raise ValueError("Ingresar una lista de precios con la misma longitud que la lista de acciones")
            # Se actualizan los precios de las acciones
            self.prices = last_prices
            

    # Método para rebalancear el portafolio según los pesos objetivo dados
    def rebalance(self):
        
            # Se verifica que el número de pesos ingresados sea igual al número de acciones en el portafolio
            if not (len(self.tickers)==len(self.target_weights))==True:
                raise ValueError("Ingresar una lista de precios con la misma longitud que la lista de acciones")
            
            # Se verifica que la suma de los pesos sea igual a 1
            if not sum(self.target_weights)==1:
                raise ValueError("La suma de los pesos debe ser igual a 1")   
            
            # Se calcula el vlor actual del portafolio 
            current_portfolio_value = sum([self.shares[i] * self.prices[i] for i in range(len(self.tickers))])
            # Se calcula la nueva cantidad de acciones a tener en el portafolio
            rebalanced_allocated_stocks = [(current_portfolio_value * self.target_weights[i]) / self.prices[i] for i in range(len(self.tickers))]
            # Se redondea la cantidad de acciones al entero más cercano
            rebalanced_allocated_stocks = [round(x) for x in rebalanced_allocated_stocks]
            # Se obtienen las compras y ventas de acciones necesarias para el rebalanceo
            trades = [rebalanced_allocated_stocks[i] - self.shares[i] for i in range(len(self.tickers))] 
            # Se arma u diccionario con el reporte de compras y ventas
            sell_sold = ['vender' if trades[i] < 0 else 'comprar' for i in range(len(trades))]
            trades_report = {self.tickers[i]: {'accion': sell_sold[i], 'cantidad': abs(trades[i])} for i in range(len(self.tickers))}
            # Se actualiza la cantidad de acciones en el portafolio
            self.shares = rebalanced_allocated_stocks
        
            return trades_report