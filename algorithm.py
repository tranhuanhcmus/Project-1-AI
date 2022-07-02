from queue import PriorityQueue
import queue
import pygame

def reconstruct_path(came_from, current, draw):
	cost=0
	while current in came_from:
		current = came_from[current]
		current.make_path()
		cost=cost+1
		draw()
	return cost

def Manhattan(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)
	
def A_Star(draw, grid, start, end):
	count_open_node = 0
	frontier = PriorityQueue()
	frontier.put((0, count_open_node, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = Manhattan(start.get_pos(), end.get_pos())

	open_set = {start}

	while not frontier.empty():

		current = frontier.get()[2]
		open_set.remove(current)

		if current == end:
			cost=reconstruct_path(came_from, end, draw)
			end.make_end()
			print("Cost:",cost)
			print("Number of Open Node:",count_open_node)
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor] :
				if current != start:
					came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + Manhattan(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set:
					count_open_node += 1
					frontier.put((f_score[neighbor], count_open_node, neighbor))
					open_set.add(neighbor)
					neighbor.make_open()

		draw()


	return False

def UCS(draw, grid, start, end):
	count_open_node = 0
	frontier = PriorityQueue()
	frontier.put((0, count_open_node, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0

	open_set = {start}

	while not frontier.empty():

		current = frontier.get()[2]
		open_set.remove(current)

		if current == end:
			cost=reconstruct_path(came_from, end, draw)
			end.make_end()
			print("Cost:",cost)
			print("Number of Open Node:",count_open_node)
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor] :
				if current != start:
					came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				if neighbor not in open_set:
					count_open_node += 1
					frontier.put((g_score[neighbor], count_open_node, neighbor))
					open_set.add(neighbor)
					neighbor.make_open()

		draw()


	return False

def GreedyBestFirstSearch(draw, grid, start, end):
	count_open_node = 0
	frontier = PriorityQueue()
	frontier.put((0, count_open_node, start))
	came_from = {}
	
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = Manhattan(start.get_pos(), end.get_pos())

	open_set = {start}

	while not frontier.empty():

		current = frontier.get()[2]
		open_set.remove(current)

		if current == end:
			cost=reconstruct_path(came_from, end, draw)
			end.make_end()
			print("Cost:",cost)
			print("Number of Open Node:",count_open_node)
			return True

		for neighbor in current.neighbors:
			temp_f_score = Manhattan(neighbor.get_pos(), end.get_pos())

			if temp_f_score < f_score[neighbor] :
				if current != start:
					came_from[neighbor] = current
				f_score[neighbor] = temp_f_score
				
				if neighbor not in open_set:
					count_open_node += 1
					frontier.put((f_score[neighbor], count_open_node, neighbor))
					open_set.add(neighbor)
					neighbor.make_open()

		draw()


	return False


def BFS(draw, grid, start, end):
	count_open_node = 0
	frontier = queue.Queue()
	frontier.put((count_open_node, start))
	came_from = {}

	open_set = {start}

	while not frontier.empty():

		current = frontier.get()[1]
		if current == end:
			cost=reconstruct_path(came_from, end, draw)
			end.make_end()
			print("Cost:",cost)
			print("Number of Open Node:",count_open_node)
			return True

		for neighbor in current.neighbors:
				if neighbor not in open_set:
					count_open_node += 1
					frontier.put((count_open_node, neighbor))
					if current != start:
						came_from[neighbor] = current
					open_set.add(neighbor)
					neighbor.make_open()

		

		draw()


	return False

def DFS(draw, grid, start, end):
	count_open_node = 0
	frontier = queue.LifoQueue()
	frontier.put((count_open_node, start))
	came_from = {}

	open_set = {start}

	while not frontier.empty():

		current = frontier.get()[1]
		if current == end:
			cost=reconstruct_path(came_from, end, draw)
			end.make_end()
			print("Cost:",cost)
			print("Number of Open Node:",count_open_node)
			return True

		for neighbor in current.neighbors:
				if neighbor not in open_set:
					count_open_node += 1
					frontier.put((count_open_node, neighbor))
					if current != start:
						came_from[neighbor] = current
					open_set.add(neighbor)
					neighbor.make_open()

		

		draw()


	return False
