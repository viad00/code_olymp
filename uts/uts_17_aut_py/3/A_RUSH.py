from itertools import permutations
import zlib, json
#n = int(input()) # Лучше не смотреть на это НЕ решение)
#pool = list(map(int, input().split()))
#ans = sum(pool)//2
'''dis = {
    206: 207,
    155: 156,
    355: 360,
    356: 361,
    277: 278,
    380: 381,
    464: 465,
    54: 103,
    311: 343
}'''
dis = {

}
print(json.dumps(dis))
print(json.loads(json.dumps(dis)))
kek = zlib.compress(bytearray(json.dumps(dis), encoding='UTF-8'), level=-1)
print(kek)
print(json.loads(str(zlib.decompress(kek), encoding='UTF-8')))
#if ans in dis:
#    ans = dis[ans]
#print(ans)
