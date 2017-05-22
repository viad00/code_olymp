var
  a: array[1..10, 1..20] of integer;
  i, j, sum, ssum, ssumk: integer;

begin
  for i := 1 to 10 do begin write(i, ': ');for j := 1 to 20 do begin a[i, j] := random(10);write(a[i, j], ' '); end;writeln; end;
  writeln();
  ssum := 9999;
  for i := 1 to 10 do 
  begin
    sum := 0;
    for j := 1 to 20 do 
    begin
      sum := sum + a[i, j];
    end;
    if sum < ssum then begin
      ssum := sum;
      ssumk := i;
    end;
  end;
  writeln(ssumk, ': ', ssum);
end.