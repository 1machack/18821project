import random
import math

def gen_random_unit_vector(dimension):
	vec = [random.gauss(0, 1) for i in range(dimension)]
	return normalize(vec)
	
def normalize(vec):
	vec_square = map(lambda x: x*x, vec)
	vec_length = math.sqrt(reduce(lambda x, y: x+y, vec_square))
	return map(lambda x: x/vec_length, vec)

def compute_max_dp(vecs):
	max_dp = 0
	for i in range(len(vecs)):
		for j in range(i+1, len(vecs)):
			dp = reduce(lambda x, y: x+y, map(lambda x, y: x*y, vecs[i], vecs[j]))
			dp = dp*dp
			if dp>max_dp:
				max_dp=dp
	return max_dp



def try_random(dimension=3, num_vectors=5, num_tries=100):
	min_max_dp = 1
	min_vecs = []
	for i in range(num_tries):
		random_vecs = [gen_random_unit_vector(dimension) for j in range(num_vectors)]
		max_dp = compute_max_dp(random_vecs)
		if max_dp<min_max_dp:
			min_max_dp = max_dp
			min_vecs = random_vecs
	return min_max_dp, min_vecs

