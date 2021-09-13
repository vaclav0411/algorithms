def solution(root, max_light=-float('inf')):
    if root is None:
        return max_light

    if root.value >= max_light:
        max_light = root.value
    right = solution(root.right, max_light)
    left = solution(root.left, max_light)
    if right > max_light and left > max_light:
        if right and left:
            return right if right > left else left
    if left < max_light and right < max_light:
        return max_light
    return right if right > max_light else left
