var a, b, c, d: real;
begin
writeln('перчаток, портфеля, галстука, Исходная сумма');
Readln(a, b, c, d);
if d-a-b-c >= 0 then writeln('Ваш сдач', d-a-b-c)
else
writeln('Не хватать', d-a-b-c)
end.