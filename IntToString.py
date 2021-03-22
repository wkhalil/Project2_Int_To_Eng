def numberToWords(num: int) -> str:
    l1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
          'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
          'Eighteen', 'Nineteen']
    l2 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    l3 = ['', 'Thousand', 'Million', 'Billion']

    def trans(num):
        out = ''
        if num >= 100:
            out += l1[num // 100] + ' Hundred'
            num %= 100
        if num >= 20:
            out += ' ' + l2[num // 10]
            num %= 10
        if num > 0:
            out += ' ' + l1[num]
        return out

    if not num:
        return 'Zero'
    arr = []
    while num:
        arr.append(num % 1000)
        num //= 1000

    res = []
    for i in range(len(arr)):
        tmp = trans(arr[i])
        if tmp:
            tmp = tmp + ' ' + l3[i]
            res.append(tmp.strip())

    ans = ' '.join(res[::-1])
    return ans.strip()


if __name__ == '__main__':
    print(numberToWords(110))