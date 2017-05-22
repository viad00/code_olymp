program gr;
var N, sum:integer;
begin
writeln('Число');
Readln(N);
sum:=sum+N div 10000;
write(N div 10000,'   ');
N:=N mod 10000;
sum:=sum+N div 1000;
write(N div 1000,'   ');
N:=N mod 1000;
sum:=sum+N div 100;
write(N div 100,'   ');
N:=N mod 100;
sum:=sum+N div 10;
write(N div 10,'   ');
N:=N mod 10;
sum:=sum+N div 1;
write(N div 1,'   ');
N:=N mod 1;
write(sum);
end.