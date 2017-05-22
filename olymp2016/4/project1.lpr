program project1;
var
  k,l,m,n: integer;
begin
  writeln('k,l,m,n');
  readln(k,l,m,n);
  if (k+l+m+n) mod 2=0 then writeln('Одинаковы')
  else writeln('Разные');
end.

