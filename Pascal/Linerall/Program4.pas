Program pr1;
var r1, r2: integer;
s1, s2: real;
begin
writeln('Радиус 1');
readln(r1);
writeln('Радиус 2');
readln(r2);
s1:=Pi*r1*r1;
writeln('Площадь 1 = ', s1);
s2:=Pi*r2*r2;
writeln('Площадь 2 = ', s2);
writeln('Кольцо = ', s2 - s1);
end.