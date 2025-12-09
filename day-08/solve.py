"""Day 08 Puzzle Solution"""

import argparse

import numpy as np
import scipy


def data_vectors(data) -> np.ndarray:
    """Turn data into (N,3) matrix containing N 3-dimentional vectors"""

    # 3 Dimensional vectors for keeping track of x,y,z
    number_of_junction_boxes = len(data)
    spatial_coords = np.ndarray((number_of_junction_boxes, 3))
    for idx, line in enumerate(data):
        spatial_coords[idx] = np.array([int(val) for val in line.split(",")])

    return spatial_coords


def solution1(data, num_closest=10, num_largest_circuits=3):
    """Solution to part 1"""

    spatial_coords = data_vectors(data)

    # Find the distance between all junctions
    pairwise_distances = scipy.spatial.distance.pdist(spatial_coords, "euclidean")
    n_closest_positions = pairwise_distances.argsort()[:num_closest]

    distance_matrix = scipy.spatial.distance.squareform(pairwise_distances)
    distance_matrix_upper = np.triu(distance_matrix)

    # Store the indexes of the closest junction boxes
    # These values represent which junction box is closest to which
    indexes = np.ndarray((num_closest, 2), dtype=int)
    for idx, value in enumerate(pairwise_distances[n_closest_positions]):
        indexes[idx] = [int(x[0]) for x in np.where(distance_matrix_upper == value)]

    # Indexes contain all the closest junction boxes, now we need to combine all the sublists with
    # common values
    connected_junctions = []
    for pair in indexes:
        index_set = set(pair)

        matching_groups = []
        for i, junction in enumerate(connected_junctions):
            if index_set.intersection(junction):
                matching_groups.append(i)

        if not matching_groups:
            connected_junctions.append(pair)
        else:
            merged_group = index_set
            for idx in sorted(matching_groups, reverse=True):
                merged_group = merged_group.union(connected_junctions.pop(idx))
            connected_junctions.append(merged_group)

    connected_junctions = [list(junction) for junction in connected_junctions]

    product = 1
    for idx in range(num_largest_circuits):
        largest_circuit = max(connected_junctions, key=len)
        connected_junctions.pop(connected_junctions.index(largest_circuit))
        # print(len(largest_circuit), largest_circuit)

        product *= len(largest_circuit)

    return product


def solution2(data):
    """Solution to part 2"""

    spatial_coords = data_vectors(data)

    # Find the distance between all junctions
    pairwise_distances = scipy.spatial.distance.pdist(spatial_coords, "euclidean")
    n_closest_positions = pairwise_distances.argsort()

    distance_matrix = scipy.spatial.distance.squareform(pairwise_distances)
    distance_matrix_upper = np.triu(distance_matrix)
    # print(distance_matrix_upper)

    indexes = np.ndarray((len(n_closest_positions), 2), dtype=int)
    for idx, value in enumerate(pairwise_distances[n_closest_positions]):
        indexes[idx] = [int(x[0]) for x in np.where(distance_matrix_upper == value)]

    connected_junctions = []
    for pair in indexes:
        index_set = set(pair)

        matching_groups = []
        for i, junction in enumerate(connected_junctions):
            if index_set.intersection(junction):
                matching_groups.append(i)

        if not matching_groups:
            # No intersection found, adding as own pair
            connected_junctions.append(pair)
        else:
            merged_group = index_set
            for idx in sorted(matching_groups, reverse=True):
                # print("matching groups", matching_groups)
                merged_group = merged_group.union(connected_junctions.pop(idx))
            connected_junctions.append(merged_group)

            connected_junctions = [list(junction) for junction in connected_junctions]

            if len(connected_junctions[0]) == len(spatial_coords):
                break

    return int(np.prod([x[0] for x in spatial_coords[pair]]))


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-08/input.txt" if not args.debug else "day-08/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    if args.debug:
        answ1 = solution1(data)
    else:
        answ1 = solution1(data, num_closest=1000)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
