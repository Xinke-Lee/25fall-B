import sys


def solve():
    # 读取所有输入，按空格分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2

        # 结束标志
        if n == 0 and m == 0:
            break

        # 按照题目描述，前 n 个是面值 A，后 n 个是数量 C
        a = []
        for i in range(n):
            a.append(int(input_data[ptr + i]))
        ptr += n

        c = []
        for i in range(n):
            c.append(int(input_data[ptr + i]))
        ptr += n

        # bits 的第 k 位为 1 表示金额 k 可以凑出
        # 初始只有 bits[0] = 1
        bits = 1
        # 掩码，用于限制金额不超过 m (即全 1 的二进制，长度为 m+1)
        mask = (1 << (m + 1)) - 1

        for i in range(n):
            val = a[i]
            count = c[i]

            # 优化：如果该种硬币总面值已超过 m，则视为无限个（完全背包）
            # 或者直接进行二进制拆分
            k = 1
            while k <= count:
                bits |= (bits << (k * val))
                bits &= mask  # 及时截断，保证位运算效率
                count -= k
                k *= 2

            if count > 0:
                bits |= (bits << (count * val))
                bits &= mask

            # 剪枝：如果 1 到 m 全都能凑出了，直接退出
            if bits == mask:
                break

        # 计算 bits 中 1 的个数（排除掉第 0 位，因为题目要求金额从 1 到 m）
        # Python 3.10+ 使用 bit_count()，旧版本使用 bin().count('1')
        if hasattr(bits, "bit_count"):
            ans = bits.bit_count() - 1
        else:
            ans = bin(bits).count('1') - 1

        sys.stdout.write(str(ans) + '\n')


if __name__ == "__main__":
    solve()