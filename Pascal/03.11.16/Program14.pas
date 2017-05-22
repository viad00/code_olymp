const
  N = 30;

var
  a: array [1..N] of integer; 
  i, k, max, max2: integer;

begin
  Randomize();
  for i := 1 to N do begin a[i] := Random(9);write(a[i], ' '); end;
  writeln();
  k := 0;
  max := 0;
  max2 := 0;
  for i := 1 to N do 
  begin
    if a[i] > max then begin
      max2 := max;
      max := a[i];
    end;
  end;
  writeln(max2);
end.