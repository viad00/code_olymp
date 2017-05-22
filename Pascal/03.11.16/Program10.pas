const
  N = 30;

var
  a: array [1..N] of integer; 
  i, j, min: integer;

begin
  Randomize();
  for i := 1 to N do begin a[i] := Random(0, 100);write(a[i], ' '); end;
  writeln();
  min:=100;
  for i := 1 to N do 
  begin
    if (a[i] > 20) and (min > a[i]) then min := a[i];
  end;
  writeln(min);
end.