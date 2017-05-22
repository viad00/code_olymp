const
  N = 4;

var
  a: array [1..N, 1..N] of integer; 
  i, j: integer;
  d: real;

begin
  Randomize();
  for i := 1 to N do begin for j := 1 to N do begin a[i][j] := Random(5);write(a[i][j], ' '); end;writeln(); end;
  writeln();
  d:=0;
  for i := 1 to N do 
  begin
    for j := 1 to N do 
    begin
      d:=d+a[i][j];
    end;
  end;
  d:=d/N;
  writeln(d);
end.