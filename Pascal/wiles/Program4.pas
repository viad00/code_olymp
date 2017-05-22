var n,m,a:integer;
begin
write('Введите число: ');
readln(n);
while n>0 do begin
a:=n mod 10;
n:=n div 10;
m:=m*10+a;
end;
write('Число в обратном порядке - ', m);
end.