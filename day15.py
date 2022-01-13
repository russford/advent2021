import heapq


def read_data ():
    with open ("day15.txt", "r") as f:
        return [[int(a) for a in l.strip()] for l in f.readlines()]


def search_astar(start, h_func, poss_func, cost_func):
    q = [(h_func(start), start)]
    visited = {start: None}
    cost = {start: 0}
    while q:
        h, state = heapq.heappop (q)
        if h_func(state) == 0:
            path = []
            final_cost = cost[state]
            while state != start:
                path.append (state)
                state = visited[state]
            return final_cost, path
        poss = poss_func (state)
        for p in poss:
            new_cost = cost[state] + cost_func(p)
            if p not in cost or new_cost < cost[p]:
                heapq.heappush(q, (new_cost + h_func(p), p))
                cost[p] = new_cost
                visited[p] = state
    return 0


def day1 (data):
    x_max, y_max = len(data[0]), len(data)

    def h_func (p):
        return abs(p[0]-x_max+1)+abs(p[1]-y_max+1)

    def poss (p):
        return [(p[0]+dx, p[1]+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]
                if 0 <= p[0]+dx < x_max and 0 <= p[1]+dy < y_max]

    def cost_func(p):
        return data[p[1]][p[0]]

    cost, path = search_astar((0,0), h_func, poss, cost_func)
    return cost


def day2 (data):
    x_max, y_max = len(data[0]), len(data)

    def h_func (p):
        return abs(p[0]-x_max*5+1)+abs(p[1]-y_max*5+1)

    def poss (p):
        return [(p[0]+dx, p[1]+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]
                if 0 <= p[0]+dx < x_max*5 and 0 <= p[1]+dy < y_max*5]

    def cost_func(p):
        t_x, t_y = p[0] // x_max, p[1] // y_max

        return (data[p[1] % y_max][p[0] % x_max] + t_x + t_y - 1) % 9 + 1

    cost, path = search_astar((0,0), h_func, poss, cost_func)
    return cost


if __name__ == "__main__":
    data = read_data()

    print(day1 (data))
    print(day2 (data))
