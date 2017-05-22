program Project1;
var
  f, f1: text;
  N, sum, sum1: integer;
begin
  assign (f, 'zadanie1.txt');
  reset (f);
  read (f, N);
  close (f);
  writeln(N);
  sum:=sum+N div 100000;
N:=N mod 100000;
  sum:=sum+N div 10000;
N:=N mod 10000;
sum:=sum+N div 1000;
N:=N mod 1000;
sum1:=sum1+N div 100;
N:=N mod 100;
sum1:=sum1+N div 10;
N:=N mod 10;
sum1:=sum1+N div 1;
N:=N mod 1;
assign (f, 'rezultat1.txt');
rewrite (f);

if sum = sum1 then begin
  write (f, 'schastlyviy');
  writeln ('schastlyviy');
end
else begin
  write (f, 'neschastliviy');
  writeln ('neschastliviy');
end;
end.
close (f);
end.

