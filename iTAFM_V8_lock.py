#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict


def build_graph(edge_list):
    graph = defaultdict(list)
    seen_edges = defaultdict(int)
    for src, dst, weight in edge_list:
        seen_edges[(src, dst, weight)] += 1
        if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
            continue
        graph[src].append((dst, weight))
        graph[dst].append((src, weight))  # remove this line of edge list is directed
    return graph


def dijkstra(graph, src, dst=None):
    nodes = []
    for n in graph:
        nodes.append(n)
        nodes += [x[0] for x in graph[n]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        u = min(q, key=dist.get)
        q.remove(u)

        if dst is not None and u == dst:
            return dist[dst], prev

        for v, w in graph.get(u, ()):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return float(dist), prev


def find_path(pr, node):  # generate path list based on parent points 'prev'
    p = []
    while node is not None:
        p.append(node)
        node = pr[node]
    return p[::-1]


if __name__ == "__main__":
    edges = [
        ("134", "134", 0.0),
        ("133", "134", 72.5),
        ("134", "133", 72.5),
        ("133", "133", 0.0),
        ("132", "133", 72.5),
        ("133", "132", 72.5),
        ("132", "132", 0.0),
        ("131", "132", 72.5),
        ("114", "132", 93.05),
        ("132", "131", 72.5),
        ("131", "131", 0.0),
        ("130", "131", 168.82),
        ("114", "131", 148.55),
        ("131", "130", 168.82),
        ("130", "130", 0.0),
        ("129", "130", 72.5),
        ("132", "114", 72.5),
        ("114", "114", 0.0),
        ("113", "114", 72.5),
        ("114", "113", 72.5),
        ("113", "113", 0.0),
        ("112", "113", 78.0),
        ("113", "112", 78.0),
        ("112", "112", 0.0),
        ("111", "112", 78.0),
        ("112", "111", 78.0),
        ("111", "111", 0.0),
        ("110", "111", 78.0),
        ("111", "110", 78.0),
        ("110", "110", 0.0),
        ("109", "110", 78.0),
        ("110", "109", 78.0),
        ("109", "109", 0.0),
        ("108", "109", 78.0),
        ("109", "108", 78.0),
        ("108", "108", 0.0),
        ("107", "108", 78.0),
        ("108", "107", 78.0),
        ("107", "107", 0.0),
        ("106", "107", 78.0),
        ("107", "106", 78.0),
        ("106", "106", 0.0),
        ("105", "106", 78.0),
        ("106", "105", 78.0),
        ("105", "105", 0.0),
        ("104", "105", 78.0),
        ("105", "104", 78.0),
        ("104", "104", 0.0),
        ("103", "104", 78.0),
        ("104", "103", 78.0),
        ("103", "103", 0.0),
        ("102", "103", 78.0),
        ("103", "102", 78.0),
        ("102", "102", 0.0),
        ("101", "102", 95.95),
        ("119", "102", 488.751),
        ("118", "102", 397.701),
        ("506", "102", 2093.564),
        ("507", "102", 2151.064),
        ("G7", "102", 1992.165),
        ("102", "101", 95.95),
        ("101", "101", 0.0),
        ("A6", "101", 72.0),
        ("119", "101", 485.201),
        ("118", "101", 394.151),
        ("506", "101", 2090.014),
        ("507", "101", 2147.514),
        ("G7", "101", 1988.615),
        ("101", "A6", 72.0),
        ("A6", "A6", 0.0),
        ("A5", "A6", 72.0),
        ("A6", "A5", 72.0),
        ("A5", "A5", 0.0),
        ("A4", "A5", 61.25),
        ("A5", "A4", 61.25),
        ("A4", "A4", 0.0),
        ("A3", "A4", 56.25),
        ("A4", "A3", 56.25),
        ("A3", "A3", 0.0),
        ("A2", "A3", 69.75),
        ("A3", "A2", 69.75),
        ("A2", "A2", 0.0),
        ("A1", "A2", 58.5),
        ("A2", "A1", 58.5),
        ("A1", "A1", 0.0),
        ("B1", "A1", 174.935),
        ("B2", "A1", 268.493),
        ("C1", "A1", 333.282),
        ("C2", "A1", 438.181),
        ("D1", "A1", 471.07),
        ("130", "129", 72.5),
        ("129", "129", 0.0),
        ("128", "129", 78.0),
        ("129", "128", 78.0),
        ("128", "128", 0.0),
        ("127", "128", 78.0),
        ("128", "127", 78.0),
        ("127", "127", 0.0),
        ("126", "127", 78.0),
        ("127", "126", 78.0),
        ("126", "126", 0.0),
        ("125", "126", 78.0),
        ("126", "125", 78.0),
        ("125", "125", 0.0),
        ("124", "125", 66.0),
        ("125", "124", 66.0),
        ("124", "124", 0.0),
        ("123", "124", 168.0),
        ("124", "123", 168.0),
        ("123", "123", 0.0),
        ("122", "123", 78.0),
        ("123", "122", 78.0),
        ("122", "122", 0.0),
        ("121", "122", 78.0),
        ("122", "121", 78.0),
        ("121", "121", 0.0),
        ("120", "121", 78.0),
        ("121", "120", 78.0),
        ("120", "120", 0.0),
        ("119", "120", 78.0),
        ("102", "119", 488.751),
        ("101", "119", 485.201),
        ("120", "119", 78.0),
        ("119", "119", 0.0),
        ("118", "119", 205.45),
        ("506", "119", 2482.815),
        ("507", "119", 2540.315),
        ("G7", "119", 2381.417),
        ("102", "118", 397.701),
        ("101", "118", 394.151),
        ("119", "118", 205.45),
        ("118", "118", 0.0),
        ("117", "118", 78.0),
        ("506", "118", 2391.765),
        ("507", "118", 2449.265),
        ("G7", "118", 2290.367),
        ("118", "117", 78.0),
        ("117", "117", 0.0),
        ("116", "117", 78.0),
        ("117", "116", 78.0),
        ("116", "116", 0.0),
        ("115", "116", 78.0),
        ("116", "115", 78.0),
        ("115", "115", 0.0),
        ("B5", "115", 284.0),
        ("B6", "115", 346.123),
        ("201", "115", 532.0),
        ("A1", "B1", 174.935),
        ("B1", "B1", 0.0),
        ("B3", "B1", 62.25),
        ("B2", "B1", 213.778),
        ("C1", "B1", 278.713),
        ("C2", "B1", 383.586),
        ("D1", "B1", 416.475),
        ("B1", "B3", 62.25),
        ("B3", "B3", 0.0),
        ("B5", "B3", 67.5),
        ("115", "B5", 284.0),
        ("B3", "B5", 67.5),
        ("B5", "B5", 0.0),
        ("B6", "B5", 160.0),
        ("201", "B5", 345.849),
        ("115", "B6", 346.123),
        ("B5", "B6", 160.0),
        ("B6", "B6", 0.0),
        ("B4", "B6", 67.5),
        ("201", "B6", 284.0),
        ("B6", "B4", 67.5),
        ("B4", "B4", 0.0),
        ("B2", "B4", 62.3),
        ("A1", "B2", 268.493),
        ("B1", "B2", 213.778),
        ("B4", "B2", 62.3),
        ("B2", "B2", 0.0),
        ("C1", "B2", 184.4),
        ("C2", "B2", 289.095),
        ("D1", "B2", 321.984),
        ("A1", "C1", 333.282),
        ("B1", "C1", 278.713),
        ("B2", "C1", 184.4),
        ("C1", "C1", 0.0),
        ("C3", "C1", 76.5),
        ("C2", "C1", 250.815),
        ("D1", "C1", 283.704),
        ("C1", "C3", 76.5),
        ("C3", "C3", 0.0),
        ("C5", "C3", 76.5),
        ("C3", "C5", 76.5),
        ("C5", "C5", 0.0),
        ("C7", "C5", 76.5),
        ("C5", "C7", 76.5),
        ("C7", "C7", 0.0),
        ("C9", "C7", 76.5),
        ("C7", "C9", 76.5),
        ("C9", "C9", 0.0),
        ("203", "C9", 422.585),
        ("S101", "C9", 1056.546),
        ("S102", "C9", 1133.5),
        ("S127", "C9", 1930.561),
        ("S128", "C9", 2007.782),
        ("C10", "C9", 159.6),
        ("304", "C9", 502.085),
        ("E9", "C9", 906.52),
        ("E10", "C9", 969.57),
        ("403", "C9", 1296.293),
        ("115", "201", 532.0),
        ("B5", "201", 345.849),
        ("B6", "201", 284.0),
        ("201", "201", 0.0),
        ("202", "201", 78.0),
        ("201", "202", 78.0),
        ("202", "202", 0.0),
        ("203", "202", 78.0),
        ("C9", "203", 422.6),
        ("202", "203", 78.0),
        ("203", "203", 0.0),
        ("S101", "203", 805.5),
        ("S102", "203", 882.5),
        ("S127", "203", 2257.297),
        ("S128", "203", 2333.03),
        ("C10", "203", 485.034),
        ("304", "203", 827.085),
        ("E9", "203", 1232.6),
        ("E10", "203", 1294.706),
        ("403", "203", 1620.6),
        ("C9", "S101", 1056.546),
        ("203", "S101", 805.5),
        ("S101", "S101", 0.0),
        ("S102", "S101", 291.0),
        ("S103", "S101", 72.5),
        ("S127", "S101", 2859.4),
        ("S128", "S101", 2951.4),
        ("C10", "S101", 1119.243),
        ("304", "S101", 1460.985),
        ("E9", "S101", 1865.009),
        ("E10", "S101", 1928.48),
        ("403", "S101", 2254.5),
        ("C9", "S102", 1133.5),
        ("203", "S102", 882.5),
        ("S101", "S102", 291.0),
        ("S102", "S102", 0.0),
        ("S104", "S102", 72.5),
        ("S127", "S102", 2951.4),
        ("S128", "S102", 3043.4),
        ("C10", "S102", 1181.244),
        ("304", "S102", 1522.985),
        ("E9", "S102", 1927.006),
        ("E10", "S102", 1990.48),
        ("403", "S102", 2316.5),
        ("S101", "S103", 72.5),
        ("S103", "S103", 0.0),
        ("S105", "S103", 77.0),
        ("S102", "S104", 72.5),
        ("S104", "S104", 0.0),
        ("S106", "S104", 77.0),
        ("S103", "S105", 77.0),
        ("S105", "S105", 0.0),
        ("S106", "S105", 194.1),
        ("S107", "S105", 72.5),
        ("S108", "S105", 164.5),
        ("S104", "S106", 77.0),
        ("S105", "S106", 194.1),
        ("S106", "S106", 0.0),
        ("S107", "S106", 164.5),
        ("S108", "S106", 72.5),
        ("S105", "S107", 72.5),
        ("S106", "S107", 164.5),
        ("S107", "S107", 0.0),
        ("S108", "S107", 134.9),
        ("S109", "S107", 72.5),
        ("S105", "S108", 164.5),
        ("S106", "S108", 72.5),
        ("S107", "S108", 134.9),
        ("S108", "S108", 0.0),
        ("S110", "S108", 72.5),
        ("S107", "S109", 72.5),
        ("S109", "S109", 0.0),
        ("S111", "S109", 84.5),
        ("S108", "S110", 72.5),
        ("S110", "S110", 0.0),
        ("S112", "S110", 84.5),
        ("S109", "S111", 84.5),
        ("S111", "S111", 0.0),
        ("S112", "S111", 249.5),
        ("S113", "S111", 89.0),
        ("S114", "S111", 181.0),
        ("S110", "S112", 84.5),
        ("S111", "S112", 249.5),
        ("S112", "S112", 0.0),
        ("S113", "S112", 181.0),
        ("S114", "S112", 89.0),
        ("S111", "S113", 89.0),
        ("S112", "S113", 181.0),
        ("S113", "S113", 0.0),
        ("S114", "S113", 112.5),
        ("S115", "S113", 89.0),
        ("S111", "S114", 181.0),
        ("S112", "S114", 89.0),
        ("S113", "S114", 112.5),
        ("S114", "S114", 0.0),
        ("S116", "S114", 89.0),
        ("S113", "S115", 89.0),
        ("S115", "S115", 0.0),
        ("S116", "S115", 112.5),
        ("S117", "S115", 89.0),
        ("S118", "S115", 181.0),
        ("S114", "S116", 89.0),
        ("S115", "S116", 112.5),
        ("S116", "S116", 0.0),
        ("S117", "S116", 181.0),
        ("S118", "S116", 89.0),
        ("S115", "S117", 89.0),
        ("S116", "S117", 181.0),
        ("S117", "S117", 0.0),
        ("S118", "S117", 249.5),
        ("S119", "S117", 84.5),
        ("S115", "S118", 181.0),
        ("S116", "S118", 89.0),
        ("S117", "S118", 249.5),
        ("S118", "S118", 0.0),
        ("S120", "S118", 84.5),
        ("S117", "S119", 84.5),
        ("S119", "S119", 0.0),
        ("S121", "S119", 72.5),
        ("S118", "S120", 84.5),
        ("S120", "S120", 0.0),
        ("S122", "S120", 72.5),
        ("S119", "S121", 72.5),
        ("S121", "S121", 0.0),
        ("S122", "S121", 134.343),
        ("S123", "S121", 72.5),
        ("S124", "S121", 164.5),
        ("S120", "S122", 72.5),
        ("S121", "S122", 134.343),
        ("S122", "S122", 0.0),
        ("S123", "S122", 164.5),
        ("S124", "S122", 72.5),
        ("S121", "S123", 72.5),
        ("S122", "S123", 164.5),
        ("S123", "S123", 0.0),
        ("S124", "S123", 194.657),
        ("S125", "S123", 77.0),
        ("S121", "S124", 164.5),
        ("S122", "S124", 72.5),
        ("S123", "S124", 194.657),
        ("S124", "S124", 0.0),
        ("S126", "S124", 77.0),
        ("S123", "S125", 77.0),
        ("S125", "S125", 0.0),
        ("S127", "S125", 72.5),
        ("S124", "S126", 77.0),
        ("S126", "S126", 0.0),
        ("S128", "S126", 72.5),
        ("C9", "S127", 1930.561),
        ("203", "S127", 2257.297),
        ("S101", "S127", 2889.415),
        ("S102", "S127", 2951.395),
        ("S125", "S127", 72.5),
        ("S127", "S127", 0.0),
        ("S128", "S127", 293.0),
        ("C10", "S127", 1869.228),
        ("304", "S127", 1522.774),
        ("E9", "S127", 1120.88),
        ("E10", "S127", 1058.88),
        ("403", "S127", 804.896),
        ("C9", "S128", 1992.561),
        ("203", "S128", 2317.607),
        ("S101", "S128", 2951.415),
        ("S102", "S128", 3013.405),
        ("S126", "S128", 72.5),
        ("S127", "S128", 293.0),
        ("S128", "S128", 0.0),
        ("C10", "S128", 1931.228),
        ("304", "S128", 1584.774),
        ("E9", "S128", 1182.88),
        ("E10", "S128", 1120.88),
        ("403", "S128", 866.893),
        ("C9", "C10", 159.6),
        ("203", "C10", 485.034),
        ("S101", "C10", 1119.243),
        ("S102", "C10", 1181.244),
        ("S127", "C10", 1869.228),
        ("S128", "C10", 1945.752),
        ("C10", "C10", 0.0),
        ("C8", "C10", 76.5),
        ("304", "C10", 440.085),
        ("E9", "C10", 844.1),
        ("E10", "C10", 906.1),
        ("403", "C10", 1233.6),
        ("C10", "C8", 76.5),
        ("C8", "C8", 0.0),
        ("C6", "C8", 76.5),
        ("C8", "C6", 76.5),
        ("C6", "C6", 0.0),
        ("C4", "C6", 76.5),
        ("C6", "C4", 76.5),
        ("C4", "C4", 0.0),
        ("C2", "C4", 76.5),
        ("A1", "C2", 438.181),
        ("B1", "C2", 383.586),
        ("B2", "C2", 289.095),
        ("C1", "C2", 250.815),
        ("C4", "C2", 76.5),
        ("C2", "C2", 0.0),
        ("D1", "C2", 183.051),
        ("A1", "D1", 471.07),
        ("B1", "D1", 416.475),
        ("B2", "D1", 321.984),
        ("C1", "D1", 283.704),
        ("C2", "D1", 183.051),
        ("D1", "D1", 0.0),
        ("D2", "D1", 69.8),
        ("D1", "D2", 69.8),
        ("D2", "D2", 0.0),
        ("D3", "D2", 72.0),
        ("D2", "D3", 72.0),
        ("D3", "D3", 0.0),
        ("D4", "D3", 76.5),
        ("D3", "D4", 76.5),
        ("D4", "D4", 0.0),
        ("D5", "D4", 97.5),
        ("305", "D4", 315.0),
        ("D4", "D5", 97.5),
        ("D5", "D5", 0.0),
        ("D6", "D5", 69.0),
        ("305", "D5", 250.6),
        ("D5", "D6", 69.0),
        ("D6", "D6", 0.0),
        ("D7", "D6", 72.0),
        ("D6", "D7", 72.0),
        ("D7", "D7", 0.0),
        ("D8", "D7", 69.8),
        ("D7", "D8", 69.8),
        ("D8", "D8", 0.0),
        ("E1", "D8", 184.8),
        ("E2", "D8", 292.59),
        ("F1", "D8", 324.497),
        ("F2", "D8", 425.479),
        ("G1", "D8", 476.517),
        ("D4", "301", 315.0),
        ("D5", "301", 250.6),
        ("301", "301", 0.0),
        ("305", "301", 122.0),
        ("301", "302", 78.0),
        ("302", "302", 0.0),
        ("302", "303", 78.0),
        ("303", "303", 0.0),
        ("303", "304", 78.0),
        ("304", "304", 0.0),
        ("305", "305", 0.0),
        ("306", "305", 78.0),
        ("306", "306", 0.0),
        ("307", "306", 78.0),
        ("307", "307", 0.0),
        ("308", "307", 78.0),
        ("C9", "308", 562.1),
        ("203", "308", 887.101),
        ("S101", "308", 1520.98),
        ("S102", "308", 1582.98),
        ("S127", "308", 1448.0),
        ("S128", "308", 1540.046),
        ("C10", "308", 500.101),
        ("304", "308", 154.6),
        ("308", "308", 0.0),
        ("E9", "308", 440.1),
        ("E10", "308", 502.086),
        ("403", "308", 828.1),
        ("D8", "E1", 184.8),
        ("E1", "E1", 0.0),
        ("E3", "E1", 76.5),
        ("E2", "E1", 257.169),
        ("F1", "E1", 289.075),
        ("F2", "E1", 390.04),
        ("G1", "E1", 441.096),
        ("E1", "E3", 76.5),
        ("E3", "E3", 0.0),
        ("E5", "E3", 76.5),
        ("E3", "E5", 76.5),
        ("E5", "E5", 0.0),
        ("E7", "E5", 76.5),
        ("E5", "E7", 76.5),
        ("E7", "E7", 0.0),
        ("E9", "E7", 76.5),
        ("C9", "E9", 907.57),
        ("203", "E9", 1232.6),
        ("S101", "E9", 1866.48),
        ("S102", "E9", 1928.48),
        ("S127", "E9", 1105.5),
        ("S128", "E9", 1197.545),
        ("C10", "E9", 844.1),
        ("304", "E9", 500.085),
        ("E7", "E9", 76.5),
        ("E9", "E9", 0.0),
        ("E10", "E9", 159.6),
        ("403", "E9", 485.457),
        ("C9", "E10", 969.57),
        ("203", "E10", 1294.706),
        ("S101", "E10", 1928.48),
        ("S102", "E10", 1990.48),
        ("S127", "E10", 1043.5),
        ("S128", "E10", 1135.545),
        ("C10", "E10", 906.1),
        ("304", "E10", 562.085),
        ("E9", "E10", 159.6),
        ("E10", "E10", 0.0),
        ("E8", "E10", 76.5),
        ("403", "E10", 423.6),
        ("E10", "E8", 76.5),
        ("E8", "E8", 0.0),
        ("E6", "E8", 76.5),
        ("E8", "E6", 76.5),
        ("E6", "E6", 0.0),
        ("E4", "E6", 76.5),
        ("E6", "E4", 76.5),
        ("E4", "E4", 0.0),
        ("E2", "E4", 76.5),
        ("D8", "E2", 292.59),
        ("E1", "E2", 257.169),
        ("E4", "E2", 76.5),
        ("E2", "E2", 0.0),
        ("F1", "E2", 181.8),
        ("F2", "E2", 282.735),
        ("G1", "E2", 333.773),
        ("D8", "F1", 324.497),
        ("E1", "F1", 289.075),
        ("E2", "F1", 181.8),
        ("F1", "F1", 0.0),
        ("F3", "F1", 60.8),
        ("F2", "F1", 228.883),
        ("G1", "F1", 279.94),
        ("F1", "F3", 60.8),
        ("F3", "F3", 0.0),
        ("F5", "F3", 67.5),
        ("F3", "F5", 67.5),
        ("F5", "F5", 0.0),
        ("401", "F5", 284.5),
        ("F6", "F5", 162.5),
        ("502", "F5", 347.366),
        ("F5", "401", 284.5),
        ("401", "401", 0.0),
        ("402", "401", 78.0),
        ("F6", "401", 346.887),
        ("502", "401", 532.0),
        ("401", "402", 78.0),
        ("402", "402", 0.0),
        ("403", "402", 78.0),
        ("C9", "403", 1295.57),
        ("203", "403", 1620.6),
        ("S101", "403", 2254.48),
        ("S102", "403", 2316.48),
        ("S127", "403", 791.5),
        ("S128", "403", 883.5),
        ("C10", "403", 1233.6),
        ("304", "403", 887.664),
        ("E9", "403", 485.107),
        ("E10", "403", 423.6),
        ("402", "403", 78.0),
        ("403", "403", 0.0),
        ("F5", "F6", 162.5),
        ("401", "F6", 346.887),
        ("F6", "F6", 0.0),
        ("F4", "F6", 67.5),
        ("502", "F6", 284.887),
        ("F6", "F4", 67.5),
        ("F4", "F4", 0.0),
        ("F2", "F4", 60.8),
        ("D8", "F2", 425.479),
        ("E1", "F2", 390.04),
        ("E2", "F2", 282.735),
        ("F1", "F2", 228.883),
        ("F4", "F2", 60.8),
        ("F2", "F2", 0.0),
        ("G1", "F2", 175.1),
        ("D8", "G1", 476.517),
        ("E1", "G1", 441.096),
        ("E2", "G1", 333.773),
        ("F1", "G1", 279.94),
        ("F2", "G1", 175.1),
        ("G1", "G1", 0.0),
        ("G2", "G1", 76.5),
        ("G1", "G2", 76.5),
        ("G2", "G2", 0.0),
        ("G3", "G2", 76.5),
        ("G2", "G3", 76.5),
        ("G3", "G3", 0.0),
        ("G4", "G3", 76.5),
        ("G3", "G4", 76.5),
        ("G4", "G4", 0.0),
        ("G5", "G4", 76.5),
        ("G4", "G5", 76.5),
        ("G5", "G5", 0.0),
        ("501", "G5", 76.5),
        ("G5", "501", 76.5),
        ("501", "501", 0.0),
        ("505", "501", 416.8),
        ("506", "501", 427.9),
        ("G7", "501", 121.947),
        ("F5", "502", 347.366),
        ("401", "502", 532.0),
        ("F6", "502", 284.887),
        ("502", "502", 0.0),
        ("503", "502", 78.0),
        ("502", "503", 78.0),
        ("503", "503", 0.0),
        ("504", "503", 78.0),
        ("503", "504", 78.0),
        ("504", "504", 0.0),
        ("505", "504", 78.0),
        ("501", "505", 416.8),
        ("504", "505", 78.0),
        ("505", "505", 0.0),
        ("506", "505", 291.5),
        ("G7", "505", 409.406),
        ("102", "506", 2093.564),
        ("101", "506", 2090.014),
        ("119", "506", 2482.815),
        ("118", "506", 2391.765),
        ("501", "506", 427.9),
        ("505", "506", 291.5),
        ("506", "506", 0.0),
        ("507", "506", 78.0),
        ("G7", "506", 326.784),
        ("102", "507", 2151.064),
        ("101", "507", 2147.514),
        ("119", "507", 2540.315),
        ("118", "507", 2449.265),
        ("506", "507", 78.0),
        ("507", "507", 0.0),
        ("508", "507", 78.0),
        ("G7", "507", 384.284),
        ("507", "508", 78.0),
        ("508", "508", 0.0),
        ("509", "508", 78.0),
        ("508", "509", 78.0),
        ("509", "509", 0.0),
        ("510", "509", 78.0),
        ("509", "510", 78.0),
        ("510", "510", 0.0),
        ("511", "510", 78.0),
        ("510", "511", 78.0),
        ("511", "511", 0.0),
        ("512", "511", 78.0),
        ("511", "512", 78.0),
        ("512", "512", 0.0),
        ("513", "512", 78.0),
        ("512", "513", 78.0),
        ("513", "513", 0.0),
        ("514", "513", 78.0),
        ("513", "514", 78.0),
        ("514", "514", 0.0),
        ("515", "514", 78.0),
        ("514", "515", 78.0),
        ("515", "515", 0.0),
        ("516", "515", 78.0),
        ("515", "516", 78.0),
        ("516", "516", 0.0),
        ("517", "516", 78.0),
        ("516", "517", 78.0),
        ("517", "517", 0.0),
        ("518", "517", 78.0),
        ("517", "518", 78.0),
        ("518", "518", 0.0),
        ("519", "518", 78.0),
        ("518", "519", 78.0),
        ("519", "519", 0.0),
        ("520", "519", 78.0),
        ("519", "520", 78.0),
        ("520", "520", 0.0),
        ("521", "520", 78.0),
        ("520", "521", 78.0),
        ("521", "521", 0.0),
        ("522", "521", 78.0),
        ("521", "522", 78.0),
        ("522", "522", 0.0),
        ("523", "522", 78.0),
        ("522", "523", 78.0),
        ("523", "523", 0.0),
        ("524", "523", 78.0),
        ("523", "524", 78.0),
        ("524", "524", 0.0),
        ("525", "524", 78.0),
        ("524", "525", 78.0),
        ("525", "525", 0.0),
        ("102", "G7", 1992.165),
        ("101", "G7", 1988.615),
        ("119", "G7", 2381.417),
        ("118", "G7", 2290.367),
        ("501", "G7", 121.947),
        ("505", "G7", 409.406),
        ("506", "G7", 326.784),
        ("507", "G7", 384.284),
        ("G7", "G7", 0.0),
    ]

    g = build_graph(edges)

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import json
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import statistics
from itertools import chain, combinations
import psycopg2
from psycopg2 import Error

print("!!!!Start")
print("current time:-", dt.now())

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="HpboOFRzmUlEFtPjWZvYTDFNNKuxMavN",
                                  password="aqTKjhGTvyfRHSfaoG2IBcE9D3vFWOHN22btHNrTFaWSTgEIyyKsepMHrMctz4Eh",
                                  host="localhost",
                                  port="5431",
                                  database="agos_server")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Executing a SQL query
    # cursor.execute("select * from public.flight_info_flightinfo where schedule_flight_time >= '2022-05-26 11:00:00' and radio_group_id = 1 and canceled ='FALSE' and type ='DEP' and finished = 'False';")
    cursor.execute("select * from public.flight_flight where schedule_flight_time >= '2023-04-01 10:00:00' and canceled ='FALSE' and type ='DEP';")
    # Fetch result
    record = cursor.fetchall()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()

def AddnewCol(XX, col_name):
    Temp = []
    for x in XX['flight_number']:
        Temp.append("")
    XX[col_name] = Temp
    return XX


def tractor_stat(wp):
    ts = wp.groupby('Tractor').count()
    ts = ts.iloc[:, :1]
    ts.columns = ['No. of Flights']
    ts = ts.sort_values(by='No. of Flights', ascending=False)
    ts = ts.reset_index()
    b = 0
    Temp = []
    for y in range(len(ts)):
        T1 = wp[wp['Tractor'] == ts['Tractor'][b]]
        T1.reset_index(drop=True, inplace=True)
        a = 0
        tot_distance = 0
        for x in range(len(T1)):
            if str(T1['bay'][a]) != 'nan':
                if a == 0:
                    d, prev = dijkstra(g, 'G7', str(T1['bay'][a]))
                    tot_distance = tot_distance + d
                elif a == len(T1):
                    d, prev = dijkstra(g, str(T1['bay'][a]), 'G7')
                    tot_distance = tot_distance + d
                else:
                    if str(T1['bay'][a - 1]) != 'nan':
                        d, prev = dijkstra(g, str(T1['bay'][a - 1]), str(T1['bay'][a]))
                        tot_distance = tot_distance + d
                    else:
                        tot_distance = tot_distance + Das_Out['Distance'].mean()
            else:
                tot_distance = tot_distance + Das_Out['Distance'].mean()
            a += 1
        Temp.append(tot_distance)
        b += 1
    ts['Total Distance'] = Temp
    return ts


def working_time(start, dest):
    wort_t = wt_minute
    wt_dist, prev = dijkstra(g, start, dest)
    if wt_dist < 1250:
        wort_t = wt_minute+timedelta(minutes=5)
    elif wt_dist < 2500:
        wort_t = wt_minute+timedelta(minutes=7.5)
    elif wt_dist < 3750:
        wort_t = wt_minute+timedelta(minutes=10)
    else:
        wort_t = wt_minute+timedelta(minutes=12.5)

    return wort_t


def assign_best_GSE(flt, das, tractor):
    #print(tractor.columns)
    tractor['Des_Bay'] = tractor['Des_Bay'].fillna('G7')
    sla = sla_minute
    wt = wt_minute
    des_bay = das.loc[(das.flight_number == flt), 'bay'].iloc[0]
    b = 0
    for x in tractor['Tractor_ID']:
        d, prev = dijkstra(g, str(tractor['Des_Bay'][b]), des_bay)
        tractor['Distance'][b] = d
        b = b + 1
    des_AC = das.loc[(das.flight_number == flt), 'aircraft'].iloc[0]
    tractor = tractor.sort_values(by=['Flight_counter', 'Distance', 'Tractor_type'], ascending=[True, True, False])
    if des_AC.startswith('32') or des_AC.startswith('73') or des_AC.startswith('31'):
        tractor = tractor.sort_values(by='A320', ascending=False)
    elif des_AC.startswith('33') or des_AC.startswith('34') or des_AC.startswith('35'):
        tractor = tractor.sort_values(by='A330', ascending=False)
    elif des_AC.startswith('75') or des_AC.startswith('76'):
        tractor = tractor.sort_values(by='B757', ascending=False)
    elif des_AC.startswith('38'):
        tractor = tractor.sort_values(by='A380', ascending=False)
    elif des_AC.startswith('78'):
        tractor = tractor.sort_values(by='B787', ascending=False)
    elif des_AC.startswith('77'):
        tractor = tractor.sort_values(by='B777', ascending=False)
    elif des_AC.startswith('747'):
        tractor = tractor.sort_values(by='B747', ascending=False)
    elif des_AC.startswith('748'):
        tractor = tractor.sort_values(by='B748', ascending=False)
    elif des_AC.startswith('E'):
        tractor = tractor.sort_values(by='E90', ascending=False)
    else:
        tractor = tractor.sort_values(by='Tractor_size', ascending=True)
    # ---------------------------------------
    # if des_AC.startswith('32')|des_AC.startswith('73')|des_AC.startswith('31'):
    #    tractor = tractor.sort_values(by='Tractor_size', ascending=False)
    # print(tractor)
    # else:
    #    tractor = tractor.sort_values(by='Tractor_size', ascending=True)

    # -----------------------------------------
    #zin 21/6/23 test ass tractor
    #tractor = tractor.reset_index(drop=True)
    #print('des ac  ' + des_AC)
    #print(tractor)
    # flight's start time
    slct_flt_start_time = das.loc[(das.flight_number == flt), 'Time'].iloc[0] - sla
    # Tractor Inuse Check
    c = 0
    for y in tractor['Tractor_ID']:
        dd = int(len(das.loc[(das.Tractor == tractor['Tractor_ID'][c]), 'Time'].reset_index(drop=True)))
        if int(len(das.loc[(das.Tractor == tractor['Tractor_ID'][c]), 'Time'].reset_index(drop=True))) > 0:
            prev_flt_stop_time = das.loc[(das.Tractor == tractor['Tractor_ID'][c]), 'Time'].reset_index(drop=True).iloc[
                                     -1] + working_time(tractor.Des_Bay[c], des_bay)
            if prev_flt_stop_time <= slct_flt_start_time:
                tractor.loc[(tractor.Tractor_ID == tractor['Tractor_ID'][c]), 'Tractor_inuse'] = 'No'
            else:
                tractor.loc[(tractor.Tractor_ID == tractor['Tractor_ID'][c]), 'Tractor_inuse'] = 'Yes'
        else:
            tractor.loc[(tractor.Tractor_ID == tractor['Tractor_ID'][c]), 'Tractor_inuse'] = 'No'
        c = c + 1
    tractor = tractor.sort_values(by='Tractor_inuse', ascending=True)
    tractor = tractor.reset_index(drop=True)
    if tractor['Tractor_inuse'].loc[(tractor.Tractor_inuse == 'No')].count() != 0:
        das.loc[(das.flight_number == flt), 'Tractor'] = tractor.Tractor_ID[0]
        #print('this is flight  '+flt+' >>>> '+tractor.Tractor_ID[0]+' >>> '+des_AC)
        # Increase Flight_counter
        tractor.Flight_counter[0] = tractor.Flight_counter[0] + 1
    else:
        das.loc[(das.flight_number == flt), 'Tractor'] = 'No GSE AVA'
    tractor.Prev_flight[0] = tractor.Des_flight[0]
    tractor.Last_location[0] = tractor.Des_Bay[0]
    tractor.Des_flight[0] = flt
    tractor.Des_Bay[0] = das.loc[(das.flight_number == flt), 'bay'].iloc[0]
    return tractor, das


# Generate possible combination of vehicle
def find_combination(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def powerset(iterable, minlength ,maxlength):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    #return chain.from_iterable(combinations(s, r) for r in range(minlength, len(s)+1))
    return chain.from_iterable(combinations(s, r) for r in range(minlength, maxlength + 1))

def generate_combinations(min_size, max_size, L_size, M_size):
    combinations = []
    for total in range(min_size, max_size + 1):
        for l in range(min(L_size, total + 1)):
            m = total - l
            if m <= M_size:
                combinations.append((l, m))
    return combinations

def find_opt_num_GSE(df_gse_predict):
    density = df_gse_predict['flight_number'].groupby(df_gse_predict["Time"].dt.hour).count()
    print(np.std(density))
    if np.std(density) <= 1.9:  # narrowspread
        #return density.max(), int(density.mean())
        #return density.max(), int((density.max() - density.mean()) / 2 + density.mean())
        return density.max(), int((density.max() - density.mean()) / 2 + density.mean())
    if np.std(density) > 1.9 and np.std(density) < 4.0:  # widespread
        #return density.max(), int((density.max() - density.mean()) / 2 + density.mean())
        return density.max()-2, int((density.max() - density.mean()) / 2 + density.mean()) -3
    if np.std(density) >= 4.0 and np.std(density) < 4.1:  # widespread
        return density.max() - 4, int((density.max() - density.mean()) / 2 + density.mean()) - 3
    if np.std(density) >= 4.1:  # widespread
        return density.max() - 2, int((density.max() - density.mean()) / 2 + density.mean()) - 3


def reduce_sim(sim_com, dff):
    max_GSE, mean_GSE = find_opt_num_GSE(dff)
    sim_com = sim_com[(sim_com.TotalGSE <= max_GSE) & (sim_com.TotalGSE >= mean_GSE)]
    sim_com = sim_com.reset_index(drop=True)
    return sim_com


def sizecount(comb, tractor, p):
    m_act = 0
    l_act = 0
    m_att = 0
    l_att = 0
    f = 0
    for w in range(len(comb.Combo[p])):
        aim = tractor.loc[tractor.Tractor_ID == comb.Combo[p][f]].index.tolist()
        if tractor.iloc[aim[0], 3] == 'Medium':
            if tractor.iloc[aim[0], 4] == 'ACT Conventional Pushback':
                m_act += 1
            if tractor.iloc[aim[0], 4] == 'ATT Towbarless Pushback':
                m_att += 1
        if tractor.iloc[aim[0], 3] == 'Large':
            if tractor.iloc[aim[0], 4] == 'ACT Conventional Pushback':
                l_act += 1
            if tractor.iloc[aim[0], 4] == 'ATT Towbarless Pushback':
                l_att += 1
        f = f + 1
    return m_act, l_act, m_att, l_att

def sizecountML(comb, tractor, p):
    m = 0
    l = 0
    f = 0
    for w in range(len(comb.Combo[p])):
        aim = tractor.loc[tractor.Tractor_ID == comb.Combo[p][f]].index.tolist()
        if tractor.iloc[aim[0], 3] == 'Medium':
            m+=1
        if tractor.iloc[aim[0], 3] == 'Large':
            l+=1
        f = f + 1
    return m,l


def combine_tractor(tr, last_tr):
    ax = 0
    for i in last_tr['Tractor_ID']:
        bx = tr.loc[(tr.Tractor_ID == last_tr['Tractor_ID'][ax])].index
        tr['Last_location'][bx] = last_tr['Last_location'][ax]
        # tr['Flight_counter'][bx] = tr['Flight_counter'][bx] + last_tr['Flight_counter'][ax]
        tr['Flight_counter'][bx] = last_tr['Flight_counter'][ax]
        tr['Prev_flight'][bx] = last_tr['Prev_flight'][ax]
        tr['Des_flight'][bx] = last_tr['Des_flight'][ax]
        tr['Des_Bay'][bx] = last_tr['Des_Bay'][ax]
        tr['Distance'][bx] = last_tr['Distance'][ax]
        tr['Tractor_inuse'][bx] = last_tr['Tractor_inuse'][ax]
        ax = ax + 1
    return tr

df_raws = pd.DataFrame(record, columns=['id','ac_register','actual_flight_time', 'aircraft', 'bay', 'belt', 'departure_date','estimate_flight_time', 'flight_number', 'gate','next_station', 'schedule_flight_time','sequence','canceled','finished', 'working', 'created_at', 'updated_at', 'booking_pax','prev_station','type'])
df_raws = df_raws.replace(r'^s*$', float('NaN'), regex = True)

#Filter Shift in UTC TIME

#now = '2022-07-01 09:00:00'
now = dt.utcnow()

# Next 1 Hour
now_start = now - timedelta(hours=2)
now_stop = now + timedelta(hours=8)

#Define SLA
sla_minute = timedelta(minutes=10)

#Define working time + travel time = wt
wt_minute = timedelta(minutes=10)


# Read Input File
Tractor = pd.read_excel(r"C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor.xlsx", index_col=0)
ReqTimeInput = pd.read_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ReqTime.txt', delimiter=';')
ReqTimeInput = ReqTimeInput.drop_duplicates(subset=['flight'], keep='last')
ReqTimeInput = ReqTimeInput.astype({'Time':'datetime64[ns]'})

# manage Time format
# Ascending Start Time
df_raws = df_raws.reset_index()
# splitting 'updated_at' drop+07
df_raws[['UPDATE', 'D']] = df_raws.updated_at.apply(
    lambda x: pd.Series(str(x).split("+")))
df_raws = df_raws.drop(columns=['D', 'updated_at'])
# splitting 'schedule_flight_time' drop+07
df_raws[['STD', 'D']] = df_raws.schedule_flight_time.apply(
    lambda x: pd.Series(str(x).split("+")))
df_raws[['ETD','E']] = df_raws.estimate_flight_time.apply(
   lambda x: pd.Series(str(x).split("+")))
df_raws = df_raws.drop(columns=['E'])
df_raws = df_raws.astype({'UPDATE': 'datetime64[ns]'})
df_raws = df_raws.astype({'STD': 'datetime64[ns]'})
df_raws = df_raws.astype({'ETD': 'datetime64[ns]'})
#df_raws.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ssraw.csv')
# filter Data
#filter Data
AA =df_raws[(df_raws['STD']>= now_start) & (df_raws['STD']< now_stop)]
BB =df_raws[(df_raws['ETD']>= now_start) & (df_raws['ETD']< now_stop)]
df_raws = pd.concat([AA,BB])
# please remove this line ,set for avoid nan in ac type bug
# df_raws = df_raws.dropna(subset = ["aircraft"], inplace=True)
# prevernt flight duplicate Keep lat update
df_unique = df_raws.drop_duplicates(subset=['flight_number'], keep='last')
# Ascending Start Time
df_unique = df_unique.sort_values(by=['STD'], ascending=True)
df_unique = df_unique.reset_index(drop=True)
# Create START and Finish Time
#df_unique['START'] = df_unique['STD'] - sla_minute
#df_unique['FINISH'] = df_unique['STD'] + wt_minute
df_input = df_unique

# Clean Remote bay Size such as 112R,503L to 112,503
a = 0
for x in df_input['flight_number']:
    if str(df_input['bay'][a]) != 'nan':
        if str(df_input['bay'][a]).startswith('1') | str(df_input['bay'][a]).startswith('2') | str(
                df_input['bay'][a]).startswith('3') | str(df_input['bay'][a]).startswith('4') | str(
                df_input['bay'][a]).startswith('5'):
            df_input['bay'][a] = str(df_input['bay'][a])[0:3]
    a = a + 1


Tractor_Out = Tractor.reset_index().copy()
Tractor = Tractor.loc[(Tractor.Tractor_ava == 'Yes')].reset_index()
df_das = df_input[
    ['flight_number', 'aircraft', 'ac_register', 'bay', 'estimate_flight_time', 'working', 'actual_flight_time',
     'schedule_flight_time']]
df_das = AddnewCol(df_das, 'Req_time')
df_das = AddnewCol(df_das, 'Time')
df_das = AddnewCol(df_das, 'Tractor')
df_das.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\raw.csv')
df_das['Req_time'] = df_das['estimate_flight_time']
df_das['Time'] = df_das['estimate_flight_time']
df_das.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\rraw.csv')
df_das['Time'] = df_das['Time'].fillna(df_das['schedule_flight_time'])
df_das.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\rrraw.csv')
df_das = df_das.sort_values(by=['Time'], ascending=True)
df_das = df_das.reset_index(drop=True)
df_das_raw = df_das.copy()



print("!!!!before sim")
print("current time:-", dt.now())

stuff = list(Tractor['Tractor_ID'])
#data_s = {'Combo': [], 'TotalDistance': [], 'TotalGSE': [], 'M_ACT': [], 'L_ACT': [], 'M_ATT': [], 'L_ATT': []}
data_s = {'Combo': [], 'TotalDistance': [], 'TotalGSE': [], 'M': [], 'L': []}
sim = pd.DataFrame(data_s)
max_GSE2, mean_GSE2 = find_opt_num_GSE(df_das)
print(max_GSE2)
print(mean_GSE2)
M_count = Tractor['Tractor_ID'].loc[(Tractor['Tractor_size'] == 'Medium')].count()
L_count = Tractor['Tractor_ID'].loc[(Tractor['Tractor_size'] == 'Large')].count()

"""
print("!!!! START Comb_Poom")
print("current time:-", dt.now())
combi = generate_combinations(mean_GSE2, max_GSE2, L_count, M_count)
print(combi)
rc=0
print(Tractor)
for total, (ll, mm) in enumerate(combi, mean_GSE2):
    print(f"case total {ll+mm} [(L size:{ll}),(M size:{mm})]")
    lc=0
    mc=0
    combo = []
    for idx, (key, value) in enumerate(Tractor['Tractor_ID'].items()):
        if lc+mc < ll+mm:
            if (Tractor['Tractor_size'][idx] == 'Large') & (lc < ll):
                combo.append(Tractor['Tractor_ID'][idx])
                lc+=1
            if (Tractor['Tractor_size'][idx] == 'Medium') & (mc < mm):
                combo.append(Tractor['Tractor_ID'][idx])
                mc+=1
    log = {'Combo': [combo], 'TotalDistance': [0], 'TotalGSE': ll+mm, 'M': mm, 'L': ll}
    app_log = pd.DataFrame(log)
    sim = sim.append(app_log)
    rc+=1
"""
#sim = sim.reset_index(drop=True)
#sim.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\sim_unique_p.csv')
#print("combooooooooooooo")
#print(sim)

print("!!!!Comb_stuff")
print("current time:-", dt.now())

"""
#for i, combo in enumerate(find_combination(stuff), 1):
for i, combo in enumerate(powerset(stuff,mean_GSE2), 1):
    log = {'Combo': [combo], 'TotalDistance': [0], 'TotalGSE': [len(combo)], 'M_ACT': [0], 'L_ACT': [0], 'M_ATT': [0],
           'L_ATT': [0]}
    app_log = pd.DataFrame(log)
    sim = sim.append(app_log)
"""
#for i, combo in enumerate(find_combination(stuff), 1):
#for i, combo in enumerate(powerset(stuff,mean_GSE2), 1):

for i, combo in enumerate(powerset(stuff,mean_GSE2,max_GSE2), 1):
    log = {'Combo': [combo], 'TotalDistance': [0], 'TotalGSE': [len(combo)], 'M': [0], 'L': [0]}
    app_log = pd.DataFrame(log)
    m = 0
    l = 0
    for w in range(len(app_log['Combo'][0])):
        aim = Tractor.loc[Tractor.Tractor_ID == app_log['Combo'][0][w]].index.tolist()
        if Tractor.iloc[aim[0], 3] == 'Medium':
            m += 1
        if Tractor.iloc[aim[0], 3] == 'Large':
            l += 1
    app_log['M']=m
    app_log['L']=l
    sim = sim.append(app_log)
sim = sim.reset_index(drop=True)
print(sim.count())
sim = reduce_sim(sim, df_das)
print(sim)
print(sim.count())

sim_unique = sim.copy()


d = 0
"""for i in range(int(len(sim_unique['Combo']))):
    M_act, L_act, M_att, L_att = sizecount(sim_unique, Tractor, d)
    sim_unique['M_ACT'][d] = M_act
    sim_unique['L_ACT'][d] = L_act
    sim_unique['M_ATT'][d] = M_att
    sim_unique['L_ATT'][d] = L_att
    d = d + 1
"""
#for i in range(int(len(sim_unique['Combo']))):
#    M,L = sizecountML(sim_unique, Tractor, d)
#    sim_unique['M'][d] = M
#    sim_unique['L'][d] = L
#    d = d + 1

print("!!!!After count com")
print("current time:-", dt.now())

sim2 = sim_unique.copy()
sim2.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\sim222.csv')
#sim_unique = sim_unique.drop_duplicates(subset=['M_ACT', 'L_ACT', 'M_ATT', 'L_ATT'], keep='last')
sim_unique = sim_unique.drop_duplicates(subset=['M', 'L'], keep='last')
sim_unique = sim_unique.reset_index(drop=True)
sim_unique.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\sim_unique.csv')
# impute nan at A/C
df_das['aircraft'] = df_das['aircraft'].fillna('77W')
df_das['bay'] = df_das['bay'].fillna('D2')

print(df_das)
print("!!!!ass")
print("current time:-", dt.now())
print(sim_unique.count())
a = 0
fc = 0
for x in range(len(sim_unique.TotalDistance)):
    f = 0
    Tractor_filter = Tractor[Tractor['Tractor_ID'].str.contains('|'.join(sim_unique.Combo[a]))]
    Tractor_filter = Tractor_filter.reset_index(drop=True)
    df_das.drop(df_das.index, inplace=True)
    df_das = df_das_raw.copy()
    df_das['aircraft'] = df_das['aircraft'].fillna('77W')
    df_das['bay'] = df_das['bay'].fillna('D2')
    Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], df_das, Tractor_filter)
    f = f + 1
    if fc == sim_unique.TotalGSE[a] and a != 0:
        sim_unique.TotalDistance[a] = 'No GSE AVA'
    else:
        for j in df_das['flight_number']:
            if f < int(len(df_das['flight_number'])):
                Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], Das_Out, Out)
            f = f + 1
        if Das_Out['Tractor'].loc[(Das_Out['Tractor'] == 'No GSE AVA')].count() == 0:
            sim_unique.TotalDistance[a] = tractor_stat(Das_Out)['Total Distance'].sum()
        else:
            sim_unique.TotalDistance[a] = 'No GSE AVA'
            fc = sim_unique.TotalGSE[a]
    a = a + 1

print("!!!!ass2")
print("current time:-", dt.now())
print("!!!!After sim Unique")
print("current time:-", dt.now())
sim_unique.drop(sim_unique[(sim_unique.TotalDistance == 0) | (sim_unique.TotalDistance == 'No GSE AVA')].index,inplace=True)
sim_unique = sim_unique.sort_values(by='TotalGSE', ascending=False)
sim_unique = sim_unique.sort_values(by='TotalDistance', ascending=True)
sim_unique = sim_unique.reset_index(drop=True)
print(sim_unique)
"""
sim2 = sim2[(sim2.M_ACT == sim_unique['M_ACT'][0]) & (sim2.M_ATT == sim_unique['M_ATT'][0]) & (
            sim2.L_ATT == sim_unique['L_ATT'][0]) & (sim2.L_ACT == sim_unique['L_ACT'][0])]
"""
sim2 = sim2[(sim2.M == sim_unique['M'][0]) & (sim2.L == sim_unique['L'][0])]

sim2 = sim2.reset_index(drop=True)

print(sim2.count())
sim2.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\sim22.csv')


a = 0
fc = 0
for x in range(len(sim2.TotalDistance)):
    f = 0
    Tractor_filter = Tractor[Tractor['Tractor_ID'].str.contains('|'.join(sim2.Combo[a]))]
    Tractor_filter = Tractor_filter.reset_index(drop=True)
    df_das.drop(df_das.index, inplace=True)
    df_das = df_das_raw.copy()
    df_das['aircraft'] = df_das['aircraft'].fillna('77W')
    df_das['bay'] =  df_das['bay'].fillna('D2')
    Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], df_das, Tractor_filter)
    f = f + 1
    if fc == sim2.TotalGSE[a] and a != 0:
        sim2.TotalDistance[a] = 'No GSE AVA'
    else:
        for j in df_das['flight_number']:
            if f < int(len(df_das['flight_number'])):
                Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], Das_Out, Out)
            f = f + 1
        if Das_Out['Tractor'].loc[(Das_Out['Tractor'] == 'No GSE AVA')].count() == 0:
            sim2.TotalDistance[a] = tractor_stat(Das_Out)['Total Distance'].sum()
        else:
            sim2.TotalDistance[a] = 'No GSE AVA'
            fc = sim.TotalGSE[a]
    a = a + 1


sim2.drop(sim2[(sim2.TotalDistance == 0) | (sim2.TotalDistance == 'No GSE AVA')].index, inplace=True)
sim2 = sim2.sort_values(by='TotalDistance', ascending=True)
sim2 = sim2.reset_index(drop=True)


f = 0
Tractor_f = Tractor[Tractor['Tractor_ID'].str.contains('|'.join(sim2.Combo[0]))]
Tractor_f = Tractor_f.reset_index(drop=True)
df_das.drop(df_das.index, inplace=True)
df_das = df_das_raw.copy()
df_das['aircraft'] = df_das['aircraft'].fillna('77W')
df_das['bay'] = df_das['bay'].fillna('D2')

#data_t = {'Flight': [], 'Tractor1': [], 'Tractor2': [], 'Tractor3': [], 'Tractor4': [], 'Tractor5': []}
data_t = {'Flight': [], 'Tractor1': [], 'Tractor2': [], 'Tractor3': [], 'Tractor4': [],
          'Tractor5': [], 'Tractor6': [],'Tractor7': [], 'Tractor8': [], 'Tractor9': [],
          'Tractor10': [],'Tractor11': [], 'Tractor12': [], 'Tractor13': [],
          'Tractor14': [], 'Tractor15': [], 'Tractor16': [],'Tractor17': [],
          'Tractor18': [], 'Tractor19': [], 'Tractor20': []}
data_t2 = {'Flight': [], 'Tractor1': [], 'Tractor2': [], 'Tractor3': [], 'Tractor4': [],
          'Tractor5': [], 'Tractor6': [],'Tractor7': [], 'Tractor8': [], 'Tractor9': [],
          'Tractor10': [],'Tractor11': [], 'Tractor12': [], 'Tractor13': [],
          'Tractor14': [], 'Tractor15': [], 'Tractor16': [],'Tractor17': [],
          'Tractor18': [], 'Tractor19': [], 'Tractor20': []}
Tractor_option = pd.DataFrame(data_t)
Tractor_option2 = pd.DataFrame(data_t2)
Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], df_das, Tractor_f)

log = {'Flight': [], 'Tractor1': [], 'Tractor2': [], 'Tractor3': [], 'Tractor4': [],
          'Tractor5': [], 'Tractor6': [],'Tractor7': [], 'Tractor8': [], 'Tractor9': [],
          'Tractor10': [],'Tractor11': [], 'Tractor12': [], 'Tractor13': [],
          'Tractor14': [], 'Tractor15': [], 'Tractor16': [],'Tractor17': [],
          'Tractor18': [], 'Tractor19': [], 'Tractor20': []}

log2 = {'Flight': [], 'Tractor1': [], 'Tractor2': [], 'Tractor3': [], 'Tractor4': [],
          'Tractor5': [], 'Tractor6': [],'Tractor7': [], 'Tractor8': [], 'Tractor9': [],
          'Tractor10': [],'Tractor11': [], 'Tractor12': [], 'Tractor13': [],
          'Tractor14': [], 'Tractor15': [], 'Tractor16': [],'Tractor17': [],
          'Tractor18': [], 'Tractor19': [], 'Tractor20': []}
mask = Tractor['Tractor_ID'].isin(Out['Tractor_ID'])
notmask = ~mask
selected_values = Tractor['Tractor_ID'][notmask].reset_index(drop=True)
cnt=0
for idx, (key, value) in enumerate(log.items()):
  if idx < Out['Tractor_ava'].count():
      if idx == 0:
        log[key] = df_das['flight_number'][f]
      else:
        log[key] = Out['Tractor_ID'][idx]
  else:
        log[key] = "  "
for idx, (key, value) in enumerate(log2.items()):
  if idx < selected_values.count():
      if idx == 0:
          log2[key] = df_das['flight_number'][f]
      else:
          log2[key] = selected_values[idx-1]

  else:
      if idx == selected_values.count():
          log2[key] = selected_values[idx-1]
      else:
        log2[key] = "  "


app_log = pd.DataFrame(log, index=[0])
Tractor_option = Tractor_option.append(app_log)
app_log2 = pd.DataFrame(log2, index=[0])
Tractor_option2 = Tractor_option2.append(app_log2)
f = f + 1
for j in df_das['flight_number']:
    if f < int(len(df_das['flight_number'])):
        Out, Das_Out = assign_best_GSE(df_das['flight_number'][f], Das_Out, Out)
        mask = Tractor['Tractor_ID'].isin(Out['Tractor_ID'])
        notmask = ~mask
        selected_values = Tractor['Tractor_ID'][notmask].reset_index(drop=True)
        cnt = 0
        for idx, (key, value) in enumerate(log.items()):
            if idx < Out['Tractor_ava'].count():
                if idx == 0:
                    log[key] = df_das['flight_number'][f]
                else:
                    log[key] = Out['Tractor_ID'][idx]
            else:
                log[key] = "  "
        for idx, (key, value) in enumerate(log2.items()):
            if idx < selected_values.count():
                if idx == 0:
                    log2[key] = df_das['flight_number'][f]
                else:
                    log2[key] = selected_values[idx-1]
            else:
                if idx == selected_values.count():
                    log2[key] = selected_values[idx - 1]
                else:
                    log2[key] = "  "
        app_log = pd.DataFrame(log, index=[0])
        Tractor_option = Tractor_option.append(app_log)
        app_log2 = pd.DataFrame(log2, index=[0])
        Tractor_option2 = Tractor_option2.append(app_log2)
    f = f + 1
Tractor_option = Tractor_option.reset_index(drop=True)
Tractor_option2 = Tractor_option2.reset_index(drop=True)

print("!!!!Workplan")
print("current time:-", dt.now())
print(Das_Out)

print(tractor_stat(Das_Out))

Tractor_Out = combine_tractor(Tractor_Out, Out)

print("!!!!End")
print("current time:-", dt.now())
df_das.to_json(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_das.json')
df_das.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_das.csv')
df_das_raw.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_das_raw.csv')
df_raws.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_raws.csv')
df_show = df_das[['flight_number','aircraft','bay','Time','Tractor']]
df_show.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_show.csv')

Tractor_Out.to_json(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Out.json')
Tractor_Out.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Out.csv')
tractor_stat(Das_Out).to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_stat_out.csv')

Tractor_option.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option.csv')
Tractor_option2.to_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option2.csv')

