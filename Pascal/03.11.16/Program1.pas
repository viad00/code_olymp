var
  a: array[1..30] of integer;
  i, k, ki, kmax, kimax: integer;

begin
  for i := 1 to 30 do begin a[i] := random(10);write(a[i], ' '); end;
  writeln();
  kmax := 0;
  kimax := 0;
  for i := 1 to 29 do 
  begin
    ki := i;
    k := a[i] + a[i + 1];
    if k > kmax then 
    begin
      kmax:=k;
      kimax:=ki;
    end;
  end;
  writeln(kimax, ':= ', kmax);
end.