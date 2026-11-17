prices = {"input":0.3,"output":0.67}

def cost(token,price_per_million):
    return token*price_per_million/1000000

total = cost(2000 , prices["input"])  + cost(500 , prices["output"])

print(f"cost per call : ${total:.6f}")

