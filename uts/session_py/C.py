w, h, xo, yo, x, y = map(int, input().split())

l = abs(x-xo)+abs(y-yo)
ll = yo + abs(h-y) + abs(x-xo)
lll = h-yo+y+abs(x-xo)
llll = xo+abs(w-x)+abs(y-yo)
lllll = w-xo+x+abs(y-yo)
llllll = xo+yo+abs(h-y)+abs(w-x)
lllllll = abs(h-yo)+abs(w-xo)+x+y
print(min(l,ll,lll,llll,lllll,llllll,lllllll))
