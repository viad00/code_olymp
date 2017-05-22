program gr;
var N:integer;
begin
writeln('Число');
Readln(N);
write(N div 10000,'   ');
N:=N mod 10000;
write(N div 1000,'   ');
N:=N mod 1000;
write(N div 100,'   ');
N:=N mod 100;
write(N div 10,'   ');
N:=N mod 10;
write(N div 1,'   ');
N:=N mod 1;
end.