from homework_5.tracer.tracer import tracer


def permutations(array: list):
    permutations = []
    enable = [True] * len(array)

    @tracer
    def inner_permutation(permutation: list):
        if len(permutation) == len(array):
            permutations.append(permutation.copy())
            return
        for i in range(len(array)):
            if enable[i]:
                permutation.append(array[i])
                enable[i] = False
                inner_permutation(permutation)
                enable[i] = True
                permutation.pop()

    inner_permutation([])
    return permutations


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
