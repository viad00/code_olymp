program gr;
var N, g:integer;
begin
writeln('Число, del');
Readln(N, g);
if N div 100 = g then write(N div 100,'   ');
N:=N mod 100;
if N div 10 = g then write(N div 10,'   ');
N:=N mod 10;
if N div 1 = g then write(N div 1,'   ');
N:=N mod 1;
end.