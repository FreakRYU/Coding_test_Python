def solution(n, m, section):
    cnt = 0
    z = 0
    # section 순회
    for i in section:
        # z가 i번 벽돌보다 작은 수이면 갱신 및 카운트
        if z == 0 or z < i:
            z = i + m - 1
            cnt += 1
        else:
            continue

    return cnt