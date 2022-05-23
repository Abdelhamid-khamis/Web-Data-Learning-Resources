import binance.client 
from binance.client import Client 
import pandas as pd 


Pkey = '123ASD4444124' 
Skey = '123ASD3241244'
client = Client(api_key=Pkey, api_secret=Skey) 


def format_value(valuetoformatx,fractionfactorx):
    
					value = valuetoformatx
					fractionfactor = fractionfactorx
					Precision = abs(int(f'{fractionfactor:e}'.split('e')[-1]))
					FormattedValue = float('{:0.0{}f}'.format(value, Precision))
					return FormattedValue		

def pairPriceinfo(ticker,client): 
				info = client.get_symbol_info(ticker)
				minPrice = pd.to_numeric(info['filters'][0]['minPrice'])  #  0 to isolate  price precision   #  2 to isloate qty 
				return minPrice

def pairQtyinfo(ticker,client):
					info = client.get_symbol_info(ticker)
					minQty = pd.to_numeric(info['filters'][2]['minQty'])   
					#print()
					return minQty 



# print out USDT Balance 
json = client.get_asset_balance(asset='USDT')
freeUSDT = float(json['free'])
totalUSDT = freeUSDT + float(json['locked'])

# print menu to the user 
print(f'\n \n Salam Whale /////////////// \n Total USDT {totalUSDT}/\n FreeUSDT {freeUSDT}\n \n Choose from this list: \n 1 = MarketBuy \n 2 = SELL OCO Order \n 3= SELL MARKET')
choice = int(input())
#print('this is what you choose: ',choice,type(choice))
if choice ==1:
	#send market buy order 
	print('You choose to MarketBuy, please write the ticker you want to purchse and include Quote pair:')
	ticker = str(input())
	price = client.get_avg_price(symbol=ticker)

	price = float(price['price'])


	print(f'you have choose:  \n {ticker} \n {price}$')
	print(f'How much in % you want to use from your FREE USDT to Buy {ticker}')

	pctUse = float(input())

	USDT = freeUSDT*pctUse
	qty = USDT/price

	print(f'\n Print 1 to Confirm? \n market buy order of {qty}, cost is: {USDT}')
	confirm = int(input())
	if confirm == 1:
		minQty = pairQtyinfo(ticker,client)
		qtyFormatted = format_value(qty,minQty)
		order = client.order_market_buy(symbol = ticker, quantity = qtyFormatted)
		print('\n Market BuyOrder is 100/100 Executed')

		#send market buy order
	else:
		print('Trade is terminated !!! thank you. ')

elif choice ==2:
	#polace oco sell order for the ticker we already have balance of
	print('Please write the asset name that you want to palce oco sell (XRP,BNB,BTC)\n')
	asset= str(input()).upper() #XRP
	
	#FORMATTTIN THE QTY 
	assetBalance = client.get_asset_balance(asset =asset)
	assetBalance = float(assetBalance['free'])


	print(f'You Total {asset} tokens balance = ',assetBalance)

	#switch
	print('please write the ticker you want to place OCO order on:(xtpusdt/xrpeth)')
	ticker = str(input()).upper()


	minQty = pairQtyinfo(ticker,client)
	assetBalance = format_value(assetBalance,minQty)

	print('you choose',ticker)
	price = client.get_avg_price(symbol=ticker)
	price = float(price['price'])

	#limit price , stopPrice , stopLimit.
	print('please choose your tp % from current price')
	pct_tp = float(input())
	pct_tp = pct_tp/100


	print('please wirte you sl % from current price: 2%/3%')
	pct_sl = float(input())
	pct_sl = pct_sl/100


	minPrice = pairPriceinfo(ticker,client)
	Above = price+(price*pct_tp)
	Above = format_value(Above,minPrice)
	belowTrigger = price-(price*pct_sl)
	belowTrigger = format_value(belowTrigger,minPrice)
	belowLimit = belowTrigger-(belowTrigger*0.001)
	belowLimit = format_value(belowLimit,minPrice)



	print('please confirm you want to place the oco orders: by number 1:')
	confirm = int(input())
	if confirm == 1:
		#place oco order 
					orderoco = client.create_oco_order(symbol= ticker,side ='SELL',
						quantity= assetBalance,
								price = Above ,
									stopPrice= belowTrigger, 
										stopLimitPrice = belowLimit,
											limitIcebergQty =0,
												stopIcebergQty = 0,																	
													stopLimitTimeInForce= 'GTC')
					
					print(f'{ticker} OCO Sell is PLACED ^^^')
					
	# we will ask if you want to sell the xrp based on just a % .
	# or yo want to write down the price your self ? 

elif choice==3:
		#what is the pair you want to sell 
		print('what is the ticker you want to sell(XRPUSDT?)')
		ticker= str(input()).upper()
		#qty to sell 
		asset = ticker[:-4].upper()
		qty = client.get_asset_balance(asset=asset)
		qty = float(qty['free'])

		minQty = pairQtyinfo(ticker,client) 
		qty = format_value(qty,minQty)

		order = client.order_market_sell(symbol = ticker, quantity = qty)
		print(f'100/100 MARKET SELL ON {ticker}')

else: 
	print('this is not the right choice')

