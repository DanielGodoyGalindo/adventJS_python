"""
The sleigh's GPS has gone crazy! 😱 Santa Claus has the segments of his trip, but they're all out of order.
Your mission is to reconstruct the complete route from the origin to the final destination.
Keep in mind: The first element of the array is always the first segment of the trip. From there, you must keep connecting destinations to the next origins.

revealSantaRoute([
  ['MEX', 'CAN'],
  ['UK', 'GER'],
  ['CAN', 'UK']
])
// → ['MEX', 'CAN', 'UK', 'GER']

revealSantaRoute([
  ['USA', 'BRA'],
  ['JPN', 'PHL'],
  ['BRA', 'UAE'],
  ['UAE', 'JPN'],
  ['CMX', 'HKN']
])
// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

revealSantaRoute([
  ['STA', 'HYD'],
  ['ESP', 'CHN']
])
// → ['STA', 'HYD']
🔎 Keep in mind:

There are no duplicate routes or cycles in Santa's path.
There may be segments that don't belong to the route; these must be ignored.
"""


def reveal_santa_route(routes: list[list[str]]) -> list[str]:
    
    # return next countries in the found route
    def next_route(country):
        for route in routes:
            if route[0] == country:
                if len(route)>1:
                    return route[1:] # if more than one country, return all found
                else:
                    return route[0] # return the one found
    
    output = []
    country = routes[0][0] # first country in route
    output.append(country)
    while True:
        result = next_route(country)
        if result:
            for r in result:
                output.append(r) # save all countries found in the route
            country = result[-1] # save last one to find next route
        else:
            break
    return output


print(reveal_santa_route([
  ['STA', 'HYD'],
  ['ESP', 'CHN']
]))