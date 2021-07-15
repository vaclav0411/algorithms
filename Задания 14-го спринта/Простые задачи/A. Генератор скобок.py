def generate_brackets(n: int, k: int, prefix='', lead=0, trailing=0):
    if n == 0:
        print(prefix)
    else:
        if lead < k and trailing > 0:
            generate_brackets(n-1, k, prefix+'(', lead+1, trailing+1)
            generate_brackets(n-1, k, prefix+')', lead, trailing-1)
        elif trailing > 0:
            generate_brackets(n-1, k, prefix+')', lead, trailing-1)
        elif lead < k:
            generate_brackets(n-1, k, prefix+'(', lead+1, trailing+1)


if __name__ == "__main__":
    half = int(input())
    amount = 2 * half
    generate_brackets(amount, half)
