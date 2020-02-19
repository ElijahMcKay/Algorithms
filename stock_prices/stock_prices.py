#!/usr/bin/python

import argparse

stocks = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
	# defining a variable to contain our max profit so far.  Find a more elegant solution for this
	max_profit = -10000
	for i in range(len(prices)):
		# looping through each value after the current (we can't compare to values that have already passed)
		for j in range(i + 1, len(prices)):
			if prices[j] - prices[i] > max_profit:
				max_profit = prices[j] - prices[i]

	return max_profit


print(find_max_profit(stocks))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))