Program pr1;
var r1, r2: integer;
s1, s2: real;
begin
writeln('������ 1');
readln(r1);
writeln('������ 2');
readln(r2);
s1:=Pi*r1*r1;
writeln('������� 1 = ', s1);
s2:=Pi*r2*r2;
writeln('������� 2 = ', s2);
writeln('������ = ', s2 - s1);
end.